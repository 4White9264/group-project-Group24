import subprocess
import json

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

if title:
    # 将 Title 作为输入传递给 paper_info.py
    print(f"Running paper_info.py with title: \"{title}\"")
    subprocess.run(['python', 'paper_info.py', title])
else:
    print("Title not found in Section_D_test.py output")

if first_author:
    # 将第一个作者的名字传递给 author_info.py
    print(f"Running author_info.py with author: \"{first_author}\"")
    subprocess.run(['python', 'author_info.py', first_author])
else:
    print("First author not found in Section_D_test.py output")