import requests
import json
import sys
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

# 获取作者ID的函数
def get_author_id(name, config):
    params = {
        "engine": "google_scholar_profiles",
        "mauthors": name,
        "api_key": config['SERPAPI_API_KEY']
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    profiles = results.get("profiles", [])
    if profiles:
        return profiles[0].get("author_id", None)
    return None

# 获取作者详细信息的函数，包括h-index、i10-index和被引用次数
def get_author_details(author_id, config):
    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "api_key": config['SERPAPI_API_KEY']
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results

# 计算评分的函数
def calculate_scores(h_index, i10_index, total_citations):
    h_index_score = (h_index / 50) * 100 * (1/3) if h_index != "N/A" else 0
    i10_index_score = (i10_index / 150) * 100 * (1/3) if i10_index != "N/A" else 0
    total_citations_score = (total_citations / 10000) * 100 * (1/3) if total_citations != "N/A" else 0
    total_score = h_index_score + i10_index_score + total_citations_score
    return h_index_score, i10_index_score, total_citations_score, total_score

# 示例调用
if __name__ == "__main__":
    config = read_config('config.txt')
    
    if len(sys.argv) < 2:
        print("Usage: python test.py <author_name>")
        sys.exit(1)
    
    author_name = sys.argv[1]
    
    print(f"Retrieving information for author: {author_name}")
    author_id = get_author_id(author_name, config)
    if author_id:
        author_details = get_author_details(author_id, config)
        if author_details:
            interests = author_details.get("interests", [])
            cited_by = author_details.get("cited_by", {}).get("table", [])
            
            h_index = "N/A"
            i10_index = "N/A"
            total_citations = "N/A"
            
            for item in cited_by:
                if item.get("citations", {}).get("all", "N/A") != "N/A":
                    total_citations = item["citations"]["all"]
                if item.get("h_index", {}).get("all", "N/A") != "N/A":
                    h_index = item["h_index"]["all"]
                if item.get("i10_index", {}).get("all", "N/A") != "N/A":
                    i10_index = item["i10_index"]["all"]
            
            interests_formatted = ", ".join([interest.get("title", "N/A") for interest in interests])
            
            print(f"Interests: {interests_formatted}")
            print(f"h-index: {h_index}")
            print(f"i10-index: {i10_index}")
            print(f"Cited by: {total_citations}")
            
            # 计算评分
            h_index_score, i10_index_score, total_citations_score, total_score = calculate_scores(h_index, i10_index, total_citations)
            
            print(f"\nh-index Score: {h_index_score:.2f}")
            print(f"i10-index Score: {i10_index_score:.2f}")
            print(f"Total Citations Score: {total_citations_score:.2f}")
            print(f"Total Score: {total_score:.2f}")
            print("\n")
        else:
            print("Error retrieving author information")
    else:
        print("Author ID not found")