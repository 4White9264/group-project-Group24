from Section_B_article_summary import get_context_and_feedback_from_ai
from Section_B_get_cited_by import get_cited_by

def get_Section_B_output(pdf_name, article_name, translation = "English"):
    # 因为需要把两个模块的输出合并，故另写一个函数来完成
    output_dict_1 = get_context_and_feedback_from_ai(pdf_name, article_name, translation)
    output_dict_2 = get_cited_by(article_name)

    Section_B_output = {
        "summaries": output_dict_1.get("summaries", {}),
        "related_work": output_dict_1.get("related_work", {}),
        "logical_chain": output_dict_1.get("logical_chain", {}),
        "cited_by": {
            'cited_by_0': {
                'title': output_dict_2.get('cited_by_0', {}).get('title', 'N/A'),
                'snippet': output_dict_2.get('cited_by_0', {}).get('snippet', 'N/A')
            }, 
            'cited_by_1': {
                'title': output_dict_2.get('cited_by_1', {}).get('title', 'N/A'),
                'snippet': output_dict_2.get('cited_by_1', {}).get('snippet', 'N/A')
            },
            'cited_by_2': {
                'title': output_dict_2.get('cited_by_2', {}).get('title', 'N/A'),
                'snippet': output_dict_2.get('cited_by_2', {}).get('snippet', 'N/A')
            }
        }
    }

    return Section_B_output