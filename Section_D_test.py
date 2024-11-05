from Section_D_arxiv_api_integration import arxiv_api_calling


# 调用函数
article_title = "Self-Modeling Based Diagnosis of Software-Defined Networks"
translation = "English"
article = arxiv_api_calling(article_title, translation)

# 打印文章信息
print(f"ID: {article['id']}")
print(f"Published: {article['published']}")
print(f"Updated: {article['updated']}")
print(f"Title: {article['title']}")
print(f"Summary: {article['summary']}")
print(f"Authors: {', '.join(article['authors'])}")
print(f"PDF Link: {article.get('pdf_link', 'N/A')}\n")
print(f"Summarized Summary: {article.get('summarized summary')}\n")