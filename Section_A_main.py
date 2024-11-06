import subprocess
import json
from Section_A_paper_info import get_paper_detailed_info
from Section_A_author_info import get_author_detailed_info

# 运行 Section_D_test.py 并捕获输出
result = subprocess.run(['python', 'Section_D_test.py'], capture_output=True, text=True)

# 解析输出，找到 Title 和 Authors
output_lines = result.stdout.split('\n')
title = None
first_author = None
for line in output_lines:
    if line.startswith("Title:"):
        title = line.split("Title:")[1].strip()
    elif line.startswith("Authors:"):
        authors = line.split("Authors:")[1].strip().split(', ')
        if authors:
            first_author = authors[0]
            break

def get_author_and_paper_info(title, authors):
    paper_info = {}
    if title:
        # 将 Title 作为输入传递给 paper_info.py
        print(f"Running paper_info.py with title: \"{title}\"")
        paper_info = get_paper_detailed_info(title)
        print(paper_info)
    else:
        print("Title not found in Section_D_test.py output")

    first_author = authors[0] if authors else None
    author_info = {}
    if first_author:
        # 将第一个作者的名字传递给 author_info.py
        print(f"Running author_info.py with author: \"{first_author}\"")
        author_info = get_author_detailed_info(first_author)
    else:
        print("First author not found in Section_D_test.py output")

    paper_info["author_info"] = author_info
    
    return paper_info