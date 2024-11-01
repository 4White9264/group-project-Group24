import requests
import json
import toml
import os

# Load API key from secrets.toml
file_path = 'credentials.txt'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        secrets = toml.load(f)

OPENROUTER_API_KEY = secrets['OPENROUTER']['OPENROUTER_API_KEY']

def answer(article_summary, translation = "English"):

    # 构建对比 prompt
    system_prompt = f"""
    You are an academic assistant, please help me to analyse some articles in {translation}.
    """

    # 构建消息
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"User question: {article_summary}"},
    ]

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({ 
            "messages": messages,
            "model": "meta-llama/llama-3.1-70b-instruct:free"
        })
    )

    # 打印响应的 JSON 数据以进行调试
    print("Response JSON:", response.json())

    # 检查响应状态码
    if response.status_code != 200:
        raise Exception(f"API 请求失败，状态码: {response.status_code}, 错误信息: {response.json()}")

    # 解析响应数据
    try:
        resp = response.json()
        if 'choices' in resp and len(resp['choices']) > 0:
            content = resp['choices'][0]['message']['content']
            return content
        else:
            raise KeyError("响应中没有 'choices' 键或 'choices' 为空")
    except KeyError as e:
        raise KeyError(f"解析响应数据时出错: {e}")