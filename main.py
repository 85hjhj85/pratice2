import streamlit as st

# 페이지 설정
st.set_page_config(page_title="2025년형 MBTI 테스트", page_icon="✨", layout="centered")

# CSS를 이용한 간단한 디자인 커스텀
st.markdown("""
    <style>
    .main { text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# 질문 데이터 (실제 MBTI 문항으로 확장 가능)
questions = [
    {"q": "1. 주말에 당신의 모습은?", "options": ["친구들과 밖에서 에너지를 채운다", "집에서 혼자 침대와 물아일체가 된다"], "type": "EI"},
    {"q": "2. 당신이 더 선호하는 여행 방식은?", "options": ["지도에 모든 맛집을 찍어두는 계획형", "발길 닿는 대로 떠나는 무계획형"], "type": "JP"},
    {"q": "3. 친구가 '나 우울해서 화분 샀어'라고 한다면?", "options": ["무슨 화분 샀어? (T적 사고)", "왜 우울해? 무슨 일 있어? (F적 사고)"], "type": "TF"},
    {"q": "4. 새로운 일을 시작할 때 당신은?", "options": ["현실적인 가능성을 먼저 본다", "미래의 비전과 상상을 먼저 한다"], "type": "SN"}
]

# 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# 메인 화면 구성
st.title("✨ 2025 신년 MBTI 테스트")
st.write("---")

# 테스트 진행
if st.session_state.step < len(questions):
    current_q = questions[st.session_state.step]
    st.subheader(current_q["q"])
    
    # 선택지 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.button(current_q["options"][0]):
            st.session_state.answers.append((current_q["type"], 0))
            st.session_state.step += 1
            st.rerun()
    with col2:
        if st.button(current_q["options"][1]):
            st.session_state.answers.append((current_q["type"], 1))
            st.session_state.step += 1
            st.rerun()
            
    # 진행도 표시
    progress = st.session_state.step / len(questions)
    st.progress(progress)

# 결과 계산 및 출력
else:
    st.balloons()
    st.success("테스트 완료! 당신의 유형은...")
    
    # 결과 계산 로직
    mbti_result = ""
    scores = {"EI": 0, "SN": 0, "TF": 0, "JP": 0}
    for q_type, choice in st.session_state.answers:
        scores[q_type] += choice
    
    mbti_result += "I" if scores["EI"] > 0 else "E"
    mbti_result += "N" if scores["SN"] > 0 else "S"
    mbti_result += "F" if scores["TF"] > 0 else "T"
    mbti_result += "P" if scores["JP"] > 0 else "J"
    
    st.header(f"당신은 [ {mbti_result} ] 입니다!")
    
    # 결과별 메시지 (예시)
    mbti_desc = {
        "ENFJ": "모두를 이끄는 따뜻한 리더!",
        "ISTP": "효율을 중시하는 냉철한 기술자!",
        # ... 모든 유형 추가 가능
    }
    st.info(mbti_desc.get(mbti_result, "매력 넘치는 성격의 소유자시군요!"))
    
    if st.button("다시 하기"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
