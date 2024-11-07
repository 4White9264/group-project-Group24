# Author: Zehao ZHANG 24069596g

import fitz  # PyMuPDF
from Section_B_arxiv_api_integration_ai_connect import answer
# 从settings.py中导入全局变量
from Section_B_settings import USER_PROMPT
import json

# 提取一页的文本
def extract_text_without_images(page):
    # 提取页面中的所有文本块
    text_blocks = page.get_text("blocks")[1:]
    text = ""
    # 记录上一个文本块的坐标
    x,y = 0,0
    for block in text_blocks: 
        # 一个问题在于，读取pdf页面的时候会先把文本块都读完再读取图片中的文本
        # 所以可以用坐标来判断下一个块是下一段文本还是图片中的文本
        if x > block[0] and y > block[1]:
            break
        #if y == block[1]:
        #    text += block[4]
        #else:
        text += block[4].replace("\n", "") + "\n"
        x = block[0]
        y = block[1]
    return text

# 提取 PDF 文本转化为txt
def pdf_to_txt(pdf_name):    
    # 打开 PDF 文件
    pdf_document = fitz.open(f'{pdf_name}.pdf')
    pdf_txt = ''
    for i in range(len(pdf_document)):
        page = pdf_document.load_page(i)
        text = extract_text_without_images(page)
        pdf_txt += text + '\n'
        
    # 过滤或处理文本
    # 去除空行
    pdf_list = pdf_txt.split('\n')
    pdf_list = [x for x in pdf_list if x != '' and x != ' ']
    pdf_txt = '\n'.join(pdf_list)

    with open(f"{pdf_name}.txt", 'w', encoding='utf-8') as txt_file:
        txt_file.write(pdf_txt)
    print(f"PDF内容已保存到 {pdf_name}.txt")

# 考虑PDF文件名和文章名不一致的情况
# 文件名可从用户上传的文件中读取，文章名由另一section提供
def get_context_and_feedback_from_ai(pdf_name, article_name, translation = "English"):
    pdf_to_txt(pdf_name)
    with open(f"{pdf_name}.txt", "r") as f:
        article_text = f.read()
    user_prompt = USER_PROMPT
    user_prompt = user_prompt.replace("{article_text}", article_text)
    user_prompt = user_prompt.replace("{article_name}", article_name)
    # print(user_prompt)
    
    output_information = answer(user_prompt, translation)
    output_dict = json.loads(output_information)
    # 按照段落标题来分割原文
    # 滑动空间？-未实现
    titles = []
    for key in output_dict['texts'].keys():
        titles.append(key)
    # print(titles)
    for title in titles:
        article_text = article_text.replace(title, "\n\n\n\n\n")
    article_text_list = article_text.split("\n\n\n\n\n")
    # print(article_text_list)
    output_dict['texts'] = dict(zip(titles, article_text_list[1:]))

    return output_dict