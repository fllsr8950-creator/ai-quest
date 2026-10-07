import streamlit as st
import random

st.set_page_config(
    page_title="AI 100% 진짜 활용법 - Self-Guided Quest",
    page_icon="🤖",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚀 중고생을 위한 AI 100% 진짜 활용법</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>선생님 없이 스스로 깨는 Self-Guided AI Pick & Check 퀘스트</p>", unsafe_allow_html=True)

if 'completed_stages' not in st.session_state:
    st.session_state.completed_stages = []

progress = len(st.session_state.completed_stages) / 3.0
st.progress(min(progress, 1.0))
st.caption(f"🎯 전체 진행률: {int(min(progress, 1.0) * 100)}% ({len(st.session_state.completed_stages)}/3 스테이지 완료)")

tab1, tab2, tab3 = st.tabs([
    "🕵️ Stage 1: AI 오류 수사대", 
    "🎯 Stage 2: 상황별 AI Pick", 
    "⚡ Stage 3: 프롬프트 & 팩트체크"
])

# Stage 1 문제 데이터베이스 (배경지식 없이 검색으로 팩트체크하는 문제들)
questions_db = [
    {
        "id": 1,
        "title": "🔍 사건 #1: 우주비행사의 셀카?",
        "ai_claim": "1969년 아폴로 11호 달 착륙 성공 당시, 우주비행사 암스트롱은 스마트폰으로 지구에 실시간 셀카 사진을 전송했다.",
        "options": [
            "① 참 (실제로 일어난 일이다)",
            "② 거짓 (스마트폰 연도와 달 착륙 연도가 맞지 않는 할루시네이션이다)"
        ],
        "answer_index": 1,
        "hint": "💡 **배경지식 없이 검증하기 (검색 팁)**\n포털창에 `[아폴로 11호 연도(1969)]`와 `[스마트폰 개발 연도]`를 각각 검색해서 연도를 대조해 보세요!",
        "explanation": "🎉 **정답입니다! (거짓 적발 성공)**\n세계 최초의 스마트폰(IBM 사이먼)은 1992년에 나왔습니다. 배경지식이 없어도 **'두 연도 검색 대조(Timeline Check)'**로 10초 만에 AI 거짓말을 적발할 수 있습니다!"
    },
    {
        "id": 2,
        "title": "🔍 사건 #2: 조선시대 독도 스쿠버 다이빙?",
        "ai_claim": "조선시대 안용복은 조선왕조실록 기록에 따라 자폐식 스쿠버 다이빙 장비를 직접 제작하여 독도 바닷속을 탐사했다.",
        "options": [
            "① 참 (조선시대 기술로 다이빙 장비를 만들어 탐사했다)",
            "② 거짓 (안용복의 활동 시기와 스쿠버 다이빙 장비 발명 시기가 맞지 않는다)"
        ],
        "answer_index": 1,
        "hint": "💡 **배경지식 없이 검증하기 (검색 팁)**\n포털창에 `[안용복 활동 시기(17세기)]`와 `[스쿠버 다이빙 장비 발명 연도(20세기)]`를 검색해서 대조해 보세요!",
        "explanation": "🎉 **정답입니다! (거짓 적발 성공)**\n현대적 스쿠버 장비(Aqua-Lung)는 1943년 프랑스에서 발명되었습니다. **'인물 시기 vs 장비 발명 연도 대조'**로 가짜 뉴스임을 즉시 검증할 수 있습니다!"
    },
    {
        "id": 3,
        "title": "🔍 사건 #3: 대한민국 청소년 수면 보장법?",
        "ai_claim": "2023년 대한민국 국회에서는 중고등학생의 매일 8시간 수면을 법적으로 의무화하는 '청소년 수면 보장법'이 만장일치로 통과되어 시행 중이다.",
        "options": [
            "① 참 (실제로 통과되어 시행 중인 법률이다)",
            "② 거짓 (실제 존재하지 않는 법안이며 AI가 지어낸 지어냄 현상이다)"
        ],
        "answer_index": 1,
        "hint": "💡 **배경지식 없이 검증하기 (검색 팁)**\n포털 뉴스 탭에 `\"청소년 수면 보장법\" 만장일치`를 따옴표 검색해 보세요. 실제 뉴스 기사가 나오나요?",
        "explanation": "🎉 **정답입니다! (거짓 적발 성공)**\n포털 뉴스 검색 결과가 0건입니다! 실제로 존재하지 않는 법안을 AI가 그럴듯하게 지어낸 경우, **'키워드 포털 교차 검색(Cross-Search)'**으로 100% 가려낼 수 있습니다."
    },
    {
        "id": 4,
        "title": "🔍 사건 #4: 메밀꽃 필 무렵의 인스타그램 연재?",
        "ai_claim": "소설가 이효석은 1936년 발표한 단편소설 <메밀꽃 필 무렵>을 인스타그램에 매주 연재하여 당시 청년들의 대대적인 호응을 얻었다.",
        "options": [
            "① 참 (당시 소설가가 SNS를 적극 활용했다)",
            "② 거짓 (소설 발표 연도와 SNS 서비스 시기가 맞지 않는 가짜 사실이다)"
        ],
        "answer_index": 1,
        "hint": "💡 **배경지식 없이 검증하기 (검색 팁)**\n`[메밀꽃 필 무렵(1936년)]`과 `[인스타그램 출시 연도(2010년)]`를 비교해 보세요!",
        "explanation": "🎉 **정답입니다! (거짓 적발 성공)**\n1936년 일제강점기에는 인터넷과 인스타그램이 없었습니다! **'서비스 연도 교차 검증'**으로 오류를 쉽게 잡아낼 수 있습니다."
    }
]

with tab1:
    st.subheader("🕵️ Stage 1: AI 오류 수사대 (배경지식 없이 팩트체크하기)")
    st.info("💡 **핵심 노하우**: 배경지식이 없어도 **'연도 대조'**나 **'포털 키워드 검색'**을 활용하면 AI의 거짓말(할루시네이션)을 100% 적발할 수 있습니다!")
    
    if 'q_idx' not in st.session_state:
        st.session_state.q_idx = random.randint(0, len(questions_db) - 1)
        
    if st.button("🎲 다른 문제 랜덤 뽑기"):
        st.session_state.q_idx = random.randint(0, len(questions_db) - 1)
        st.rerun()
            
    current_q = questions_db[st.session_state.q_idx]
    
    st.markdown(f"### {current_q['title']}")
    st.warning(f"🤖 **AI의 주장**: \"{current_q['ai_claim']}\"")
    
    with st.expander("🔍 배경지식이 없는데 어떻게 검증하나요? (팩트체크 힌트 보기)"):
        st.markdown(current_q['hint'])
        
    user_choice = st.radio(
        "이 AI 답변은 참일까요, 거짓일까요?",
        current_q['options'],
        key=f"q_radio_{current_q['id']}",
        index=None
    )
    
    if user_choice:
        if current_q['options'].index(user_choice) == current_q['answer_index']:
            st.success(current_q['explanation'])
            if 1 not in st.session_state.completed_stages:
                st.session_state.completed_stages.append(1)
        else:
            st.error("❌ 다시 생각해보세요! 위의 [팩트체크 힌트]를 참고해 검색해보세요.")

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
            st.success("🎉 축하합니다! 3단계 팩트체크 및 모든 퀘스트를 완수하셨습니다!")
            if 3 not in st.session_state.completed_stages:
                st.session_state.completed_stages.append(3)
