import streamlit as st
import random
import os

st.set_page_config(
    page_title="중고생 AI 100% 활용법",
    page_icon="🤖",
    layout="wide"
)

# Custom Styling (모든 Streamlit 브랜드, 워터마크, 툴바, Fullscreen 완벽 제거)
st.markdown("""
<style>
    /* 1. 상단 헤더, 우측 메뉴, Deploy 버튼 완전 숨기기 */
    header, header[data-testid="stHeader"], [data-testid="stHeader"], .stAppHeader, div[data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }
    [data-testid="stToolbar"], #MainMenu, .stActionButton, button[title*="View code"], a[href*="github.com"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* 2. 하단 푸터 및 'Built with Streamlit' 워터마크 완벽 숨기기 */
    footer, [data-testid="stFooter"], .stAppFooter, div[class*="stAppFooter"], 
    div[class*="viewerBadge"], [data-testid="stAppViewerFooter"], div[class*="stAppViewerFooter"], 
    a[href*="streamlit.io"], [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0px !important;
    }

    /* 3. Fullscreen (전체 화면 버튼 및 이미지 툴바) 완벽 숨기기 */
    button[title="View fullscreen"], 
    button[title="Fullscreen"], 
    [data-testid="styledFullScreenButton"], 
    [data-testid="stElementToolbar"], 
    .stElementToolbar,
    div[data-testid="stElementToolbar"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }

    /* 4. 본문 상단 여백 보정 */
    .stAppViewContainer > .main, .main .block-container {
        padding-top: 1.5rem !important;
    }

    .main-title {
        font-size: 2.1rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.3rem;
        color: #0F172A;
    }
    .sub-title {
        font-size: 1rem;
        text-align: center;
        margin-bottom: 1.8rem;
        color: #475569;
    }
    
    /* Global Text Wrapping & Button styling */
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
    
    /* Selectbox label styling */
    div[data-testid="stSelectbox"] label p {
        font-size: 1.05rem !important;
        font-weight: 700 !important;
    }

    /* Checkbox label text truncation fix */
    div[data-testid="stCheckbox"] label, 
    div[data-testid="stCheckbox"] label p,
    div[data-testid="stCheckbox"] p,
    .stCheckbox label,
    .stCheckbox label p {
        white-space: normal !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        text-overflow: unset !important;
        line-height: 1.4 !important;
        font-size: 0.95rem !important;
    }

    /* Column Gap Tightening */
    [data-testid="column"] {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 0.5rem !important;
        align-items: center !important;
    }
    
    /* Sleek AI Title & External Link Badge */
    .ai-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1E293B !important;
        text-decoration: none !important;
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
    }
    .ai-card-title:hover {
        color: #2563EB !important;
    }
    .official-badge {
        font-size: 0.72rem;
        font-weight: 600;
        background-color: #EFF6FF;
        color: #2563EB;
        border: 1px solid #BFDBFE;
        padding: 0.15rem 0.5rem;
        border-radius: 9999px;
        letter-spacing: -0.01em;
        transition: all 0.2s ease;
    }
    .ai-card-title:hover .official-badge {
        background-color: #2563EB;
        color: #FFFFFF;
        border-color: #2563EB;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# KakaoTalk Image Mapping, Custom Image Sizes & Official URLs
# ---------------------------------------------------------
IMAGE_FILES = {
    "Gemini": "KakaoTalk_20261007_220156149_01.png",
    "ChatGPT": "KakaoTalk_20261007_220156149_02.png",
    "Claude": "KakaoTalk_20261007_220156149_03.png",
    "Canva": "KakaoTalk_20261007_220156149_04.png",
    "NotebookLM": "KakaoTalk_20261007_220156149_05.png",
    "QANDA": "KakaoTalk_20261007_220156149_06.png",
    "Gamma": "KakaoTalk_20261007_220156149_07.png",
    "ThetaWaveAI": "KakaoTalk_20261007_220156149_08.png",
    "UnivAI": "KakaoTalk_20261007_220156149_09.png",
    "Liner": "KakaoTalk_20261007_220156149_10.png",
    "Perplexity": "KakaoTalk_20261007_220156149.png"
}

IMAGE_WIDTHS = {
    "Perplexity": 90,
    "UnivAI": 95,
    "Liner": 85,
    "ThetaWaveAI": 85,
    "Gemini": 70,
    "ChatGPT": 70,
    "Claude": 70,
    "Canva": 70,
    "NotebookLM": 70,
    "QANDA": 70,
    "Gamma": 70
}

AI_URLS = {
    "Perplexity": "https://www.perplexity.ai",
    "Liner": "https://liner.ai",
    "Gemini": "https://gemini.google.com",
    "NotebookLM": "https://notebooklm.google.com",
    "ThetaWaveAI": "https://thetawave.ai",
    "UnivAI": "https://univ.ai",
    "Claude": "https://claude.ai",
    "ChatGPT": "https://chatgpt.com",
    "QANDA": "https://qanda.ai",
    "Gamma": "https://gamma.app",
    "Canva": "https://www.canva.com"
}

def render_ai_card(name, key, description):
    filename = IMAGE_FILES.get(key, "")
    img_width = IMAGE_WIDTHS.get(key, 70)
    url = AI_URLS.get(key, "#")
    
    col_img, col_txt = st.columns([1, 4], gap="small")
    
    with col_img:
        if filename and os.path.exists(filename):
            st.image(filename, width=img_width)
        else:
            st.markdown("🤖")
            
    with col_txt:
        st.markdown(
            f"<a href='{url}' target='_blank' class='ai-card-title'>"
            f"{name} <span class='official-badge'>Official ↗</span>"
            f"</a>\n\n{description}", 
            unsafe_allow_html=True
        )
    st.divider()

# ---------------------------------------------------------
# Header & Subtitle
# ---------------------------------------------------------
st.markdown("<div class='main-title'>중고생 AI 100% 활용법</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>내 과제에 맞는 AI를 추천받고, 맞춤 프롬프트까지 한 번에 완성해 보세요!</div>", unsafe_allow_html=True)

# Main Tabs
tab_main, tab_fact = st.tabs([
    "AI 추천 & 프롬프트 생성", 
    "AI 실수 찾아보기"
])

# ---------------------------------------------------------
# 1탭: 내 과제에 맞는 AI 추천 + 프롬프트 생성
# ---------------------------------------------------------
with tab_main:
    st.subheader("1. 내 과제에 맞는 AI 추천")
    st.info("과제 특성에 맞는 최적의 AI 도구를 고르면 거짓 정보(할루시네이션) 위험을 줄이고 작업 효율을 높일 수 있습니다.")
    
    task_type = st.selectbox(
        "내가 진행하려는 과제는 무엇인가요?",
        [
            "선택하세요",
            "🔍 최신 정보·뉴스·논문 출처 조사 및 보고서 검토",
            "📚 학습 자료 정리·이해 및 AI 퀴즈 생성",
            "✍️ 긴 글 분석·보고서 작문·독후감 및 논술",
            "📐 수학 문제 풀이·개념 이해 및 오답 노트",
            "🎨 PPT·카드뉴스·인포그래픽 제작",
            "🌐 영어/외국어 독해·회화·영작문 및 번역",
            "💻 코딩·프로그래밍·알고리즘 및 정보 실습"
        ],
        key="task_type_select"
    )
    
    if "🔍" in task_type:
        st.markdown("### 추천 AI 도구 목록 (이름을 클릭하면 공식 사이트로 이동합니다)")
        render_ai_card("Perplexity (퍼플렉시티)", "Perplexity", "실시간 웹 검색 연동 및 문장마다 출처(URL)를 직접 달아주어 팩트체크 수고를 90% 줄여줍니다.")
        render_ai_card("Liner AI (라이너)", "Liner", "전문 자료 조사와 학술·웹 출처 검증, 완성된 보고서/자료의 정밀 내용 검토에 특화되어 있습니다.")
        render_ai_card("Google Gemini (제미나이)", "Gemini", "구글 검색 생태계와 결합하여 최신 정보 탐색 및 이미지/문서 분석에 우수합니다.")

    elif "📚" in task_type:
        st.markdown("### 추천 AI 도구 목록 (이름을 클릭하면 공식 사이트로 이동합니다)")
        render_ai_card("NotebookLM (노트북LM)", "NotebookLM", "내 교과서, 프린트, PDF 자료를 업로드하면 깊이 있는 내용 이해, 마인드맵/시각화 자료 및 오디오 가이드를 제공합니다.")
        render_ai_card("ThetaWaveAI (세타웨이브 AI)", "ThetaWaveAI", "긴 학습 자료를 한눈에 들어오게 요약·정리하고, 시험 대비용 맞춤형 AI 퀴즈를 자동으로 생성해 줍니다.")
        render_ai_card("Univ AI (유니브 AI)", "UnivAI", "교과 및 학술 자료의 체계적 정리와 복습용 실전 퀴즈 생성으로 자기주도 학습을 돕습니다.")

    elif "✍️" in task_type:
        st.markdown("### 추천 AI 도구 목록 (이름을 클릭하면 공식 사이트로 이동합니다)")
        render_ai_card("Claude (클로드)", "Claude", "방대한 분량의 긴 글과 논문 분석, 자연스러운 보고서 작문 및 논리적 텍스트 생성에 가장 탁월합니다.")
        render_ai_card("ChatGPT (챗GPT)", "ChatGPT", "개념 요약, 아이디어 발상, 독후감 개요 작성 등 만능으로 활용하기 좋은 대표 AI입니다.")

    elif "📐" in task_type:
        st.markdown("### 추천 AI 도구 목록 (이름을 클릭하면 공식 사이트로 이동합니다)")
        render_ai_card("QANDA (콴다)", "QANDA", "수학 문제 풀이 과정 해설, 오답 원인 분석 및 단계별 문제 해결에 독보적인 수학 전문 AI입니다.")
        render_ai_card("ChatGPT (챗GPT)", "ChatGPT", "수학 공식의 원리와 논리적 풀이 절차를 친절하게 해설해 주는 학습 파트너입니다.")

    elif "🎨" in task_type:
        st.markdown("### 추천 AI 도구 목록 (이름을 클릭하면 공식 사이트로 이동합니다)")
        render_ai_card("Gamma (감마)", "Gamma", "한 줄 프롬프트나 아이디어만 입력하면 발표용 PPT 슬라이드와 전용 웹 문서를 1분 만에 디자인해 줍니다.")
        render_ai_card("Canva AI (캔바)", "Canva", "카드뉴스, 인포그래픽, 포스터 시각화 디자인 템플릿을 자동으로 완성해 줍니다.")
        render_ai_card("NotebookLM (노트북LM)", "NotebookLM", "내 학습 자료를 기반으로 인포그래픽 개요와 시각화 자료 구상을 구체화해 줍니다.")

    elif "🌐" in task_type:
        st.markdown("### 추천 AI 도구 목록 (이름을 클릭하면 공식 사이트로 이동합니다)")
        render_ai_card("Claude (클로드)", "Claude", "방대한 분량의 긴 글과 논문 분석, 자연스러운 보고서 작문 및 논리적 텍스트 생성에 가장 탁월합니다.")
        render_ai_card("ChatGPT (챗GPT)", "ChatGPT", "영어 회화 롤플레잉 연습, 문법 오류 수정, 어휘 설명에 우수한 외국어 학습 파트너입니다.")

    elif "💻" in task_type:
        st.markdown("### 추천 AI 도구 목록 (이름을 클릭하면 공식 사이트로 이동합니다)")
        render_ai_card("Claude (클로드)", "Claude", "복잡한 코드 오류(디버깅) 원인을 친절하게 설명하고 깔끔한 알고리즘 코드를 작성해 줍니다.")
        render_ai_card("ChatGPT (챗GPT)", "ChatGPT", "파이썬, HTML, C언어 등 정보 교과 실습 과제의 기초 코드 작성과 주석 해설에 유용합니다.")

    st.markdown("---")

    # 프롬프트 생성 영역
    st.subheader("2. AI 맞춤 질문(프롬프트) 생성기")
    st.info("AI에게 확실한 역할, 조건, 분량, 답변 모양을 지정해 주면 100점짜리 답변이 나옵니다.")

    col1, col2 = st.columns(2)
    with col1:
        role = st.text_input(
            "AI의 캐릭터 / 직업 (어떤 역할로 답해줄까요?)", 
            placeholder="예) 친절한 고등학교 정보 선생님", 
            key="role_input"
        )
        topic = st.text_input(
            "내가 궁금한 주제 / 과제", 
            placeholder="예) 인공지능 윤리와 저작권 문제", 
            key="topic_input"
        )
        constraint = st.text_input(
            "꼭 지켜야 할 약속 / 조건", 
            placeholder="예) 초등학생도 이해할 쉬운 단어로 핵심만 설명", 
            key="constraint_input"
        )
        
        # 확실한 정보/출처 요구 옵션 체크박스
        include_source = st.checkbox("확실하지 않은 정보 추측 방지 및 출처 요구하기", key="chk_include_source")

        length_out = st.selectbox(
            "답변 분량 / 길이 선택하기",
            [
                "상세한 설명 (보고서/발표용)",
                "보통 (1~2문단 분량)",
                "한 줄 핵심 요약"
            ],
            key="length_select"
        )

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

        role_str = role if role else "전문가"
        topic_str = topic if topic else "[질문할 주제]"
        
        constraint_base = constraint if constraint else "핵심 위주로 친절하게 설명"
        if include_source:
            constraint_str = f"{constraint_base}. 확실하지 않은 정보는 추측하지 말고, 신뢰할 수 있는 출처를 함께 제시해주세요."
        else:
            constraint_str = constraint_base

        generated_prompt = f"당신은 [{role_str}]입니다. [{topic_str}]에 대해 알려주세요.\n\n[약속/조건]: {constraint_str}\n[답변 분량]: {length_out}\n[답변 모양]: {format_out} 형태로 작성해 주세요."
        
        st.text_area("완성된 프롬프트 (복사해서 AI에 그대로 입력하세요):", generated_prompt, height=150)
        
    with col2:
        st.markdown("#### 3. 최종 제출 전 팩트체크 체크리스트")
        chk1 = st.checkbox("출처 체크 (숫자, 날짜, 인명을 포털에서 직접 대조해 보았나요?)", key="chk1")
        chk2 = st.checkbox("도구 체크 (과제 성격에 맞는 최적의 AI를 사용하였나요?)", key="chk2")
        chk3 = st.checkbox("내 글로 재구성 (AI 답변을 그대로 복사하지 않고 내 언어로 바꿨나요?)", key="chk3")
        
        if chk1 and chk2 and chk3:
            st.balloons()
            st.success("축하합니다! AI를 100% 주도적으로 컨트롤하는 스마트 AI 리터러시 마스터 과정을 완수하셨습니다!")

# ---------------------------------------------------------
# 2탭: AI 실수 찾아보기
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
    fig, fig_fact, fig_era = selected_fig

    selected_ana = random.choice(anachronisms)
    ana, ana_fact = selected_ana

    subj = random.choice(subjects)

    claim = f"{fig_era} {fig}({fig_fact})은 {subj} 중 효율성을 높이기 위해 {ana}했다."
    hint = f"팩트체크 힌트: 포털에 [{fig} 활동 시기]와 [{ana_fact}]를 각각 검색해 연도를 대조해 보세요!"
    explanation = f"거짓 적발 성공!\n{fig}의 활동 시기와 {ana_fact}의 연도는 서로 맞지 않습니다. 이처럼 AI는 연도와 문맥을 조합해 그럴듯한 거짓 정보를 만듭니다."
    
    return {
        "claim": claim,
        "hint": hint,
        "explanation": explanation
    }

with tab_fact:
    st.subheader("AI 실수 찾아보기")
    st.markdown("""
    > **자율 훈련 공간**: AI가 그럴듯하게 지어낸 가짜 사실을 **'연도 대조/검색'**만으로 적발해 보는 자율 연습실입니다. 궁금할 때 언제든 도전해 보세요!
    """)
    
    if 'current_case' not in st.session_state:
        st.session_state.current_case = generate_infinite_case()
        
    c = st.session_state.current_case
    
    if st.button("새로운 연습 문제 받기", key="btn_new_case"):
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
            st.success(c['explanation'])
            if 'solved_cases_count' not in st.session_state:
                st.session_state.solved_cases_count = 0
            if st.session_state.get('last_solved_claim') != c['claim']:
                st.session_state.solved_cases_count += 1
                st.session_state.last_solved_claim = c['claim']
                st.rerun()
            st.metric("내 누적 오류 적발 건수", f"{st.session_state.solved_cases_count}건 성공!")
        else:
            st.error("다시 검증해 보세요! 힌트를 참고하여 두 연도가 일치하는지 확인해 보세요.")
