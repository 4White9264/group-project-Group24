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

# 从jcr.xls中获取期刊信息的函数
def get_journal_info(journal_name, file_path):
    df = pd.read_excel(file_path)
    journal_info = df[df['Journal name'].str.lower() == journal_name.lower()]
    return journal_info

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
                cited_by = result.get("inline_links", {}).get("cited_by", {}).get("total", "N/A")
                
                # 从summary中提取期刊名称
                journal_name = "N/A"
                if '-' in summary:
                    journal_name = summary.split('-')[-2].split(',')[0].strip()
                
                print(f"Title: {title}")
                print(f"Link: {link}")
                print(f"Snippet: {snippet}")
                print(f"Summary: {summary}")
                print(f"Authors: {author_info}")
                print(f"Journal: {journal_name}")
                print(f"Cited by: {cited_by}")
                
                # 从jcr.xls中获取期刊信息
                journal_info = get_journal_info(journal_name, 'jcr.xls')
                if not journal_info.empty:
                    for _, row in journal_info.iterrows():
                        jif = row['2022 JIF']
                        quartile = row['JIF Quartile']
                        category = row['Category']
                        print(f"2022 JIF: {jif}")
                        print(f"JIF Quartile: {quartile}")
                        print(f"Category: {category}")
                else:
                    print("No matching journal found in jcr.xls")
                
                print("\n")
        else:
            print("No organic results found.")
    else:
        print("Error retrieving paper information")