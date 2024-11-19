import requests 
from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO
from Section_C_input import Section_A_output, Section_D_output, Section_B_output
from Section_B_get_output import get_Section_B_output
from Section_D_Summary import summary


app = Flask(__name__)

def get_article_details(title):
    # 为了测试目的，我们直接使用提供的数据

    # # 在代码调通直接别解开这个，会耗费AI配额，不解开用的就是input.py里的数据
    Section_D_output = summary(title)
    Section_B_output = get_Section_B_output(title, title, "English")

    first_author_info_latest_three_pub = Section_D_output.get('First Author Info', {}).get('latest_three_publications', [])
    formated1 = f"\n{first_author_info_latest_three_pub[0][0]}, {first_author_info_latest_three_pub[0][1]}"
    formated2 = f"{first_author_info_latest_three_pub[1][0]}, {first_author_info_latest_three_pub[1][1]}"
    formated3 = f"{first_author_info_latest_three_pub[2][0]}, {first_author_info_latest_three_pub[2][1]}"
   

    article = {
        'title': Section_D_output.get('Title', 'N/A'),  # 从 Section_D_output 获取标题
        'author_name': ', '.join(Section_D_output.get('Authors', [])),  # 从 Section_D_output 获取作者姓名
        'summary': Section_D_output.get('Summary', 'N/A'),  # 从 Section_D_output 获取摘要
        # 'snippet': Section_A_output.get('snippet', 'N/A'),  # 从 Section_A_output 获取片段
        'pdf_link': Section_D_output.get('PDF Link', 'N/A'),  # 从 Section_D_output 获取 PDF 链接
        # 'summarized_summary': Section_D_output.get('Summarized Summary', 'N/A'),  # 从 Section_D_output 获取总结摘要
        'published': Section_D_output.get('Published', 'N/A'),  # 从 Section_D_output 获取发表日期
        'updated': Section_D_output.get('Updated', 'N/A'),  # 从 Section_D_output 获取更新日期
        # 'authors': Section_D_output.get('Authors', 'N/A'),  # 从 Section_D_output 获取作者列表
        'author_info': Section_D_output.get('First Author Info', {}),  # 从 Section_D_output 获取第一作者信息
        "first_author_info_name":(Section_D_output.get('Authors', []))[0],  # 从 Section_D_output 获取第一作者姓名
        'first_author_info_affiliation': Section_D_output.get('First Author Info', {}).get('affiliation', 'N/A'),  # 从 Section_D_output 获取第一作者机构
        'first_author_info_scholar_id': Section_D_output.get('First Author Info', {}).get('scholar_id', 'N/A'),  # 从 Section_D_output 获取第一作者 Google Scholar ID
        'first_author_info_citation': Section_D_output.get('First Author Info', {}).get('citation', 'N/A'),  # 从 Section_D_output 获取第一作者引用次数
        "first_author_info_num_publications": Section_D_output.get('First Author Info', {}).get('num_publications', 'N/A'),  # 从 Section_D_output 获取第一作者发表文章数
        'first_author_info_hindex': Section_D_output.get('First Author Info', {}).get('hindex', 'N/A'),  # 从 Section_D_output 获取第一作者 h-index
        'first_author_info_hindex5y': Section_D_output.get('First Author Info', {}).get('hindex5y', 'N/A'),  # 从 Section_D_output 获取第一作者 5 年 h-index
        'first_author_info_i10index': Section_D_output.get('First Author Info', {}).get('i10index', 'N/A'),  # 从 Section_D_output 获取第一作者 i10-index
        'first_author_info_i10index5y': Section_D_output.get('First Author Info', {}).get('i10index5y', 'N/A'),  # 从 Section_D_output 获取第一作者 5 年 i10-index

        # 从 Section_D_output 获取第一作者最新的三篇文章
        'first_author_info_latest_three1': formated1,
        'first_author_info_latest_three2': formated2,
        'first_author_info_latest_three3': formated3,

        "evaluation_from_ai": Section_D_output.get('Evaluation from AI', 'N/A'),  # 从 Section_D_output 获取 AI 评价

        "substitute_paper1_names": Section_D_output.get('Substitute paper names', 'N/A')[0],  # 从 Section_D_output 获取替代论文名称
        "substitute_paper2_names": Section_D_output.get('Substitute paper names', 'N/A')[1],  # 从 Section_D_output 获取替代论文名称
        "substitute_paper3_names": Section_D_output.get('Substitute paper names', 'N/A')[2],  # 从 Section_D_output 获取替代论文名称


        # 'journal': Section_A_output.get('journal', 'N/A'),  # 从 Section_A_output 获取期刊信息
        # 'cited_by': Section_A_output.get('cited_by', 'N/A'),  # 从 Section_A_output 获取引用次数
        'cited_by_articles': Section_B_output.get('cited_by', {}),  # 从 Section_B_output 获取前三篇引用的文章信息
        'related_work': Section_B_output.get('related_work', {}),  # 从 Section_A_output 获取相关工作
        'logical_chain': Section_B_output.get('logical_chain', 'N/A'),  # 从 Section_B_output 获取逻辑链
        'Summaries': Section_B_output.get('summaries', {'a':'b'}),  # 从 Section_B_output 获取各章节总结
        'SecB_Status': Section_B_output.get('AI_Status', 'N/A'),  # 从 Section_B_output 获取 AI 状态
        'SecB_Error': Section_B_output.get('Error', 'N/A'),  # 从 Section_B_output 获取错误信息
        # 'google_scholar_profile': Section_A_output.get('author_info', {}).get('google_scholar_profile', 'N/A'),  # 从 Section_A_output 获取 Google Scholar 个人资料
        # 'search_link': Section_A_output.get('author_info', {}).get('search_link', 'N/A')  # 从 Section_A_output 获取搜索链接
       
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
    title = request.args.get('title')
    article = get_article_details(title)
    pdf_url = article['pdf_link']
    
    # Download the PDF file from the URL
    response = requests.get(pdf_url)
    if response.status_code == 200:
        pdf_data = BytesIO(response.content)
        return send_file(pdf_data, as_attachment=True, download_name="article.pdf", mimetype='application/pdf')
    else:
        return "Failed to download PDF", 404

# 定义路由，处理 404 错误
@app.route('/<path:path>')
def catch_all(path):
    return render_template('404.html')

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=False, port=5008)  # 启动 Flask 应用，启用调试模式，设置端口为 5017