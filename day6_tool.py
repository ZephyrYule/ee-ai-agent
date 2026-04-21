import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def measure_voltage(pin_name):
    print(f"\n[硬件中断]正在启动ADC模块,采集{pin_name}引脚电压。。。")
    if pin_name == "VCC":
        return "3.3v"
    elif pin_name == "GND":
        return "0v"
    else:
        return "1.2v(悬空未知状态)"
    
tools_list = [
        {
            "type": "function",
            "function":{
                "name": "measure_voltage",
                "description":"当用户需要测量某个引脚、测试点或芯片管脚的电压时，调用此工具",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "pin_name":{
                        "type":"string",
                        "description":"引脚名称,例如 VCC,GND,PAO等"
                        }
                       
                    }
                },
                "required": ["pin_name"]#必填参数
            }
        }
    ]


print("智能万用表Agent V1.0")
user_input = input("请下达指令：")
messages = [{"role": "user","content": user_input}]
print("正在向云端主控发送指令。。。")
response = client.chat.completions.create(
    model="qwen-plus",
    messages=messages,
    tools=tools_list
)
ai_msg = response.choices[0].message
if ai_msg.tool_calls:
    print("\n AI触发调用本地工具!")
    tool_call = ai_msg.tool_calls[0]
    func_name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    target_pin = args.get("pin_name")
    print(f"ai下发指令:请执行[{func_name}],测试参数:[{target_pin}]")
    if func_name == "measure_voltage":
        result = measure_voltage(target_pin)
        print(f"测试完成结果是:{result}")
else:
    print("\n ai 直接回答:",ai_msg.content)