from pdf_to_txt import pdf_to_txt
from arxiv_api_integration_ai_connect import answer
import json

article_name = 'Self-Modeling Based Diagnosis of Software-Defined Networks'

pdf_to_txt(article_name)

with open("prompt.txt", "r") as f:
    user_prompt = f.read()
with open("output.txt", "r") as f:
    article_text = f.read()

user_prompt = user_prompt.replace("{article_text}", article_text)
user_prompt = user_prompt.replace("{article_name}", article_name)
#print(user_prompt)

output_information = answer(user_prompt, translation = "English")
output_dict = json.loads(output_information)
output_text = output_dict['texts']
print(output_text)
output_summaries = output_dict['summaries']
print(output_summaries)
output_relatedwork = output_dict['Related work']
print(output_relatedwork)
output_logic = output_dict['Logical Chain']
print(output_logic)

