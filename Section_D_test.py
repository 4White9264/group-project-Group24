from Section_D_arxiv_api_integration import arxiv_api_calling


# 调用函数
article_title = "Self-Modeling Based Diagnosis of Software-Defined Networks"
translation = "English"
# article = arxiv_api_calling(article_title, translation)



article = {
    "ID": "http://arxiv.org/abs/1507.03352v1",
    "Published": "2015-07-13",
    "Updated": "2015-07-13",
    "Title": "Self-Modeling Based Diagnosis of Software-Defined Networks",
    "Summary": (
        "Networks built using SDN (Software-Defined Networks) and NFV (Network "
        "Functions Virtualization) approaches are expected to face several challenges "
        "such as scalability, robustness and resiliency. In this paper, we propose a "
        "self-modeling based diagnosis to enable resilient networks in the context of "
        "SDN and NFV. We focus on solving two major problems: On the one hand, we lack "
        "today of a model or template that describes the managed elements in the context "
        "of SDN and NFV. On the other hand, the highly dynamic networks enabled by the "
        "softwarisation require the generation at runtime of a diagnosis model from "
        "which the root causes can be identified. In this paper, we propose finer "
        "granular templates that do not only model network nodes but also their "
        "sub-components for a more detailed diagnosis suitable in the SDN and NFV "
        "context. In addition, we specify and validate a self-modeling based diagnosis "
        "using Bayesian Networks. This approach differs from the state of the art in the "
        "discovery of network and service dependencies at run-time and the building of "
        "the diagnosis model of any SDN infrastructure using our templates."
    ),
    "Authors": "José Manuel Sánchez, Imen Grida Ben Yahia, Noel Crespi",
    "PDF Link": "http://arxiv.org/pdf/1507.03352v1",
    "Summarized Summary": (
        "This paper addresses the challenges of scalability, robustness, and resiliency "
        "in SDN (Software-Defined Networks) and NFV (Network Function Virtualization) "
        "environments by proposing a self-modeling based diagnosis approach. It presents "
        "finer granular templates that model not only network nodes but also their "
        "sub-components for more precise diagnosis. The authors employ Bayesian Networks "
        "to dynamically generate a diagnosis model at runtime, enabling the identification "
        "of root causes. This approach distinguishes itself by its ability to discover "
        "network and service dependencies in real time and construct diagnosis models for "
        "SDN infrastructures using the proposed templates."
    )
}

# 构建输出字符串
output = (
    f"ID: {article['ID']}\n"
    f"Published: {article['Published']}\n"
    f"Updated: {article['Updated']}\n"
    f"Title: {article['Title']}\n"
    f"Summary: {article['Summary']}\n"
    f"Authors: {article['Authors']}\n"
    f"PDF Link: {article.get('PDF Link', 'N/A')}\n"
    f"Summarized Summary: {article.get('Summarized Summary')}\n"
)

# 打印输出字符串
print(output)


