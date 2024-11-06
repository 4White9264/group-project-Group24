import requests
import json

def generate_summary(prompt):
    # 从配置文件中读取API密钥
    with open('config.txt', 'r') as file:
        config = {}
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    OPENROUTER_API_KEY = config['OPENROUTER_API_KEY']
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        raise Exception(f"API 请求失败，状态码: {response.status_code}, 错误信息: {response.json()}")

# 示例调用
if __name__ == "__main__":
    prompt = "请总结以下作者的信息：\n1. 学校：Technische Universität München\n2. 专业：计算机科学\n3. 职位：教授\n4. 研究领域：人工智能\n5. 主要的top3文章：文章1, 文章2, 文章3\n6. 谷歌个人主页链接：https://scholar.google.com/citations?user=O7qS9DkAAAAJ&hl=en"
    summary = generate_summary(prompt)
    print("Summary:", summary)