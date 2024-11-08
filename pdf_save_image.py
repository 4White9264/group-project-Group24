
import fitz
import re
import os

file_path = 'Self-Modeling Based Diagnosis of Software-Defined Networks.pdf' 
# PDF 文件路径
dir_path = 'image' 
# 存放图片的文件夹

def pdf2image1(path, pic_path):
    checkIM = r"/Subtype(?= */Image)"
    pdf = fitz.open(path)
    lenXREF = pdf.xref_length()
    count = 1
    for i in range(1, lenXREF):
        text = pdf.xref_object(i)
        isImage = re.search(checkIM, text)
        if not isImage:
            continue
        pix = fitz.Pixmap(pdf, i)
        new_name = f"img_{count}.png"
        pix.save(os.path.join(pic_path, new_name))
        count += 1
        pix = None

pdf2image1(file_path, dir_path)


'''

from spire.pdf.common import *
from spire.pdf import *
 
def extract_images_from_pdf(pdf_path, output_dir):
    """
    从 PDF 文件中提取所有图片，并将其保存到指定的输出目录中。
    
    参数:
        pdf_path (str): 输入 PDF 文件的路径。
        output_dir (str): 输出图片文件的目录。
    """
    # 创建 PdfDocument 实例并加载 PDF 文件
    doc = PdfDocument()
    doc.LoadFromFile(pdf_path)
 
    # 创建 PdfImageHelper 实例
    image_helper = PdfImageHelper()
 
    image_count = 1
    # 循环遍历每个页面
    for page_index in range(doc.Pages.Count):
        page = doc.Pages[page_index]
        # 获取页面的图片信息
        image_infos = image_helper.GetImagesInfo(page)
 
        # 提取并保存图片
        for image_index in range(len(image_infos)):
            # 指定输出文件名
            output_file = os.path.join(output_dir, f"Image-{image_count}.png")
            # 将图片保存为图片文件
            image_infos[image_index].Image.Save(output_file)
            image_count += 1
 
    doc.Close()
 
# 使用示例
extract_images_from_pdf("Self-Modeling Based Diagnosis of Software-Defined Networks.pdf", "image")
'''