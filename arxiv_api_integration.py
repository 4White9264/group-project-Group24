import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
# from arxiv_api_integration_ai_connect import answer

def pdf_download(pdf_link, article_title):
    # 根据返回的PDF下载连接，下载 PDF 文件
    pdf_filename = article_title + ".pdf"
    urllib.request.urlretrieve(pdf_link, pdf_filename)

def arxiv_api_calling(article_title, translation):
    # 定义参数
    method_name = "query"
    start = 0
    max_results = 30
    search_query = urllib.parse.quote(article_title)
    
    # 构建查询URL
    url = f"http://export.arxiv.org/api/{method_name}?search_query={search_query}&start={start}&max_results={max_results}"
    
    # 发送请求并解析响应
    response = urllib.request.urlopen(url)
    xml_response = response.read()
    root = ET.fromstring(xml_response)
    
    # 处理响应
    articles = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        pdf_link = entry.find('{http://www.w3.org/2005/Atom}link[@title="pdf"]').attrib['href']
        
        print(f"Title: {title}")
        print(f"Summary: {summary}")
        print(f"PDF Link: {pdf_link}")
        
        # 下载PDF文件
        pdf_download(pdf_link, title)
        
        # 添加文章信息到列表
        articles.append({
            "title": title,
            "summary": summary,
            "pdf_link": pdf_link
        })
    
    return articles

# 示例调用
if __name__ == "__main__":
    article_title = "Deep Learning"
    translation = False
    articles = arxiv_api_calling(article_title, translation)
    for article in articles:
        print(article)