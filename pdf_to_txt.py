'''
import PyPDF2

#获取 PDF 信息
pdfFile = open('Self-Modeling Based Diagnosis of Software-Defined Networks.pdf', 'rb')
pdfObj = PyPDF2.PdfReader(pdfFile)
page_count = len(pdfObj.pages)
print(page_count)

#提取文本
for p in range(0, page_count):
    text_pdfObj = pdfObj.pages[p]
    text_pdf = text_pdfObj.extract_text()
    text_list = text_pdf.split('\n')
    text_str = '\n'.join(text_list[1:])
    #print(text.extract_text())
    with open(f"output_{p}.txt", 'w', encoding='utf-8') as txt_file:
        txt_file.write(text_str)
    print("PDF内容已保存到 output.txt")
    '''

'''
import fitz  # PyMuPDF

# 打开 PDF 文件
pdf_document = fitz.open('Self-Modeling Based Diagnosis of Software-Defined Networks.pdf')
for i in range(len(pdf_document)):
    page = pdf_document.load_page(i)
    text = page.get_text()
    text_list = text.split('\n')
    filtered_text_list = list(filter(lambda x: x and x.strip(), text_list))
    text = '\n'.join(filtered_text_list[1:])

    # 过滤或处理文本
    with open(f"output_{i}.txt", 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    print(f"PDF内容已保存到 output_{i}.txt")

    '''

import fitz  # PyMuPDF

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
        text += block[4] + "\n"
        x = block[0]
        y = block[1]
    return text

def pdf_to_txt(pdf_name):    
    # 打开 PDF 文件
    pdf_document = fitz.open(f'{pdf_name}.pdf')
    pdf_txt = ''
    for i in range(len(pdf_document)):
        page = pdf_document.load_page(i)
        text = extract_text_without_images(page)
        
        '''
        text_list = text.split('\n')
        filtered_text_list = list(filter(lambda x: x and x.strip(), text_list))
        text = '\n'.join(filtered_text_list)
        '''
        pdf_txt += text + '\n'
        
        # 过滤或处理文本
    pdf_txt= pdf_txt.replace('\n\n','\n')
    with open(f"output.txt", 'w', encoding='utf-8') as txt_file:
        txt_file.write(pdf_txt)
    print(f"PDF内容已保存到 output.txt")

    
    

