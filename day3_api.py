import os 
from dotenv import load_dotenv
from openai import OpenAI
 
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
print("正在呼叫通义千问大模型，请稍等...")
response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role":"system","content":"你是一个资深的电子信息工程专家，说话简明扼要。"},
        {"role":"user","content":"请用一句话解释什么是PCB(印制电路板)?"}
    ],
    temperature=0.7
)

ai_answer = response.choices[0].message.content
print("\n AI专家回答:")
print(ai_answer)#测试git
