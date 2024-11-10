from Section_B_article_summary import get_context_and_feedback_from_ai
from Section_B_pdf_processing import pdf_to_txt
from Section_B_get_cited_by import get_cited_by

article = {}
article['title'] = "Self-Modeling Based Diagnosis of Software-Defined Networks"
'''
pdf_to_txt(article['title'])

# Section B
output_dict = get_context_and_feedback_from_ai(article['title'], article['title'], translation = "English")
print("/*-----------------------------------------------------------------------------*/")
print("现在开始输出zzh的结果：")
output_text = output_dict['texts']
#print(output_text)
for key in output_text.keys():
    print(key)
    print(output_text[key])
print("/*-----------------------------------------------------------------------------*/")
output_summaries = output_dict['summaries']
print(output_summaries)
print("/*-----------------------------------------------------------------------------*/")
output_relatedwork = output_dict['Related work']
print(output_relatedwork)
print("/*-----------------------------------------------------------------------------*/")
output_logic = output_dict['Logical Chain']
print(output_logic)
'''
print(get_cited_by(article['title']))