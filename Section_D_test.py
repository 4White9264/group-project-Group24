from Section_D_Summary import summary
import json

article_title = "Noncommutative Poisson structure and invariants of matrices"
result = summary(article_title)

print(result)


# print(result.get("Evaluation from AI", "N/A"))

# print(result.get("Substitute paper names", "N/A"))


# # 将结果转换为字典并打印
# result_dict = {
#     "ID": "http://arxiv.org/abs/2402.06909v2",
#     "Published": "2024-02-10",
#     "Updated": "2024-02-13",
#     "Title": "Noncommutative Poisson structure and invariants of matrices",
#     "Summary": "We introduce a novel approach that employs techniques from noncommutative Poisson geometry to comprehend the algebra of invariants of two $n\\times n$ matrices. We entirely solve the open problem of computing the algebra of invariants of two $4 \\times 4$ matrices. As an application, we derive the complete description of the invariant commuting variety of $4 \\times 4$ matrices and the fourth Calogero-Moser space.",
#     "Authors": ["Farkhod Eshmatov", "Xabier García-Martínez", "Rustam Turdibaev"],
#     "First Author Info": {
#         "affiliation": "Professor of Mathematics, AKFA University",
#         "scholar_id": "K23i7AcAAAAJ",
#         "citation": 156,
#         "num_publications": 33,
#         "hindex": 8,
#         "hindex5y": 7,
#         "i10index": 7,
#         "i10index5y": 3,
#         "latest_three_publications": [
#             ("Noncommutative Poisson structure and invariants of matrices", "2024"),
#             ("On the coordinate rings of Calogero-Moser spaces and the invariant commuting variety of a pair of matrices", "2023"),
#             ("On transitive action on quiver varieties", "2022")
#         ]
#     },
#     "PDF Link": "http://arxiv.org/pdf/2402.06909v2",
#     "Evaluation from AI": "Based on the summary and the details provided, this paper seems worth reading in detail if you are immersed in fields such as noncommutative geometry, algebraic invariants, or mathematical physics. Specifically, if you're interested in Poisson geometry or the computation of matrix invariants, the paper appears to provide a significant result by fully solving an open problem for $4 \\times 4$ matrices. Additionally, if you're studying applications of matrix invariants to areas like the Calogero-Moser space, this could offer a useful and complete description.",
#     "Substitute paper names": [
#         "Invariants of 4x4 Matrices through Noncommutative Geometry",
#         "Noncommutative Poisson Techniques for Invariant Geometry",
#         "Matrix Invariants and Poisson Structures: A 4x4 Case Study"
#     ]
# }
# print(json.dumps(result_dict, indent=4, ensure_ascii=False))