from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="moonshot-v1-128k"
                       ,openai_api_key='sk-6yokLIqoeGXbMslIvoQRikIeBoRe2ysQmyeIKZ9hnz5hMTSc'
                       ,base_url = "https://api.moonshot.cn/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, 'sk-6yokLIqoeGXbMslIvoQRikIeBoRe2ysQmyeIKZ9hnz5hMTSc'))
# print(get_chat_response("我上一个问题是什么？", memory, 'sk-6yokLIqoeGXbMslIvoQRikIeBoRe2ysQmyeIKZ9hnz5hMTSc'))

# from openai import OpenAI

# client = OpenAI(
#     api_key = "api密钥",
#     base_url = "https://api.moonshot.cn/v1",
# )

# # query 为你提问的问题
# query="请问长江和嘉陵江相汇在什么地方"
# completion = client.chat.completions.create(
#     model = "moonshot-v1-128k", #支持 8k、32k、128k
#     messages = [
#         {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
#         {"role": "user", "content": query}
#     ],
#     temperature = 0.3, #值得范围从0~1；0代表输出越准确，1代表输出越灵活
# )
# output= completion.choices[0].message.content
# # output为kimi大模型回答的结果
# print(output)
