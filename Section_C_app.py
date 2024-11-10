from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO
from Section_C_input import Section_A_output, Section_D_output, Section_B_output

app = Flask(__name__)

def get_article_details(title):
    # For testing purposes, we use the provided data directly
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
        'google_scholar_profile': Section_A_output.get('author_info', {}).get('google_scholar_profile', 'N/A'),
        'search_link': Section_A_output.get('author_info', {}).get('search_link', 'N/A')
    }
    return article

def create_excel_file(article):
    df = pd.DataFrame([article])
    df = df.transpose()
    df.reset_index(inplace=True)
    df.columns = ['Heading', 'Details']
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Article Details')
        writer.close()
    output.seek(0)
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_article', methods=['POST'])
def fetch_article():
    title = request.form['title']
    article = get_article_details(title)
    return render_template('article_details.html', article=article)

@app.route('/download_excel')
def download_excel():
    title = request.args.get('title')
    article = get_article_details(title)
    excel_file = create_excel_file(article)
    return send_file(excel_file, as_attachment=True, download_name="article_details.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/download_pdf')
def download_pdf():
    title = request.args.get('title')
    article = get_article_details(title)
    pdf_link = article['pdf_link']
    return send_file(pdf_link, as_attachment=True, download_name="article.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True, port=5017)