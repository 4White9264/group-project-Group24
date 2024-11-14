from Section_B_get_output import get_Section_B_output
from Section_B_article_summary import get_context_and_feedback_from_ai
from Section_B_get_cited_by import get_cited_by
from Section_B_pdf_processing import pdf_to_txt

output = get_Section_B_output("Self-Modeling Based Diagnosis of Software-Defined Networks","Self-Modeling Based Diagnosis of Software-Defined Networks").get("summaries")

# output = get_context_and_feedback_from_ai("Self-Modeling Based Diagnosis of Software-Defined Networks","Self-Modeling Based Diagnosis of Software-Defined Networks")

# output = get_cited_by("Self-Modeling Based Diagnosis of Software-Defined Networks")

# pdf_to_txt("Self-Modeling Based Diagnosis of Software-Defined Networks")

print(output)