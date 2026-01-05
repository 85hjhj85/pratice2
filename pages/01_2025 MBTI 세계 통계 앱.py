import streamlit as st
import pandas as pd

st.set_page_config(page_title="MBTI World Tour", page_icon="🌎")

st.title("🌎 2025 MBTI 세계 통계 앱")
st.markdown("""
### 이 앱은 무엇을 하나요?
제공된 국가별 MBTI 데이터를 바탕으로, 전 세계의 성격 분포를 탐험합니다.
왼쪽 사이드바를 이용해 원하는 페이지로 이동하세요!

1. **🌍 MBTI 세계지도**: 유형별 전 세계 분포 확인
2. **✈️ 소울 국가 찾기**: 나와 가장 잘 맞는 국가 매칭
3. **⚔️ 국가 간 비교**: 두 나라의 성향 차이 분석
4. **💎 희귀도 분석**: 특정 국가에서 내가 얼마나 특별한지 확인
""")

# 데이터 로드 (다른 페이지에서도 사용 가능하게 캐싱)
@st.cache_data
def load_data():
    return pd.read_csv('countriesMBTI_16types.csv')

df = load_data()
st.info(f"현재 총 {len(df)}개국의 데이터가 로드되었습니다.")
st.dataframe(df.head())
