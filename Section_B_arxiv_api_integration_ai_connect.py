import requests
import json
# 从settings.py中导入全局变量
from Section_B_settings import OPENROUTER_API_KEY, SYSTEM_PROMPT, MODEL, AI_URL

def answer(article_summary, translation = "English"):

    # 构建对比 prompt
    system_prompt = SYSTEM_PROMPT.replace("{translation}", translation)

    # 构建消息
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"User question: {article_summary}"},
    ]

    response = requests.post(
        url = AI_URL,
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({ 
            "messages": messages,
            "model": MODEL
        })
    )

    # 打印响应的 JSON 数据以进行调试
    print("Response JSON:", response.json())
    print("/*---------------------------------------------------------------*/")
    # 检查响应状态码
    if response.status_code != 200:
        raise Exception(f"API request error, status: {response.status_code}, info: {response.json()}")

    # 解析响应数据
    try:
        resp = response.json()
        if 'choices' in resp and len(resp['choices']) > 0:
            content = resp['choices'][0]['message']['content']
            return content
        else:
            raise KeyError("No key named 'choices' of the value of 'choices' is empty in Response.")
    except KeyError as e:
        raise KeyError(f"Some wrong in parsing data: {e}")