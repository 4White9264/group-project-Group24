import requests
import json
import sys
import os
import pandas as pd
from serpapi import GoogleSearch

# 读取配置文件的函数
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config

# 获取论文信息的函数
def get_paper_info(title, config):
    params = {
        "engine": "google_scholar",
        "q": title,
        "api_key": config['SERPAPI_API_KEY']
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results

# 读取所有xlsx文件并学习内容
def read_all_xlsx_files(directory):
    data_frames = []
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):
            file_path = os.path.join(directory, file)
            df = pd.read_excel(file_path)
            data_frames.append(df)
    return data_frames

# 使用AI对期刊信息进行总结
def summarize_journal_info(journal_info, xlsx_content, config):
    OPENROUTER_API_KEY = config['OPENROUTER_API_KEY']
    YOUR_SITE = config.get('YOUR_SITE_URL', 'your_site_url_here')
    YOUR_APP_NAME = config.get('YOUR_APP_NAME', 'your_app_name_here')
    
    combined_content = f"Journal Info: {journal_info}\n\nXLSX Content:\n"
    for df in xlsx_content:
        combined_content += df.to_string(index=False) + "\n\n"
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": YOUR_SITE,  # Optional, for including your app on openrouter.ai rankings.
            "X-Title": YOUR_APP_NAME,  # Optional. Shows in rankings on openrouter.ai.
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "meta-llama/llama-3.2-1b-instruct:free",  # Optional
            "messages": [
                {
                    "role": "user",
                    "content": f"Summarize the following journal information and related xlsx content: {combined_content}"
                }
            ]
        })
    )
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        raise Exception(f"API 请求失败，状态码: {response.status_code}, 错误信息: {response.json()}")

# 示例调用
if __name__ == "__main__":
    config = read_config('config.txt')
    
    if len(sys.argv) < 2:
        print("Usage: python paper_info.py <paper_title>")
        sys.exit(1)
    
    paper_title = sys.argv[1]
    
    print(f"Retrieving information for paper: {paper_title}")
    paper_info = get_paper_info(paper_title, config)
    if paper_info:
        organic_results = paper_info.get("organic_results", [])
        if organic_results:
            for result in organic_results:
                title = result.get("title", "N/A")
                link = result.get("link", "N/A")
                snippet = result.get("snippet", "N/A")
                publication_info = result.get("publication_info", {})
                summary = publication_info.get("summary", "N/A")
                authors = publication_info.get("authors", [])
                author_info = ", ".join([author.get("name", "N/A") for author in authors])
                journal_name = summary.split('-')[-1].strip() if '-' in summary else 'N/A'
                
                print(f"Title: {title}")
                print(f"Link: {link}")
                print(f"Snippet: {snippet}")
                print(f"Summary: {summary}")
                print(f"Authors: {author_info}")
                print(f"Journal: {journal_name}")
                print("\n")
                
                # 读取所有xlsx文件并学习内容
                data_frames = read_all_xlsx_files('AI_ACADEMIC_ASSISTANT')  # 替换为实际的目录路径
                
                # 使用AI对期刊信息进行总结
                try:
                    journal_summary = summarize_journal_info(journal_name, data_frames, config)
                    print("\nJournal Summary:\n")
                    print(journal_summary)
                except Exception as e:
                    print(f"Error summarizing journal information: {e}")
        else:
            print("No organic results found.")
    else:
        print("Error retrieving paper information")