import streamlit as st

st.title("퀴즈 앱")

# 객관식 퀴즈
st.subheader("1. 대한민국 수도는 어디인가요?")
q1_answer = st.radio("보기 선택:", ["부산", "서울", "대구", "인천"])
q1_correct = (q1_answer == "서울")

# 주관식 퀴즈
st.subheader("2. 사과는 영어로 무엇인가요?")
q2_answer = st.text_input("정답을 입력하세요(모두 소문자로):")
q2_correct = (q2_answer.strip().lower() == "apple")

# 결과
if st.button("제출"):
    st.write("📍 객관식 정답 여부:", "정답!" if q1_correct else "오답!")
    st.write("📍 주관식 정답 여부:", "정답!" if q2_correct else "오답!")
