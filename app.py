import streamlit as st
import random

st.set_page_config(
    page_title="2026CJU 중고생 AI 100% 진짜 활용법",
    page_icon="🤖",
    layout="wide"
)

# Custom Styling (Light & Dark Mode compatible + Mobile Responsive)
st.markdown("""
<style>
    /* Responsive Title styling for Light & Dark mode */
    .main-title {
        font-size: 2rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .sub-title {
        font-size: 1rem;
        text-align: center;
        margin-bottom: 1.5rem;
        opacity: 0.85;
    }
    
    /* Bridge Box styling compatible with Light & Dark Mode */
    .bridge-box {
        background-color: rgba(37, 99, 235, 0.12);
        border-left: 5px solid #2563EB;
        padding: 1.2rem;
        border-radius: 8px;
        margin-top: 1.5rem;
    }
    .bridge-box h4 {
        color: #2563EB !important;
        margin-top: 0;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    /* Mobile-friendly text wrapping & button styling */
    .stRadio label, div[role="radiogroup"] label {
        white-space: normal !important;
        word-break: break-word !important;
        line-height: 1.5 !important;
        font-size: 1rem !important;
    }
    .stButton > button {
        white-space: normal !important;
        word-break: break-word !important;
        width: 100% !important;
    }
    div[data-testid="stMarkdownContainer"] {
        word-break: break-word !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# State Management & Progress Calculation (Top of Script)
# ---------------------------------------------------------
if 'solved_cases_count' not in st.session_state:
    st.session_state.solved_cases_count = 0

# Calculate completed stages upfront before rendering header
completed = []

# Stage 1: solved at least once
if st.session_state.get('stage1_done', False) or st.session_state.solved_cases_count > 0:
    completed.append(1)

# Stage 2: user selected a task type
if st.session_state.get('task_type_select', '선택하세요') != '선택하세요':
    completed.append(2)

# Stage 3: user checked all 3 checkboxes
if (st.session_state.get('chk1', False) and 
    st.session_state.get('chk2', False) and 
    st.session_state.get('chk3', False)):
    completed.append(3)

st.session_state.completed_stages = completed

# Header
st.markdown("<div class='main-title'>[2026CJU] 중고생을 위한 AI 100% 진짜 활용법</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>1단계(한계 진단) -> 2단계(AI 선택) -> 3단계(프롬프트)</div>", unsafe_allow_html=True)

progress_ratio = len(st.session_state.completed_stages) / 3.0
st.progress(min(progress_ratio, 1.0))
st.caption(f"전체 퀘스트 달성도: {int(min(progress_ratio, 1.0) * 100)}% ({len(st.session_state.completed_stages)}/3 단계 완료)")

tab1, tab2, tab3 = st.tabs([
    "1단계: AI 오류 찾기", 
    "2단계: 과제별 AI 선택", 
    "3단계: 프롬프트"
])

# ---------------------------------------------------------
# 무한 문제 조합 생성기
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
    selected_fig = random.choice(figures)
    if isinstance(selected_fig, (tuple, list)):
        fig = str(selected_fig[0]) if len(selected_fig) > 0 else "세종대왕"
        fig_fact = str(selected_fig[1]) if len(selected_fig) > 1 else "역사적 사건"
        fig_era = str(selected_fig[2]) if len(selected_fig) > 2 else "조선시대"
    else:
        fig, fig_fact, fig_era = str(selected_fig), "역사적 사건", "조선시대"

    selected_ana = random.choice(anachronisms)
    if isinstance(selected_ana, (tuple, list)):
        ana = str(selected_ana[0]) if len(selected_ana) > 0 else "스마트폰 사용"
        ana_fact = str(selected_ana[1]) if len(selected_ana) > 1 else "2000년대 기술"
    else:
        ana, ana_fact = str(selected_ana), "2000년대 기술"

    subj = str(random.choice(subjects))
    
    ana_fact_word = ana_fact.split()[0] if isinstance(ana_fact, str) and ana_fact.split() else str(ana_fact)

    claim = f"{fig_era} {fig}({fig_fact})은 {subj} 중 효율성을 높이기 위해 {ana}했다."
    hint = f"팩트체크 힌트: 포털에 [{fig} 활동 시기]와 [{ana_fact_word} 시기]를 각각 검색해 연도를 대조해 보세요!"
    explanation = f"거짓 적발 성공!\n{fig}의 활동 시기와 {ana_fact}의 연도는 서로 맞지 않습니다. 이처럼 AI는 연도와 문맥을 조합해 그럴듯한 거짓 정보를 만듭니다."
    
    return {
        "claim": claim,
        "hint": hint,
        "explanation": explanation
    }

# ---------------------------------------------------------
# 1단계: AI 오류 찾기
# ---------------------------------------------------------
with tab1:
    st.subheader("1단계: AI 오류 찾기")
    st.markdown("""
    > **미션 목표**: AI가 그럴듯하게 지어낸 가짜 사실을 **'배경지식 없이 연도 대조/검색'**만으로 적발하세요!
    """)
    
    if 'current_case' not in st.session_state:
        st.session_state.current_case = generate_infinite_case()
        
    c = st.session_state.current_case
    
    if st.button("새로운 문제 받기", key="btn_new_case"):
        st.session_state.current_case = generate_infinite_case()
        st.rerun()
            
    st.warning(f"AI가 작성한 문장:\n\n\"{c['claim']}\"")
    
    with st.expander("배경지식이 없는데 어떻게 검증하나요? (팩트체크 힌트)"):
        st.markdown(c['hint'])
        
    user_ans = st.radio(
        "이 AI 문장은 참일까요, 거짓일까요?",
        [
            "① 참 (실제 일어난 사실이다)", 
            "② 거짓 (AI가 연도를 조작한 거짓 정보이다)"
        ],
        index=None,
        key=f"radio_{hash(c['claim'])}"
    )
    
    if user_ans:
        if "②" in user_ans:
            st.session_state.stage1_done = True
            st.success(c['explanation'])
            
            # Increment count if not already counted for this case
            if st.session_state.get('last_solved_claim') != c['claim']:
                st.session_state.solved_cases_count += 1
                st.session_state.last_solved_claim = c['claim']
                st.rerun()
                
            st.metric("내 누적 오류 적발 건수", f"{st.session_state.solved_cases_count}건 성공!")
            
            st.markdown("""
            <div class='bridge-box'>
                <h4>1단계를 마친 당신! 다음 단계로 가볼까요?</h4>
                <p>매번 일일이 구글링해서 팩트체크하는 건 시간이 너무 오래 걸립니다.</p>
                <p>👉 <b>[2단계: 과제별 AI 선택] 탭으로 이동하여 처음부터 팩트와 출처를 잘 달아주는 AI 도구를 골라보세요!</b></p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.error("다시 검증해 보세요! 힌트를 참고하여 두 연도가 일치하는지 확인해 보세요.")

# ---------------------------------------------------------
# 2단계: 과제별 AI 선택 (Logos & All Added AIs)
# ---------------------------------------------------------
LOGOS = {
    "Claude": "https://upload.wikimedia.org/wikipedia/commons/7/70/Claude_AI_logo.svg",
    "ChatGPT": "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg",
    "Gemini": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg",
    "Perplexity": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Perplexity_AI_logo.svg",
    "Canva": "https://upload.wikimedia.org/wikipedia/commons/0/08/Canva_icon_2021.svg",
    "NotebookLM": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg",
    "QANDA": "https://qanda.ai/favicon.ico",
    "Gamma": "https://gamma.app/favicon.ico",
    "Liner": "https://getliner.com/favicon.ico"
}

with tab2:
    st.subheader("2단계: 과제별 AI 선택")
    st.info("왜 2단계가 필요한가요? 1단계처럼 매번 일일이 팩트체크하기 귀찮죠? 과제 특성에 맞는 최적의 AI를 고르면 거짓말 확률이 극적으로 낮아집니다!")
    
    task_type = st.selectbox(
        "내가 진행하려는 과제 성격은 무엇인가요?",
        [
            "선택하세요",
            "🔍 최신 정보, 뉴스, 논문 출처와 팩트 검증이 핵심인 과제",
            "✍️ 긴 글 분석, 보고서 작문, 교과서 개념 및 수학 오답 풀이 과제",
            "🎨 발표용 슬라이드(PPT), 카드뉴스, 인포그래픽 시각화 작업"
        ],
        key="task_type_select"
    )
    
    if "🔍" in task_type:
        st.markdown("### 🏆 추천 AI 도구 목록")
        
        # Perplexity
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["Perplexity"], width=45)
        with col_txt:
            st.markdown("**Perplexity (퍼플렉시티)**\n- 실시간 웹 검색 연동 및 문장마다 출처(URL)를 직접 달아주어 팩트체크 수고를 90% 줄여줍니다.")
        st.divider()
        
        # Gemini
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["Gemini"], width=45)
        with col_txt:
            st.markdown("**Google Gemini (제미나이)**\n- 구글 검색 생태계와 결합하여 최신 정보 탐색 및 이미지/문서 분석에 우수합니다.")
        st.divider()

        # Liner
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["Liner"], width=45)
        with col_txt:
            st.markdown("**Liner (라이너)**\n- 신뢰성 높은 학술 자료와 웹 정보를 하이라이팅하며 정확하게 탐색해 줍니다.")

    elif "✍️" in task_type:
        st.markdown("### 🏆 추천 AI 도구 목록")
        
        # Claude
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["Claude"], width=45)
        with col_txt:
            st.markdown("**Claude (클로드)**\n- 방대한 분량의 긴 글과 논문 분석, 자연스러운 보고서 작문 및 논리적 텍스트 생성에 가장 탁월합니다.")
        st.divider()

        # ChatGPT
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["ChatGPT"], width=45)
        with col_txt:
            st.markdown("**ChatGPT (챗GPT)**\n- 개념 요약, 아이디어 발상, 교과 내용 풀이 등 만능으로 활용하기 좋은 대표 AI입니다.")
        st.divider()

        # NotebookLM
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["NotebookLM"], width=45)
        with col_txt:
            st.markdown("**NotebookLM (노트북LM)**\n- 내 교과서나 PDF 자료만 업로드하면 거짓말 없이 정확하게 가르쳐주는 나만의 맞춤형 학습 조교입니다.")
        st.divider()

        # QANDA
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["QANDA"], width=45)
        with col_txt:
            st.markdown("**QANDA (콴다)**\n- 수학 문제 풀이, 오답 원인 분석 및 교과 개념 해설에 특화된 학습 도구입니다.")

    elif "🎨" in task_type:
        st.markdown("### 🏆 추천 AI 도구 목록")
        
        # Canva
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["Canva"], width=45)
        with col_txt:
            st.markdown("**Canva AI (캔바)**\n- 발표용 카드뉴스, 인포그래픽, 포스터 시각화 디자인 템플릿을 자동으로 완성해 줍니다.")
        st.divider()

        # Gamma
        col_img, col_txt = st.columns([1, 10])
        with col_img:
            st.image(LOGOS["Gamma"], width=45)
        with col_txt:
            st.markdown("**Gamma (감마)**\n- 한 줄 프롬프트만 입력하면 멋진 발표용 슬라이드(PPT)를 단 1분 만에 자동으로 제작해 줍니다.")

# ---------------------------------------------------------
# 3단계: 프롬프트
# ---------------------------------------------------------
with tab3:
    st.subheader("3단계: 내 맘대로 만드는 AI 프롬프트")
    st.info("왜 3단계가 필요한가요? 성의 없이 질문하면 AI도 대충 답합니다! AI에게 확실한 역할과 모양을 지정해 주면 100점짜리 답변이 나옵니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1. AI 맞춤 질문(프롬프트) 조립기")
        role = st.text_input("AI의 캐릭터 / 직업 (어떤 역할로 답해줄까요?)", "친절한 고등학교 정보 선생님", key="role_input")
        topic = st.text_input("내가 궁금한 주제/과제", "인공지능 윤리와 저작권 문제", key="topic_input")
        constraint = st.text_input("꼭 지켜야 할 약속/조건", "초등학생도 이해할 쉬운 단어로 3가지 요약", key="constraint_input")
        
        format_out = st.selectbox(
            "원하는 답변 모양 선택하기", 
            [
                "1, 2, 3 번호로 핵심만 깔끔 요약",
                "발표 대본 / 친근한 수다 말투 (~했단다, ~해요)",
                "한눈에 비교하는 정돈된 표",
                "학교 수행평가 제출용 깔끔한 줄글 설명문"
            ],
            key="format_select"
        )
        
        generated_prompt = f"당신은 [{role}]입니다. [{topic}]에 대해 알려주세요.\n\n[약속/조건]: {constraint}\n[답변 모양]: {format_out} 형태로 작성해 주세요."
        st.text_area("완성된 프롬프트 (복사해서 AI에 그대로 입력하세요):", generated_prompt, height=140)
        
    with col2:
        st.markdown("#### 2. 최종 제출 전 3단계 팩트체크 체크리스트")
        chk1 = st.checkbox("1단계: 출처 체크 (숫자, 날짜, 인명을 포털에서 직접 대조해 보았나요?)", key="chk1")
        chk2 = st.checkbox("2단계: 도구 체크 (과제 성격에 맞는 최적의 AI를 사용하였나요?)", key="chk2")
        chk3 = st.checkbox("3단계: 내 글로 재구성 (AI 답변을 그대로 복사하지 않고 내 언어로 바꿨나요?)", key="chk3")
        
        if chk1 and chk2 and chk3:
            st.balloons()
            st.success("축하합니다! AI를 100% 주도적으로 컨트롤하는 스마트 AI 리터러시 마스터 과정을 완수하셨습니다!")
