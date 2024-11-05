from article_section_summary import get_context_and_feedback_from_ai

article = {}
article['title'] = "Self-Modeling Based Diagnosis of Software-Defined Networks"

# Section B
output_dict = get_context_and_feedback_from_ai(article['title'], article['title'], translation = "English")
print("现在开始输出zzh的结果：")
output_text = output_dict['texts']
print(output_text)
output_summaries = output_dict['summaries']
print(output_summaries)
output_relatedwork = output_dict['Related work']
print(output_relatedwork)
output_logic = output_dict['Logical Chain']
print(output_logic)