import streamlit as st

st.set_page_config(
    page_title="AI 100% 진짜 활용법 - Self-Guided Quest",
    page_icon="🤖",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚀 중고생을 위한 AI 100% 진짜 활용법</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>선생님 없이 스스로 깨는 Self-Guided AI Pick & Check 퀘스트</p>", unsafe_allow_html=True)

if 'completed_stages' not in st.session_state:
    st.session_state.completed_stages = []

progress = len(st.session_state.completed_stages) / 4.0
st.progress(progress)
st.caption(f"🎯 전체 진행률: {int(progress * 100)}% ({len(st.session_state.completed_stages)}/4 스테이지 완료)")

tab1, tab2, tab3, tab4 = st.tabs([
    "🕵️ Stage 1: AI 오류 수사대", 
    "🎯 Stage 2: 상황별 AI Pick", 
    "⚡ Stage 3: 프롬프트 & 팩트체크", 
    "🏆 Stage 4: 마스터 인증서"
])

with tab1:
    st.subheader("🕵️ Stage 1: AI의 거짓말(할루시네이션)을 찾아라!")
    st.write("AI가 그럴듯하게 거짓말한 문장을 찾아내어 적발하세요.")
    
    q1 = st.radio(
        "Q1. 아래 AI 답변 중 '할루시네이션(거짓 정보)'이 포함된 부분은 어디일까요?",
        [
            "① 세종대왕은 조선의 4대 국왕으로 훈민정음을 창제하였다.",
            "② 세종대왕은 신하들과 집현전 학술 토론 중 분노하여 맥북 프로를 던졌다.",
            "③ 세종대왕 시대에는 측우기, 해시계 등 다양한 과학 기구가 발명되었다."
        ],
        index=None
    )
    
    if q1:
        if "②" in q1:
            st.success("🎉 정답입니다! 조선시대에는 맥북이 없었습니다.")
            if 1 not in st.session_state.completed_stages:
                st.session_state.completed_stages.append(1)
                st.rerun()
        else:
            st.error("❌ 다시 생각해보세요! 시기와 도구를 살펴보세요.")

with tab2:
    st.subheader("🎯 Stage 2: 과제 특성별 최적의 AI 골라쓰기")
    task_type = st.selectbox(
        "내가 해야 할 과제 유형은?",
        [
            "선택하세요",
            "🔍 최신 뉴스, 실시간 검색, 학술 출처 확인이 필요할 때",
            "✍️ 교과 개념 요약, 논리적 글쓰기, 수학 오답 원인 분석이 필요할 때",
            "🎨 발표 PPT, 카드뉴스, 인포그래픽 시각화 자료가 필요할 때"
        ]
    )
    
    if "🔍" in task_type:
        st.markdown("### 🏆 추천 AI: **Perplexity / Gemini**\n- **강점**: 실시간 웹 검색 연동, 정확한 출처 링크 제공")
        if 2 not in st.session_state.completed_stages: st.session_state.completed_stages.append(2)
    elif "✍️" in task_type:
        st.markdown("### 🏆 추천 AI: **ChatGPT / Claude**\n- **강점**: 긴 문맥 이해력 우수, 심도 있는 논리 구조 설계 가능")
        if 2 not in st.session_state.completed_stages: st.session_state.completed_stages.append(2)
    elif "🎨" in task_type:
        st.markdown("### 🏆 추천 AI: **Canva AI**\n- **강점**: 텍스트 입력만으로 발표용 레이아웃 자동 생성")
        if 2 not in st.session_state.completed_stages: st.session_state.completed_stages.append(2)

with tab3:
    st.subheader("⚡ Stage 3: 프롬프트 3법칙 & 3단계 팩트체크")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1️⃣ 프롬프트 3법칙 자동 생성기")
        role = st.text_input("역할 (Role)", "고등학교 역사 선생님")
        topic = st.text_input("주제/상황", "임진왜란의 주요 원인")
        constraint = st.text_input("제약조건 (Constraint)", "어려운 한자어는 빼고 3줄로 작성")
        format_out = st.selectbox("출력형식 (Format)", ["불릿 포인트", "표 형식", "대화체"])
        
        generated_prompt = f"당신은 [{role}]입니다. [{topic}]에 대해 설명해 주세요. 조건: [{constraint}]. 답변은 [{format_out}]으로 출력해 주세요."
        st.text_area("완성된 프롬프트 (복사해서 AI에 입력하세요):", generated_prompt, height=100)
        
    with col2:
        st.markdown("#### 2️⃣ 3단계 팩트체크 셀프 스위치")
        chk1 = st.checkbox("1단계: 출처 명확성 (숫자, 날짜, 인명 교과서 대조 완료)")
        chk2 = st.checkbox("2단계: 최근 데이터 일치성 (최신 정보 확인 완료)")
        chk3 = st.checkbox("3단계: 윤리성 및 저작권 (내 언어로 재구성 완료)")
        
        if chk1 and chk2 and chk3:
            st.success("✅ 3단계 팩트체크 완료!")
            if 3 not in st.session_state.completed_stages:
                st.session_state.completed_stages.append(3)

with tab4:
    st.subheader("🏆 Stage 4: AI 리터러시 마스터 인증서 발급")
    if len(st.session_state.completed_stages) >= 3:
        user_name = st.text_input("학생 이름을 입력하세요:", "홍길동")
        school_name = st.text_input("학교명을 입력하세요:", "OO중학교")
        
        if st.button("🎓 인증서 발급하기"):
            st.balloons()
            st.markdown(f"""
            <div style='border: 8px solid #2563EB; padding: 2rem; border-radius: 16px; text-align: center; background-color: #FFFFFF;'>
                <h1 style='color: #1E3A8A;'>📜 AI 100% 스마트 리터러시 마스터 증서</h1>
                <p style='font-size: 1.2rem;'><b>성명:</b> {user_name} ({school_name})</p>
                <hr>
                <p>위 학생은 <b>2026 AI Teach-Up Self-Guided 퀘스트</b>를 성실히 이수하여,<br>
                상황별 AI 선택(Pick) 및 비판적 팩트체크(Check) 역량을 갖추었음을 인증합니다.</p>
            </div>
            """, unsafe_allow_html=True)
            if 4 not in st.session_state.completed_stages:
                st.session_state.completed_stages.append(4)
    else:
        st.warning("⚠️ Stage 1~3 미션을 먼저 수행해야 마스터 인증서를 발급받을 수 있습니다!")
