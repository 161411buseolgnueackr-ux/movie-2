import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="무드 시네마 - 상황별 영화 추천",
    page_icon="🎬",
    layout="wide"
)

# 영화 데이터베이스 (상황별 목업 데이터)
movies_db = {
    "비 오는 날 ☔ (감성 충만)": [
        {
            "title": "어바웃 타임 (About Time)",
            "rating": "⭐ 8.8 / 10",
            "release_date": "2013-12-05",
            "genre": "로맨스 / 판타지 / 드라마",
            "plot": "성인이 되자마자 시간 여행 능력이 있다는 가문의 비밀을 알게 된 주인공의 따뜻하고 감동적인 로맨스.",
            "reviews": [
                "비 오는 날 창밖을 보며 감성에 젖고 싶을 때 최고의 선택입니다.",
                "시간의 소중함을 일깨워주는 인생 영화예요."
            ]
        },
        {
            "title": "라라랜드 (La La Land)",
            "rating": "⭐ 8.9 / 10",
            "release_date": "2016-12-07",
            "genre": "뮤지컬 / 로맨스 / 드라마",
            "plot": "재즈 피아니스트와 배우 지망생이 인생의 가장 빛나는 순간에서 만두 서로를 응원하며 펼쳐지는 이야기.",
            "reviews": [
                "음악과 영상미가 비 오는 날의 분위기와 완벽하게 어우러집니다.",
                "여운이 오래 남는 명작입니다."
            ]
        }
    ],
    "스트레스 해소 🚀 (빵 터지는 코미디)": [
        {
            "title": "극한직업",
            "rating": "⭐ 9.2 / 10",
            "release_date": "2019-01-23",
            "genre": "코미디 / 액션",
            "plot": "해체 위기의 마약반 형사들이 범죄조직 소탕을 위해 위장창업한 치킨집이 대박 맛집으로 입소문이 나면서 벌어지는 소동.",
            "reviews": [
                "아무 생각 없이 웃고 싶을 때 보면 스트레스가 싹 날아갑니다!",
                "대사가 하나하나 주옥같이 웃겨요."
            ]
        }
    ],
    "친구들과 파티 🎉 (신나는 어드벤처)": [
        {
            "title": "스파이더맨: 뉴 유니버스",
            "rating": "⭐ 9.4 / 10",
            "release_date": "2018-12-12",
            "genre": "애니메이션 / 액션 / SF",
            "plot": "여러 평행세계에서 온 스파이더맨들이 만나 세상을 구하기 위해 힘을 합치는 눈이 즐거운 액션 애니메이션.",
            "reviews": [
                "눈과 귀가 모두 즐거운 최고의 파티 영화!",
                "시각적인 연출이 정말 독창적이고 환상적입니다."
            ]
        }
    ],
    "혼자 조용히 힐링 🍵 (따뜻한 위로)": [
        {
            "title": "리틀 포레스트",
            "rating": "⭐ 9.0 / 10",
            "release_date": "2018-02-28",
            "genre": "드라마",
            "plot": "잠시 쉬어가도, 고향에 내려와 직접 농사지은 작물로 요리를 해 먹으며 사계절을 보내는 힐링 스토리.",
            "reviews": [
                "마음이 복잡할 때 보면 마음이 평온해지는 영화입니다.",
                "나만의 작은 숲을 선물받은 기분이에요."
            ]
        }
    ]
}

# 메인 타이틀
st.title("🎬 무드 시네마 (Mood Cinema)")
st.markdown("오늘의 **기분, 날씨, 상황**을 선택해 보세요. 딱 어울리는 영화와 상세한 정보를 추천해 드립니다!")

st.divider()

# 사이드바 또는 상단 셀렉트박스로 기분/상황 선택
selected_mood = st.selectbox(
    "💡 현재 나의 기분이나 상황을 선택하세요:",
    list(movies_db.keys())
)

st.header(f"✨ '{selected_mood}' 추천 영화 리스트")
st.write("")

# 선택된 상황에 맞는 영화 카드 출력
for movie in movies_db[selected_mood]:
    with st.container():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader(movie["title"])
            st.write(f"**평점:** {movie['rating']}")
            st.write(f"**개봉일:** {movie['release_date']}")
            st.write(f"**장르:** {movie['genre']}")
            
        with col2:
            st.write(f"**줄거리:** {movie['plot']}")
            st.markdown("**💬 관람객 후기:**")
            for review in movie["reviews"]:
                st.markdown(f"> *\"{review}\"*")
                
        st.divider()
