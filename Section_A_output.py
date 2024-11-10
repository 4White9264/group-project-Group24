article = {
    "title": "Noncommutative Poisson structure and invariants of matrices",
    "link": "https://arxiv.org/abs/2402.06909",
    "snippet": (
        "We introduce a novel approach that employs techniques from noncommutative Poisson geometry to comprehend the algebra of invariants of two $ n\\times n $ matrices. "
        "We entirely solve the open problem of computing the algebra of invariants of two $4\\times 4$ matrices. As an application, we derive the complete description of the "
        "invariant commuting variety of $4\\times 4$ matrices and the fourth Calogero-Moser space."
    ),
    "summary": "F Eshmatov, X García-Martínez, R Turdibaev - arXiv preprint arXiv …, 2024 - arxiv.org",
    "authors": ["F Eshmatov", "X García-Martínez", "R Turdibaev"],
    "journal": "arXiv preprint arXiv …",
    "cited_by": "N/A",
    "author_info": {
        "name": "Farkhod Eshmatov",
        "affiliation": "Professor of Mathematics, AKFA University",
        "email": "Verified email at akfauniversity.org",
        "top3_publications": [
            {
                "title": "Noncommutative Poisson structures, derived representation schemes and Calabi-Yau algebras",
                "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=K23i7AcAAAAJ&citation_for_view=K23i7AcAAAAJ:u-x6o8ySG0sC",
                "cited_by": 33
            },
            {
                "title": "Recollement of deformed preprojective algebras and the Calogero-Moser correspondence",
                "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=K23i7AcAAAAJ&citation_for_view=K23i7AcAAAAJ:Y0pCki6q_DkC",
                "cited_by": 18
            },
            {
                "title": "The derived non-commutative Poisson bracket on Koszul Calabi–Yau algebras",
                "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=K23i7AcAAAAJ&citation_for_view=K23i7AcAAAAJ:hqOjcs7Dif8C",
                "cited_by": 13
            }
        ],
        "google_scholar_profile": "https://scholar.google.com/citations?user=K23i7AcAAAAJ&hl=en&oi=ao",
        "search_link": "https://scholar.google.com/scholar?q=Farkhod+Eshmatov&hl=en",
        "interests": "",
        "h_index": 8,
        "i10_index": 7,
        "cited_by": 155,
        "h_index_score": 5.33,
        "i10_index_score": 1.56,
        "total_citations_score": 0.52,
        "total_score": 7.41
    }
}


def print_dict(d, indent=0):
    for key, value in d.items():
        if isinstance(value, dict):
            print(' ' * indent + f"{key}:")
            print_dict(value, indent + 4)
        elif isinstance(value, list):
            print(' ' * indent + f"{key}:")
            for item in value:
                if isinstance(item, dict):
                    print_dict(item, indent + 4)
                else:
                    print(' ' * (indent + 4) + str(item))
        else:
            print(' ' * indent + f"{key}: {value}")

print_dict(article)