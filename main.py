import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title("💬 尤顺AI助手")

with st.sidebar:
    openai_api_key = st.text('''尤顺是服务大众保姆，是人类健康护士，是生态环境的清洁工!
                                --董事长奚勇先生''')#这块地方可以写提示词注意事项，就不放密码了，减少使用阻碍

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的尤顺AI助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)