import streamlit as st

# 페이지 설정
st.set_page_config(page_title="2025 MBTI 궁합기", page_icon="❤️", layout="centered")

# 간단한 CSS 스타일링
st.markdown("""
    <style>
    .stSelectbox { color: #ff4b4b; }
    .result-card { padding: 20px; border-radius: 15px; background-color: #f0f2f6; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# MBTI 목록
mbti_list = [
    'ENFP', 'ENFJ', 'ENTP', 'ENTJ', 
    'ESFP', 'ESFJ', 'ESTP', 'ESTJ',
    'INFP', 'INFJ', 'INTP', 'INTJ', 
    'ISFP', 'ISFJ', 'ISTP', 'ISTJ'
]

# 궁합 데이터 (간소화된 로직)
def get_compatibility(mbti1, mbti2):
    # 실제로는 아주 복잡한 행렬이 들어가지만, 여기서는 핵심 로직 예시를 넣습니다.
    best_matches = {
        'INFP': ['ENFJ', 'ENTJ'],
        'ENFP': ['INFJ', 'INTJ'],
        'INFJ': ['ENFP', 'ENTP'],
        'ENFJ': ['INFP', 'ISFP'],
        # ... 여기에 더 많은 궁합을 추가할 수 있습니다.
    }
    
    if mbti2 in best_matches.get(mbti1, []):
        return "천생연분 ❤️", "서로의 부족한 점을 완벽하게 채워주는 환상의 짝꿍입니다!", 100
    elif mbti1[0] != mbti2[0] and mbti1[1:] == mbti2[1:]: # 반대되는 성향이 매력인 경우
        return "매력적인 조화 ✨", "서로 다른 점이 오히려 강한 끌림을 만들어냅니다.", 85
    else:
        return "노력이 필요한 관계 ☕", "서로의 대화 방식을 이해하려는 노력이 있다면 충분히 좋아질 수 있어요.", 60

# 메인 UI
st.title("❤️ 2025 MBTI 궁합 계산기")
st.write("우리 두 사람, 얼마나 잘 맞을까요?")

st.divider()

# 입력 섹션 (두 개의 컬럼)
col1, col2 = st.columns(2)

with col1:
    st.subheader("나의 MBTI")
    my_mbti = st.selectbox("선택하세요", mbti_list, key="mine")

with col2:
    st.subheader("상대의 MBTI")
    your_mbti = st.selectbox("선택하세요", mbti_list, key="yours")

# 결과 보기 버튼
if st.button("궁합 확인하기"):
    label, desc, score = get_compatibility(my_mbti, your_mbti)
    
    st.write("---")
    st.balloons()
    
    # 결과 출력
    st.markdown(f"""
    <div class="result-card">
        <h3>{my_mbti} ❤️ {your_mbti}</h3>
        <h1 style='color: #ff4b4b;'>{score}점</h1>
        <h2>{label}</h2>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 점수 바 시각화
    st.progress(score / 100)

# 하단 정보
st.caption("※ 본 결과는 재미로만 확인해 주세요! 모든 관계는 서로의 노력이 가장 중요합니다.")
