import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

print("===欢迎使用EE连续对话助手===")
print("(提示:输入'退出'即可安全断电)\n")

messages = [
    {"role": "system","content": "你是一个资深的电子信息工程专家。请简短回答,像朋友一样聊天。"}
]
while True:
    user_text = input("you:")
    if user_text == "退出":
        print("系统已断电,再见！")
        break
    messages.append({"role": "user","content": user_text})

    response = client.chat.completions.create(
        model="qwen-plus",
        messages=messages,
        temperature=0.8
    )
    ai_reply = response.choices[0].message.content
    print("ai:", ai_reply,"\n")

    messages.append({"role": "assistant", "content": ai_reply})