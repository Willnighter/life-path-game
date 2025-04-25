# streamlit_app.py
import streamlit as st
import random

# ----- Role definitions -----
roles = {
    "pathfinder": {
        "name": "星圖導行者 Pathfinder",
        "desc": "你以策略和遠見為燈塔，從混沌中找出前進的座標。",
        "quote": "不是因為看見才相信，而是因為相信才能看見。"
    },
    "resonant": {
        "name": "情緒引路人 Resonant",
        "desc": "你對情緒的敏銳與真誠讓你在交流中打開別人的心門。",
        "quote": "柔軟不是脆弱，是無聲的力量。"
    },
    "weaver": {
        "name": "知識縫合者 Weaver",
        "desc": "你擅長將碎片化的知識編織成洞見與創造。",
        "quote": "知識只是材料，洞察才是你鍛造現實的方式。"
    },
    "dreamer": {
        "name": "靈感旅者 Dreamer",
        "desc": "你從變動與流動中獲得靈感，活在可能性裡。",
        "quote": "不是要去哪，而是你敢去哪裡。"
    },
    "architect": {
        "name": "寂靜建築師 Architect",
        "desc": "你默默築起自己的堡壘，用堅定與清醒穩住世界。",
        "quote": "沉默不等於空白，而是一種無聲的設計語言。"
    },
    "challenger": {
        "name": "命運挑戰者 Challenger",
        "desc": "你選擇與困難同行，打破限制是你呼吸的方式。",
        "quote": "困難存在的意義，是讓你證明它沒什麼。"
    }
}

# ----- Questions and options -----
questions = [
    {
        "question": "你走進命運森林，前方有三條路，各通往不同的光影。你會？",
        "options": [
            ("選最蜿蜒的一條，看起來人煙稀少。", "architect"),
            ("走向微光處，那裡隱約傳來音樂與聲音。", "resonant"),
            ("拿出地圖與筆，嘗試記錄這些岔路與結構。", "pathfinder")
        ]
    },
    {
        "question": "你撿到一本會自動書寫的書，它正在寫下你的故事。你會？",
        "options": [
            ("翻到未來幾頁偷看結局。", "dreamer"),
            ("試圖修改內容，讓它更符合你想走的路。", "challenger"),
            ("觀察它的寫法、詞句節奏與象徵意義。", "weaver")
        ]
    },
    {
        "question": "有人走來請你幫他選一條命運之路，你會怎麼做？",
        "options": [
            ("先聽完他內心的糾結與期待。", "resonant"),
            ("詢問他過去怎麼做選擇，然後依照模式給建議。", "weaver"),
            ("我不給建議，我相信每個人都該為選擇負責。", "architect")
        ]
    },
    {
        "question": "你發現世界的規則似乎能被改寫，你會怎麼處理這個祕密？",
        "options": [
            ("立刻試圖突破它，看看邊界在哪。", "challenger"),
            ("寫成文章，紀錄給未來的旅人。", "weaver"),
            ("默默記下，留待關鍵時刻使用。", "pathfinder")
        ]
    },
    {
        "question": "你接到一個任務，期限模糊、方向自由，該怎麼展開？",
        "options": [
            ("從紀律出發，一步步建好基底。", "architect"),
            ("想像它能變成什麼，讓靈感領路。", "dreamer"),
            ("拉幾位夥伴來腦力激盪，一起冒險。", "resonant")
        ]
    },
    {
        "question": "最後，你站在一面鏡子前，看見不一樣的自己。那是一個？",
        "options": [
            ("仍在走路的人，即使風大雨大也沒停過。", "challenger"),
            ("安靜整理裝備的人，準備再次出發。", "pathfinder"),
            ("對著鏡中的自己微笑，接受一切發生的版本。", "dreamer")
        ]
    }
]

# ----- Streamlit App -----
st.set_page_config(page_title="你的人生：命運自選劇場", layout="centered")

# --- 封面畫面 ---
if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1601191905893-d270babd8c87?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title("📖 命運之書已開啟")
    st.markdown("在那尚未寫下的頁面上，你的選擇將刻下軌跡。\n每道提問都是一道門，通往不同的未來風景。\n你，是編織這部命運劇場的人。")
    if st.button("✨ 開始旅程"):
        st.session_state.start = True
        st.session_state.current_q = 0
        st.session_state.scores = {key: 0 for key in roles.keys()}
    st.stop()

# --- 問題流程 ---
st.title("🔮 你的人生：命運自選劇場")
st.markdown("在這六道選擇中，走出屬於你的一條命運分岔。\n每一題都沒有對錯，只有更靠近你的那個答案。")

if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.scores = {key: 0 for key in roles.keys()}

if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.header(f"第 {st.session_state.current_q + 1} 題")
    st.markdown(q['question'])
    for text, role in q['options']:
        if st.button(text):
            st.session_state.scores[role] += 1
            st.session_state.current_q += 1
            st.rerun()
else:
    st.subheader("🎭 你的人格角色是：")
    result = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown(f"### 🌟 {roles[result]['name']}")
    st.write(roles[result]['desc'])
    st.markdown(f"💬 *{roles[result]['quote']}*")
     # 嵌入配樂播放器
    music_links = {
        "pathfinder": "sr8bE87AlaM",
        "resonant": "3nQNiWdeH2Q",
        "weaver": "8ZtInClXe1Q",
        "dreamer": "E8E4zRzzyVM",
        "architect": "hn3wJ1_1Zsg",
        "challenger": "btm8qQUmPqY"
    }
    yt_id = music_links.get(result, None)
    if yt_id:
        st.markdown("🎧 **你的命運旋律：**")
        st.components.v1.html(f'''
            <iframe width="100%" height="166" scrolling="no" frameborder="no"
            src="https://www.youtube.com/embed/{yt_id}?autoplay=0&controls=1&loop=1">
            </iframe>
        ''', height=180)
    if st.button("🔁 再玩一次"):
        st.session_state.start = False
        st.session_state.current_q = 0
        st.session_state.scores = {key: 0 for key in roles.keys()}
        st.rerun()
