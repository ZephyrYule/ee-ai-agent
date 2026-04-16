chat_history = [
    "你好我是深圳大学的学生",
    "我想找一份实习，关于 ai agent",
    "你能帮我修改简历吗？",
]
print("用户的第一句话是：", chat_history[0])
print("用户的最新一句话是：" ,chat_history[-1])

llm_payload = {
    "model":"qwen-max",
    "temperature":0.7,
    "max_tokens":1000,
    "stream": True
}
print("当前调用模型是：", llm_payload["model"])
llm_payload["temperature"] = 0.1
print("修改后的模型温度变成了：" , llm_payload["temperature"])
print("是否开启打字机效果：" , llm_payload["stream"])
