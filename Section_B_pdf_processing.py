import fitz  # PyMuPDF
import os

# 提取 PDF 文本转化为txt
def pdf_to_txt(pdf_name): 
    if not os.path.exists(f"image/{pdf_name}"):
        os.makedirs(f"image/{pdf_name}")
    # 打开 PDF 文件
    pdf_document = fitz.open(f'{pdf_name}.pdf')
    pdf_txt = ''
    for i in range(len(pdf_document)):
        page = pdf_document.load_page(i)
        text = extract_text_and_images(page, i, pdf_name)
        pdf_txt += text + '\n'
        
    # 过滤或处理文本
    # 去除空行
    pdf_list = pdf_txt.split('\n')
    pdf_list = [x for x in pdf_list if x != '' and x != ' ']
    pdf_txt = '\n'.join(pdf_list)

    with open(f"{pdf_name}.txt", 'w', encoding='utf-8') as txt_file:
        txt_file.write(pdf_txt)
    print(f"PDF内容已保存到 {pdf_name}.txt")
    
# 提取一页
def extract_text_and_images(page, page_num, pdf_name):
    # 提取页面中的所有文本块
    # 但是去除页眉
    blocks = page.get_text("blocks")[1:]
    text = ""
    # 过滤掉空文本块
    text_blocks = [x for x in blocks if x[4] != " \n"]
    # 记录上一个文本块的坐标
    x, y = 0, 0
    x_max, y_max = 0, 0
    image_num = 1
    for i in range(len(text_blocks)): 

        # 一个问题在于，读取pdf页面的时候会先把文本块都读完再读取图片中的文本
        # 所以可以用坐标来判断下一个块是下一段文本还是图片中的文本
        if x > text_blocks[i][0] and y > text_blocks[i][1]:
            break

        # 图片截取
        # 判定方法：本文本块和上一文本块纵坐标之差大于五倍行距
        if text_blocks[i][1] - text_blocks[i-1][3] >= 5 * ( text_blocks[i][3] - text_blocks[i][1] ):
            # 认为中间有图片
            # print(text_blocks[i-1])
            rect = fitz.Rect(text_blocks[i-1][0], text_blocks[i-1][3], text_blocks[i-1][2], text_blocks[i][1])
            if is_valid_rect(rect): 
                zoom = 4  # 缩放比例，可以调整为更高的值以提高清晰度
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat, clip=rect)
                pix.save(f'image/{pdf_name}/page_{page_num + 1}_img_{image_num}.jpg')
                image_num += 1
                print(f"Image here: {text_blocks[i]}")
            else:
                print(f"Invalid rect: {text_blocks[i]}")

        # 考虑图题和图分在两页的情况
        x_max = max(x_max, text_blocks[i][2])
        y_max = max(y_max, text_blocks[i][3])
        # 确保本文本块为页内最后一个需要读取的文本块
        # 如果右下角y坐标小于页内最大y坐标，判定本页剩下的内容为图片
        if i == len(text_blocks) - 1:
            break
        if x > text_blocks[i+1][0] and y > text_blocks[i+1][1] and y_max - text_blocks[i][3] > 20:
            rect = fitz.Rect(text_blocks[i][0], text_blocks[i][3], text_blocks[i][2], y_max)
            if is_valid_rect(rect): 
                zoom = 4  # 缩放比例，可以调整为更高的值以提高清晰度
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat, clip=rect)
                pix.save(f'image/{pdf_name}/page_{page_num + 1}_img_{image_num}.jpg')
                image_num += 1
                print(f"Image here: {text_blocks[i]}")
            else:
                print(f"Invalid rect: {text_blocks[i]}")

        text += text_blocks[i][4].replace("\n", "") + "\n"
        x = text_blocks[i][0]
        y = text_blocks[i][1]
        # print("/*----------------------------------------------------------*/")
    return text

def is_valid_rect(rect):
    """检查矩形坐标是否有效"""
    return rect.x0 < rect.x1 and rect.y0 < rect.y1