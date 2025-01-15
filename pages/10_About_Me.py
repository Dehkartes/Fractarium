import streamlit as st
import requests

# FastAPI 서버 URL
FASTAPI_URL = "http://hsj3925.iptime.org:8000/ragModel/query"

# 타이틀 및 소개 섹션
st.title("허세진 챗봇 이력서 🤖")
st.markdown("""
이 챗봇은 허세진님의 이력서를 기반으로 구성되었습니다. 
아래에 질문을 입력하거나, 사이드바에서 질문 예시를 선택해보세요!
""")

# 사이드바에 질문 예시 추가
st.sidebar.markdown("""
	#### LLM 응답 가능 시간
	\t10:00-18:00
""")
st.sidebar.title("질문 예시 📋")
if st.sidebar.button("이메일 주소가 뭐에요?"):
	st.session_state["input_example"] = "이메일 주소가 뭐에요?"
if st.sidebar.button("깃허브 주소가 뭐에요?"):
	st.session_state["input_example"] = "깃허브 주소가 뭐에요?"
if st.sidebar.button("자기소개를 해주세요."):
	st.session_state["input_example"] = "자기소개를 해주세요."
if st.sidebar.button("어떤 프로젝트를 진행했나요?"):
	st.session_state["input_example"] = "지금까지 어떤 프로젝트를 진행했나요?"

# 세션 상태 초기화
if "messages" not in st.session_state:
	st.session_state.messages = []
if "input_example" not in st.session_state:
	st.session_state.input_example = ""

# 이전 대화 메시지 표시
for m in st.session_state["messages"]:
	with st.chat_message(m["role"]):
		st.markdown(m["content"])

# 질문 입력 필드
user_msg = st.chat_input("챗봇에게 질문을 입력하세요!") or st.session_state.input_example
if user_msg:
	st.session_state.input_example = ""  # 사용한 예제 초기화
	with st.chat_message("user"):
		st.markdown(user_msg)
		user_prompt = user_msg

	st.session_state.messages.append({"role": "user", "content": user_msg})

	# FastAPI 서버에 요청 보내기 (스트리밍 처리)
	with st.chat_message("assistant"):
		response = requests.post(FASTAPI_URL, json={"query": user_prompt}, stream=True)
		result = ""
		placeholder = st.empty()  # 빈 요소 생성

		if response.status_code == 200:
			for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
				if chunk:
					result += chunk
					placeholder.markdown(result)  # 동적으로 메시지 업데이트
		else:
			result = "FastAPI 서버 요청에 실패했습니다."
			placeholder.markdown(result)

	st.session_state.messages.append({"role": "assistant", "content": result})
