from article_section_summary import get_context_and_feedback_from_ai

pdf_name = 'Self-Modeling Based Diagnosis of Software-Defined Networks'
article_name = 'Self-Modeling Based Diagnosis of Software-Defined Networks'

output_dict = get_context_and_feedback_from_ai(pdf_name, article_name, translation = "English")

output_text = output_dict['texts']
print(output_text)
output_summaries = output_dict['summaries']
print(output_summaries)
output_relatedwork = output_dict['Related work']
print(output_relatedwork)
output_logic = output_dict['Logical Chain']
print(output_logic)


