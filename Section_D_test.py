from Section_D_arxiv_api_integration import arxiv_api_calling


# 调用函数
article_title = "Noncommutative Poisson structure and invariants of matrices"
translation = "English"
# article = arxiv_api_calling(article_title, translation)

# print(article)


article = {
    "id": "http://arxiv.org/abs/2402.06909v2",
    "published": "2024-02-10",
    "updated": "2024-02-13",
    "title": "Noncommutative Poisson structure and invariants of matrices",
    "summary": (
        "We introduce a novel approach that employs techniques from noncommutative "
        "Poisson geometry to comprehend the algebra of invariants of two $n\\times n$ "
        "matrices. We entirely solve the open problem of computing the algebra of "
        "invariants of two $4 \\times 4$ matrices. As an application, we derive the "
        "complete description of the invariant commuting variety of $4 \\times 4$ "
        "matrices and the fourth Calogero-Moser space."
    ),
    "authors": ['Farkhod Eshmatov', 'Xabier García-Martínez', 'Rustam Turdibaev'],
    "pdf link": "http://arxiv.org/pdf/2402.06909v2",
    "summarized summary": (
        "The paper presents a novel approach using noncommutative Poisson geometry to study "
        "the algebra of invariants of two \\( n \\times n \\) matrices. The authors resolve "
        "the open problem of computing the algebra of invariants for two \\( 4 \\times 4 \\) "
        "matrices. As an application, they provide a full description of both the invariant "
        "commuting variety for \\( 4 \\times 4 \\) matrices and the fourth Calogero-Moser space."
    )
}

# 构建输出字符串
output = (
    f"ID: {article['id']}\n"
    f"Published: {article['published']}\n"
    f"Updated: {article['updated']}\n"
    f"Title: {article['title']}\n"
    f"Summary: {article['summary']}\n"
    f"Authors: {article['authors']}\n"
    f"PDF Link: {article.get('pdf_link', 'N/A')}\n"
    f"Summarized Summary: {article.get('summarized summary')}\n"
)

# 打印输出字符串
print(output)

# def(article):


