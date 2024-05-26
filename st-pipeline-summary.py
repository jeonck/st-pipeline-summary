import streamlit as st
from transformers import pipeline

# Streamlit 애플리케이션 제목
st.title("Text Summarization App")

# 사용자가 입력할 수 있는 텍스트 영역
input_text = st.text_area("Enter the text to summarize:")

# 요약 버튼
if st.button("Summarize"):
    if input_text:
        # 요약 모델 로드
        summarizer = pipeline("summarization")

        # 요약 수행
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

        # 요약 결과 출력
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")



