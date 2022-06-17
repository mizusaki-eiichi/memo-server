import json
import os
import requests

import streamlit as st


SERVER_HOST: str = os.getenv("SERVER_HOST", default="localhost")
SERVER_PORT: int = os.getenv("SERVER_PORT", default=8000)

URI: str = f"http://{SERVER_HOST}:{SERVER_PORT}"


def main():
    page = st.sidebar.selectbox("Choose your page", ["registration", "list"])
    titles = ["メモ登録画面", "メモ一覧画面"]

    if page == "registration":
        st.title(titles[0])

        with st.form(key="registration"):
            content: str = st.text_input("メモ内容", max_chars=100)
            data = {"content": content}
            submit_button = st.form_submit_button(label="メモ登録")

            if submit_button:
                url = f"{URI}/create_memos"
                res = requests.post(url,data=json.dumps(data))
                if res.status_code == 200:
                    st.success("メモ登録完了")
                    st.json(res.json())
                else:
                    st.error("エラー")

    else:
        st.title(titles[1])
        res = requests.get(f"{URI}/read_memos")
        records = res.json()

        for record in records:
            st.subheader(f'★{record.get("content")}')


if __name__ == "__main__":
    main()
