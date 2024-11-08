from flask import Flask, render_template
from input import Section_A_output, Section_D_output, Section_B_output

app = Flask(__name__)

def get_article_details():
    article = {
        'title': Section_A_output.get('title', 'N/A'),
        'author_name': Section_A_output.get('author_info', {}).get('name', 'N/A'),
        'summary': Section_A_output.get('summary', 'N/A'),
        'snippet': Section_A_output.get('snippet', 'N/A'),
        'pdf_link': Section_D_output.get('pdf link', 'N/A'),
        'summarized_summary': Section_D_output.get('summarized summary', 'N/A'),
        'published': Section_D_output.get('published', 'N/A'),
        'updated': Section_D_output.get('updated', 'N/A'),
        'journal': Section_A_output.get('journal', 'N/A'),
        'cited_by': Section_A_output.get('cited_by', 'N/A'),
        'authors': Section_D_output.get('authors', []),
        'author_info': Section_A_output.get('author_info', {}),
        'related_work': Section_A_output.get('related_work', {}),
        'logical_chain': Section_B_output.get('logical_chain', 'N/A'),
        'Abstract': Section_B_output.get('summaries', {}).get('Abstract', 'N/A'),
        'google scholar profile': Section_A_output.get('author_info', {}).get('google_scholar_profile', 'N/A'),
        'search_link': Section_A_output.get('author_info', {}).get('search_link', 'N/A')
    }
    return article

@app.route('/')
def index():
    article = get_article_details()
    return render_template('index.html', article=article)

if __name__ == '__main__':
    app.run(debug=True, port=5007)