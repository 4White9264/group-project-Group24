from Section_B_article_summary import get_context_and_feedback_from_ai
from Section_B_get_cited_by import get_cited_by

def get_Section_B_output(pdf_name, article_name, translation = "English"):
    # 因为需要把两个模块的输出合并，故另写一个函数来完成
    output_dict_1 = get_context_and_feedback_from_ai(pdf_name, article_name, translation)
    print(output_dict_1)
    print("/*---------------------------------------------------------------*/")
    # output_dict_2 = get_cited_by(article_name)
    output_dict_2 = {'Status': 'OK', 'cited_by_num': 21, 'cited_by_details': {'cited_by_0': {'title': 'Automatic belief network modeling via policy inference for SDN fault localization', 'snippet': 'Fault localization for SDN becomes one of the most critical but difficult tasks. Existing tools typically only address a specific part of the problem (eg, control plane verification, flow …'}, 'cited_by_1': {'title': 'A survey of fault management in network virtualization environments: Challenges and solutions', 'snippet': 'The advent of 5G and the ever increasing stringent requirements in terms of bandwidth, latency, and quality of service pushes the boundaries of what is feasible with legacy Mobile …'}, 'cited_by_2': {'title': 'Self-healing topology discovery protocol for software-defined networks', 'snippet': 'This letter presents the design of a self-healing protocol for automatic discovery and maintenance of the network topology in software-defined networks. The proposed protocol …'}}}

    Section_B_output = {
        "AI_Status": output_dict_1.get("AI_Status", "N/A"),
        "summaries": output_dict_1.get('summaries', {'c':'d'}),
        "related_work": output_dict_1.get("related_work", {}),
        "logical_chain": output_dict_1.get("logical_chain", {}),
        "cited_by": output_dict_2
    }

    return Section_B_output