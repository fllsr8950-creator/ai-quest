import streamlit as st
import random

st.set_page_config(
    page_title="AI 100% 진짜 활용법 - Self-Guided Quest",
    page_icon="🤖",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #1E3A8A; text-align: center; margin-bottom: 0.3rem; }
    .sub-title { font-size: 1.05rem; color: #4B5563; text-align: center; margin-bottom: 1.5rem; }
    .bridge-box { background-color: #EFF6FF; border-left: 5px solid #2563EB; padding: 1.2rem; border-radius: 8px; margin-top: 1.5rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 중고생을 위한 AI 100% 진짜 활용법</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Stage 1(한계 진단) ➔ Stage 2(AI 선택) ➔ Stage 3(프롬프트 & 검증) 3단계 클리어 퀘스트</div>", unsafe_allow_html=True)

if 'completed_stages' not in st.session_state:
    st.session_state.completed_stages = []
if 'solved_cases_count' not in st.session_state:
    st.session_state.solved_cases_count = 0

progress = len(st.session_state.completed_stages) / 3.0
st.progress(min(progress, 1.0))
st.caption(f"🎯 전체 퀘스트 달성도: {int(min(progress, 1.0) * 100)}% ({len(st.session_state.completed_stages)}/3 단계 완료)")

tab1, tab2, tab3 = st.tabs([
    "🕵️ Stage 1: AI 오류 수사대 (한계 체감)", 
    "🎯 Stage 2: 과제별 AI Pick (도구 선택)", 
    "⚡ Stage 3: 프롬프트 & 팩트체크 (실전 기술)"
])

# ---------------------------------------------------------
# 무한 사건 조합 생성기 (Endless Random Case Generator)
# ---------------------------------------------------------
figures = [
    ("세종대왕", "1446년 훈민정음 반포", "조선 시대"),
    ("이순신 장군", "1592년 한산도 대첩", "조선 임진왜란"),
    ("아인슈타인", "1905년 상대성 이론 발표", "20세기 초"),
    ("레오나르도 다빈치", "1503년 모나리자 제작", "르네상스 시대"),
    ("김구 선생", "1919년 대한민국 임시정부 수립", "일제강점기"),
    ("갈릴레오 갈릴레이", "1610년 망원경 천체 관측", "17세기"),
    ("정약용 선생", "1796년 수원화성 거중기 사용", "조선 후기")
]

anachronisms = [
    ("인스타그램 라이브 방송으로 소통", "2010년 인스타그램 출시"),
    ("스마트폰으로 지구와 실시간 메시지 전송", "1992년 최초 스마트폰 등장"),
    ("맥북 프로 M3 노트북을 사용해 수치를 계산", "2006년 맥북 시리즈 첫 출시"),
    ("테슬라 자율주행 전기차를 타고 현장 이동", "2008년 테슬라 첫 전기차 출현"),
    ("에어팟 프로 노이즈 캔슬링을 끼고 집중력 향상", "2019년 에어팟 프로 출시"),
    ("유튜브 쇼츠 챌린지 영상을 올려 인기 획득", "2005년 유튜브 서비스 개시"),
    ("ChatGPT에 질문하여 서류 양식 작성", "2022년 ChatGPT 출시")
]

subjects = [
    "학술 토론", "전쟁 전략 회의", "과학 연구 발표", "작품 구상 과정", "독립 운동 비밀 모임", "국정 현안 회의"
]

def generate_infinite_case():
    fig, fig_fact, fig_era = random.choice(figures)
    ana, ana_fact = random.choice(anachronisms)
    subj = random.choice(subjects)
    
    claim = f"{fig_era} {fig}({fig_fact})은 {subj} 중 효율성을 높이기 위해 {ana}했다."
    hint = f"💡 **팩트체크 힌트**: 포털에 `[{fig} 활동 시기]`와 `[{ana_fact.split()[0]} 시기]`를 각각 검색해 연도를 대조해 보세요!"
    explanation = f"🎉 **거짓 적발 성공!**\n{fig}의 활동 시기와 {ana_fact}의 연도는 서로 맞지 않습니다. 이처럼 AI는 연도와 문맥을 조합해 그럴듯한 가짜 사실을 만듭니다."
    
    return {
        "claim": claim,
        "hint": hint,
        "explanation": explanation
    }

# ---------------------------------------------------------
# STAGE 1: AI 오류 수사대
# ---------------------------------------------------------
with tab1:
    st.subheader("🕵️ Stage 1: AI 오류 수사대 (무한 라이브 사건 파일)")
    st.markdown("""
    > **미션 목표**: AI가 그럴듯하게 지어낸 가짜 사실(할루시네이션)을 **'배경지식 없이 연도 대조/검색'**만으로 적발하세요!
    """)
    
    if 'current_case' not in st.session_state:
        st.session_state.current_case = generate_infinite_case()
        
    col_a, col_b = st.columns([3, 1])
    with col_b:
        if st.button("🎲 새로운 사건 받기 (무한)"):
            st.session_state.current_case = generate_infinite_case()
            st.rerun()
            
    c = st.session_state.current_case
    
    st.warning(f"🤖 **AI가 생성한 사건 보고서**: \"{c['claim']}\"")
    
    with st.expander("🔍 배경지식 없이 검증하는 법 (팩트체크 힌트)"):
        st.markdown(c['hint'])
        
    user_ans = st.radio(
        "이 AI 보고서는 참일까요, 거짓일까요?",
        ["① 참 (실제 일어난 사실이다)", "② 거짓 (AI가 연도를 조작한 할루시네이션이다)"],
        index=None,
        key=f"radio_{hash(c['claim'])}"
    )
    
    if user_ans:
        if "②" in user_ans:
            st.success(c['explanation'])
            if 1 not in st.session_state.completed_stages:
                st.session_state.completed_stages.append(1)
            st.session_state.solved_cases_count += 1
            st.metric("🕵️ 내 누적 오류 적발 건수", f"{st.session_state.solved_cases_count}건 성공!")
            
            # --- STAGE 2로 넘어가는 명확한 이유 (Narrative Bridge) ---
            st.markdown("""
            <div class='bridge-box'>
                <h4>💡 1단계를 마친 당신! 하지만 여기서 끝일까요?</h4>
                <p><b>"AI 오류를 다 찾을 수 있는데, 2~3단계는 왜 가야 하죠?"</b></p>
                <ul>
                    <li><b>문제점</b>: AI 답변을 매번 일일이 구글에 검색하고 연도 대조하는 건 <b>시간이 너무 오래 걸리고 피곤합니다!</b></li>
                    <li><b>해결책 (Stage 2)</b>: 처음부터 검색 기반 AI(Perplexity/Gemini)를 고르면 일일이 팩트체크하는 수고가 90% 줄어듭니다.</li>
                    <li><b>해결책 (Stage 3)</b>: AI에게 정교한 질문(프롬프트)을 던지면 처음부터 오류 없는 정확한 답을 뽑아낼 수 있습니다.</li>
                </ul>
                <p>👉 <b>지금 상단 [Stage 2: 과제별 AI Pick] 탭으로 이동하여 시간을 10배 아끼는 AI 도구를 골라보세요!</b></p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.error("❌ 다시 검증해 보세요! 힌트를 참고하여 두 연도가 일치하는지 확인해 보세요.")

# ---------------------------------------------------------
# STAGE 2: 과제별 AI Pick
# ---------------------------------------------------------
with tab2:
    st.subheader("🎯 Stage 2: 상황별 AI 골라쓰기 (시간 절약 10배 전략)")
    st.info("💡 **왜 Stage 2가 필요한가요?** 1단계처럼 매번 일일이 팩트체크하기 귀찮죠? 과제 특성에 맞는 최적의 AI를 고르면 거짓말 확률이 극적으로 낮아집니다!")
    
    task_type = st.selectbox(
        "내가 진행하려는 과제 성격은 무엇인가요?",
        [
            "선택하세요",
            "🔍 최신 정보, 뉴스, 논문 출처와 팩트 검증이 핵심인 과제",
            "✍️ 수식이 들어간 수학 오답 분석, 교과서 개념 요약 및 논리적 보고서",
            "🎨 발표용 슬라이드, 카드뉴스, 인포그래픽 시각화 작업"
        ]
    )
    
    if "🔍" in task_type:
        st.markdown("""
        ### 🏆 추천 AI: **Perplexity / Gemini**
        - **선택 이유**: 실시간 웹 검색 연동 및 각 문장마다 출처(URL)를 직접 달아주므로, 1단계처럼 수동 검색할 필요 없이 출처 클릭 한 번으로 검증 끝!
        """)
        if 2 not in st.session_state.completed_stages: st.session_state.completed_stages.append(2)
    elif "✍️" in task_type:
        st.markdown("""
        ### 🏆 추천 AI: **ChatGPT / Claude**
        - **선택 이유**: 긴 문맥 이해와 논리적 추론 능력이 뛰어납니다. 개념을 쉽게 풀어서 설명하거나 보고서 개요를 잡을 때 가장 우수합니다.
        """)
        if 2 not in st.session_state.completed_stages: st.session_state.completed_stages.append(2)
    elif "🎨" in task_type:
        st.markdown("""
        ### 🏆 추천 AI: **Canva AI**
        - **선택 이유**: 단순 글자가 아니라 인포그래픽, 카드뉴스 등 시각적 디자인 템플릿을 자동으로 배치해 주어 발표 자료 제작 시간을 단축합니다.
        """)
        if 2 not in st.session_state.completed_stages: st.session_state.completed_stages.append(2)

# ---------------------------------------------------------
# STAGE 3: 프롬프트 & 팩트체크
# ---------------------------------------------------------
with tab3:
    st.subheader("⚡ Stage 3: 프롬프트 3법칙 & 최종 팩트체크 스위치")
    st.info("💡 **왜 Stage 3가 필요한가요?** 나쁜 질문을 던지면 똑똑한 AI도 거짓말을 합니다. 정교한 프롬프트로 100% 원하는 답변을 한 번에 뽑아내세요!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1️⃣ 프롬프트 3법칙 자동 조합기")
        role = st.text_input("역할 (Role)", "고등학교 정보 선생님")
        topic = st.text_input("주제/과제", "인공지능 윤리와 저작권 문제")
        constraint = st.text_input("제약조건 (Constraint)", "어려운 용어 없이 3개 요약, 출처 명시")
        format_out = st.selectbox("출력형식 (Format)", ["불릿 포인트", "표 형식", "대화체"])
        
        generated_prompt = f"당신은 [{role}]입니다. [{topic}]에 대해 작성해 주세요.\n[제약조건]: {constraint}\n[출력형식]: {format_out}로 작성해 주세요."
        st.text_area("완성된 100% 프롬프트 (복사해서 AI에 입력하세요):", generated_prompt, height=120)
        
    with col2:
        st.markdown("#### 2️⃣ 최종 제출 전 3단계 팩트체크 스위치")
        chk1 = st.checkbox("1단계: 출처 명확성 (숫자, 인명, 연도 클릭 확인 완료)")
        chk2 = st.checkbox("2단계: 단일 AI 의존 탈피 (상황별 최적 AI 활용 완료)")
        chk3 = st.checkbox("3단계: 윤리적 재구성 (베끼지 않고 내 언어로 재작성 완료)")
        
        if chk1 and chk2 and chk3:
            st.balloons()
            st.success("🎉 축하합니다! AI를 100% 주도적으로 컨트롤하는 스마트 AI 리터러시 마스터 과정을 완수하셨습니다!")
            if 3 not in st.session_state.completed_stages:
                st.session_state.completed_stages.append(3)
