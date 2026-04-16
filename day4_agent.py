import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

print("---欢迎使用EE专属硬件助手---")
user_question = input("请输入你想咨询的问题(比如电路板短路怎么排查？):")
messages = [
    {
        "role" : "system",
        "content" : "你是一个自身的电子信息工程专家。请针对用户提出的硬件问题,给出具体的排查步骤(1.2.3点)。"

    },
    {
        "role" : "user",
        "content" : user_question
    }
]
print("\n正在连接云端专家,请稍后...")
response = client.chat.completions.create(
    model="qwen-plus",
    messages=messages,
    temperature=0.8
)
ai_result = response.choices[0].message.content
print("\n"+"="*30)
print("诊断意见:")
print(ai_result)
print("="*30)
