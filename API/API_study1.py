"""
구성
1) 금융감독원 정기예금 API (depositProductsSearch)
2) OpenWeatherMap Current Weather API
"""

from __future__ import annotations

from typing import Any, Dict, List, Iterable, Optional
import requests


# ---------------------------------------------------------------------
# 공통 유틸: HTTP GET + JSON 파싱
# ---------------------------------------------------------------------
def fetch_json(url: str, params: Optional[Dict[str, Any]] = None, timeout: int = 10) -> Dict[str, Any]:
    """
    1) requests.get()으로 데이터 '수집' (API 호출)
    2) response.json()으로 데이터 '가공' (파이썬 dict/list 형태로 변환)

    - params를 쓰면 URL 뒤에 ?a=1&b=2 같은 쿼리스트링이 자동으로 붙습니다.
    - timeout은 응답이 너무 오래 걸릴 때 멈추게 하는 안전장치입니다.
    """
    resp = requests.get(url, params=params, timeout=timeout)
    resp.raise_for_status()  # HTTP 오류(4xx/5xx)면 예외 발생 → 문제 원인 파악이 쉬워짐
    return resp.json()


# =====================================================================
# 1) 금융감독원 정기예금 API: depositProductsSearch
# =====================================================================
DEPOSIT_BASE_URL = "http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"


def deposit_get_result_keys(api_key: str, top_fin_grp_no: str = "020000", page_no: int = 1) -> List[str]:
    """
    [문제1] 전체 응답(JSON)에서 "result"의 '키 목록'만 뽑는 함수

    흐름
    - fetch_json()으로 API 호출
    - data["result"]에 핵심 데이터가 있으니 그 딕셔너리의 keys()를 반환
    """
    params = {
        "auth": api_key,
        "topFinGrpNo": top_fin_grp_no,
        "pageNo": page_no,
    }
    data = fetch_json(DEPOSIT_BASE_URL, params=params)

    # result는 dict이므로 keys()를 하면 키 목록이 나온다.
    return list(data["result"].keys())


def deposit_get_base_list(api_key: str, top_fin_grp_no: str = "020000", page_no: int = 1) -> List[Dict[str, Any]]:
    """
    [문제2] "result" 안의 "baseList" (상품 기본정보 리스트)만 뽑는 함수

    baseList 예시(대략)
    - 금융회사명, 상품명, 금융상품코드 등 "상품 자체" 정보가 들어있음
    """
    params = {
        "auth": api_key,
        "topFinGrpNo": top_fin_grp_no,
        "pageNo": page_no,
    }
    data = fetch_json(DEPOSIT_BASE_URL, params=params)
    return data["result"]["baseList"]


def deposit_get_option_list_slim(api_key: str, top_fin_grp_no: str = "020000", page_no: int = 1) -> List[Dict[str, Any]]:
    """
    [문제3] "optionList"(상품별 금리 옵션 리스트)를 돌면서
           필요한 필드만 뽑아 새 리스트로 만들기

    - 원본 optionList는 필드가 많은데,
      여기서는 실습에서 만든 것처럼 필요한 키만 새 딕셔너리에 담아 반환한다.
    """
    params = {
        "auth": api_key,
        "topFinGrpNo": top_fin_grp_no,
        "pageNo": page_no,
    }
    data = fetch_json(DEPOSIT_BASE_URL, params=params)
    option_list = data["result"]["optionList"]

    result: List[Dict[str, Any]] = []
    for opt in option_list:
        # opt.get("키")를 쓰면 해당 키가 없어도 KeyError 대신 None을 준다(안전)
        result.append(
            {
                "금융상품코드": opt.get("fin_prdt_cd"),
                "저축 금리": opt.get("intr_rate"),
                "저축 기간": opt.get("save_trm"),
                "저축금리유형": opt.get("intr_rate_type"),
                "저축금리유형명": opt.get("intr_rate_type_nm"),
                "최고 우대금리": opt.get("intr_rate2"),
            }
        )

    return result


def deposit_merge_base_and_options(api_key: str, top_fin_grp_no: str = "020000", page_no: int = 1) -> List[Dict[str, Any]]:
    """
    [문제4] baseList(상품)와 optionList(옵션)를 "금융상품코드(fin_prdt_cd)" 기준으로 매칭해서
           아래 형태의 새 리스트로 반환한다.

    출력 형태(실습 기준)
    [
      {
        "금융회사명": "...",
        "금융상품명": "...",
        "금리정보": [
           {"저축 금리": ..., "저축금리유형": ..., ...},
           ...
        ]
      },
      ...
    ]

    핵심 아이디어
    - baseList에서 상품코드를 하나 뽑는다.
    - optionList에서 동일한 상품코드를 가진 옵션들을 전부 찾아 "금리정보" 리스트로 묶는다.
    """
    params = {
        "auth": api_key,
        "topFinGrpNo": top_fin_grp_no,
        "pageNo": page_no,
    }
    data = fetch_json(DEPOSIT_BASE_URL, params=params)
    base_list = data["result"]["baseList"]
    option_list = data["result"]["optionList"]

    result: List[Dict[str, Any]] = []

    for base in base_list:
        product_code = base.get("fin_prdt_cd")

        # 같은 상품코드를 가진 옵션들을 모아둔다.
        rate_infos: List[Dict[str, Any]] = []
        for opt in option_list:
            if opt.get("fin_prdt_cd") == product_code:
                rate_infos.append(
                    {
                        "저축 금리": opt.get("intr_rate"),
                        "저축금리유형": opt.get("intr_rate_type"),
                        "저축금리유형명": opt.get("intr_rate_type_nm"),
                        "최고 우대금리": opt.get("intr_rate2"),
                    }
                )

        product_dict = {
            "금융회사명": base.get("kor_co_nm"),
            "금융상품명": base.get("fin_prdt_nm"),
            "금리정보": rate_infos,
        }
        result.append(product_dict)

    return result


# =====================================================================
# 2) OpenWeatherMap Current Weather API
# =====================================================================
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def weather_fetch_raw(api_key: str, lat: float, lon: float) -> Dict[str, Any]:
    """
    OpenWeatherMap API에서 현재 날씨를 '수집'해서 원본 JSON(dict) 그대로 반환
    """
    params = {"lat": lat, "lon": lon, "appid": api_key}
    return fetch_json(WEATHER_BASE_URL, params=params)


def weather_get_top_level_keys(api_key: str, lat: float, lon: float) -> List[str]:
    """
    [문제1] 응답(JSON)의 최상위 키 목록만 확인
    - data.keys()는 dict의 키 뷰(view) → list로 변환해서 반환
    """
    data = weather_fetch_raw(api_key, lat, lon)
    return list(data.keys())


def weather_get_main_and_weather(api_key: str, lat: float, lon: float) -> Dict[str, Any]:
    """
    [문제2] 최상위에서 "main"과 "weather"만 뽑아서 새 dict로 반환

    - main: 온도/습도/기압 등 '수치'
    - weather: 날씨 요약(텍스트/아이콘/id 등) 리스트
    """
    data = weather_fetch_raw(api_key, lat, lon)
    return {
        "main": data["main"],
        "weather": data["weather"],
    }


def weather_korean_keys(api_key: str, lat: float, lon: float) -> Dict[str, Any]:
    """
    [문제3] main/weather 안의 키들을 한국어 키로 매핑해서 반환

    주의
    - weather는 리스트이므로 data["weather"][0] 처럼 첫 번째 요소(dict)를 꺼내서 사용
    """
    data = weather_fetch_raw(api_key, lat, lon)
    main_data = data["main"]
    weather_data = data["weather"][0]

    return {
        "기본": {
            "체감온도": main_data["feels_like"],
            "습도": main_data["humidity"],
            "기압": main_data["pressure"],
            "온도": main_data["temp"],
            "최고온도": main_data["temp_max"],
            "최저온도": main_data["temp_min"],
        },
        "날씨": {
            "요약": weather_data["description"],
            "아이콘": weather_data["icon"],
            "핵심": weather_data["main"],
            "식별자": weather_data["id"],
        },
    }


def kelvin_to_celsius(k: float, ndigits: int = 2) -> float:
    """
    켈빈(K) → 섭씨(°C)
    - OpenWeatherMap은 기본 단위가 Kelvin이라서 (K - 273.15) 변환이 자주 필요함
    """
    return round(k - 273.15, ndigits)


def weather_korean_with_celsius(api_key: str, lat: float, lon: float) -> Dict[str, Any]:
    """
    [문제4] 문제3(C)의 구조를 유지하면서 섭씨 값을 추가한 버전
    """
    data = weather_fetch_raw(api_key, lat, lon)
    main_data = data["main"]
    weather_data = data["weather"][0]

    return {
        "기본": {
            "체감온도": main_data["feels_like"],
            "체감온도(섭씨)": kelvin_to_celsius(main_data["feels_like"]),
            "습도": main_data["humidity"],
            "기압": main_data["pressure"],
            "온도": main_data["temp"],
            "온도(섭씨)": kelvin_to_celsius(main_data["temp"]),
            "최고온도": main_data["temp_max"],
            "최고온도(섭씨)": kelvin_to_celsius(main_data["temp_max"]),
            "최저온도": main_data["temp_min"],
            "최저온도(섭씨)": kelvin_to_celsius(main_data["temp_min"]),
        },
        "날씨": {
            "요약": weather_data["description"],
            "아이콘": weather_data["icon"],
            "핵심": weather_data["main"],
            "식별자": weather_data["id"],
        },
    }


# ---------------------------------------------------------------------
# 실행 예시 (직접 실행할 때만 동작)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # ⚠️ 아래는 예시입니다. 실제 키를 넣어야 동작합니다.
    # - 금융감독원 키 / OpenWeatherMap 키는 서로 다르니 구분해서 넣으세요.
    deposit_api_key = "YOUR_FSS_API_KEY"
    weather_api_key = "YOUR_OPENWEATHER_KEY"

    # 예시 좌표(서울 시청 근처)
    seoul_lat, seoul_lon = 37.56, 126.97

    # 1) 정기예금 API 예시
    # print(deposit_get_result_keys(deposit_api_key))
    # print(deposit_get_base_list(deposit_api_key)[:1])
    # print(deposit_get_option_list_slim(deposit_api_key)[:2])
    # print(deposit_merge_base_and_options(deposit_api_key)[:1])

    # 2) 날씨 API 예시
    # print(weather_get_top_level_keys(weather_api_key, seoul_lat, seoul_lon))
    # print(weather_get_main_and_weather(weather_api_key, seoul_lat, seoul_lon))
    # print(weather_korean_keys(weather_api_key, seoul_lat, seoul_lon))
    # print(weather_korean_with_celsius(weather_api_key, seoul_lat, seoul_lon))
