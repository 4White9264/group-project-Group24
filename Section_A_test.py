import subprocess
import json

# 运行 Section_D_test.py 并捕获输出
result = subprocess.run(['python', 'Section_D_test.py'], capture_output=True, text=True)

# 解析输出，找到 Title 和 Authors
output_lines = result.stdout.split('\n')
title = None
authors = None
for line in output_lines:
    if line.startswith("Title:"):
        title = line.split("Title:")[1].strip()
    elif line.startswith("Authors:"):
        authors = line.split("Authors:")[1].strip().split(', ')

if title:
    # 将 Title 作为输入传递给 paper_info.py
    print(f"Running paper_info.py with title: \"{title}\"")
    subprocess.run(['python', 'paper_info.py', title])
else:
    print("Title not found in Section_D_test.py output")

if authors:
    # 将每个作者的名字分别传递给 author_info.py
    for author in authors:
        print(f"Running author_info.py with author: \"{author}\"")
        subprocess.run(['python', 'author_info.py', author])
else:
    print("Authors not found in Section_D_test.py output")