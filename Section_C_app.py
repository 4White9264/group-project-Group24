from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO
from Section_C_input import Section_A_output, Section_D_output, Section_B_output

app = Flask(__name__)

def get_article_details(title):
    # For testing purposes, we use the provided data directly
    article = {
        'title': Section_A_output.get('title', 'N/A'),
        'author_name': Section_A_output.get('author_info', {}).get('name', 'N/A'),
        'summary': Section_A_output.get('summary', 'N/A'),
        'snippet': Section_A_output.get('snippet', 'N/A'),
        'pdf_link': Section_D_output.get('pdf link', 'N/A'),
        'summarized_summary': Section_D_output.get('summarized summary', 'N/A'),
        'published': Section_D_output.get('published', 'N/A'),
        'updated': Section_D_output.get('updated', 'N/A'),
        'journal': Section_A_output.get('journal', 'N/A'),
        'cited_by': Section_A_output.get('cited_by', 'N/A'),
        'authors': Section_D_output.get('authors', []),
        'author_info': Section_A_output.get('author_info', {}),
        'related_work': Section_A_output.get('related_work', {}),
        'logical_chain': Section_B_output.get('logical_chain', 'N/A'),
        'Abstract': Section_B_output.get('summaries', {}).get('Abstract', 'N/A'),
        'google_scholar_profile': Section_A_output.get('author_info', {}).get('google_scholar_profile', 'N/A'),
        'search_link': Section_A_output.get('author_info', {}).get('search_link', 'N/A')
    }
    return article

# 定义函数，用于创建 Excel 文件
def create_excel_file(article):
    df = pd.DataFrame([article])  # 将文章字典转换为 DataFrame
    df = df.transpose()  # 转置 DataFrame
    df.reset_index(inplace=True)  # 重置索引
    df.columns = ['Heading', 'Details']  # 设置列名
    output = BytesIO()  # 创建一个 BytesIO 对象，用于保存 Excel 文件
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:  # 使用 xlsxwriter 引擎创建 Excel 文件
        df.to_excel(writer, index=False, sheet_name='Article Details')  # 将 DataFrame 写入 Excel 文件
        writer.close()  # 关闭写入器
    output.seek(0)  # 将文件指针移动到文件开头
    return output  # 返回 BytesIO 对象

# 定义路由，处理根路径请求
@app.route('/')
def index():
    return render_template('index.html')  # 渲染 index.html 模板

# 定义路由，处理 /fetch_article 路径的 POST 请求
@app.route('/fetch_article', methods=['POST'])
def fetch_article():
    title = request.form['title']  # 获取表单中的文章标题
    article = get_article_details(title)  # 获取文章详情
    return render_template('article_details.html', article=article)  # 渲染 article_details.html 模板，并传递文章详情

# 定义路由，处理 /download_excel 路径的 GET 请求
@app.route('/download_excel')
def download_excel():
    title = request.args.get('title')  # 获取请求参数中的文章标题
    article = get_article_details(title)  # 获取文章详情
    excel_file = create_excel_file(article)  # 创建 Excel 文件
    return send_file(excel_file, as_attachment=True, download_name="article_details.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  # 发送 Excel 文件给客户端

# 定义路由，处理 /download_pdf 路径的 GET 请求
@app.route('/download_pdf')
def download_pdf():
    title = request.args.get('title')  # 获取请求参数中的文章标题
    article = get_article_details(title)  # 获取文章详情
    pdf_link = article['pdf_link']  # 获取 PDF 链接
    return send_file(pdf_link, as_attachment=True, download_name="article.pdf", mimetype='application/pdf')  # 发送 PDF 文件给客户端

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True, port=5017)  # 启动 Flask 应用，启用调试模式，设置端口为 5017