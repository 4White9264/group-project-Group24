# 谷歌学术接口
serpapi_key = "87e734f6134fcb72e3c2f4f9f3e0a2aa9435e0903ce9a205d8d7e9024abb05a0"
engine = "google_scholar"

# AI接口调用
OPENROUTER_API_KEY = "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"
MODEL = "openai/gpt-4o-mini-2024-07-18"
AI_URL = "https://openrouter.ai/api/v1/chat/completions"
SYSTEM_PROMPT = """
You are an academic assistant, please help me to analyse some articles in {translation}.
"""
USER_PROMPT = """
The article is:
"{article_text}"

What you need to do is analyzing the article, and output the following Information:
1. Chapters' title: Get each chapter's title of this article. The Chapters should include the abstract.
2. Chapters' summaries: Get each chapter's summary of this article;
3. Related work: The summary of this article's related work;
4. Logic Chain: Explain the argumentation process of this article in one paragraph.

Output in JSON format without ```json.
Example:
{ 
    "summaries":{
        "chapter1's title": "chapter1's summary",
        "chapter2's title": "chapter1's summary",
        ......
    },
    "related_work":{
        "{article_name}": "The summary of this article's related work."
    },
    "logical_chain": "The overall logic of this article."
}
"""