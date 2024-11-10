from flask import Flask, request, render_template, send_file
import pandas as pd
from io import BytesIO
from Section_D_arxiv_for_app import arxiv_api_calling

app = Flask(__name__)

def create_excel_file(article, title):
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

@app.route('/fetch', methods=['POST'])
def fetch():
    article_titles = request.form['article_titles']
    translation = 'English'
    titles = article_titles.split('\n')
    articles = []
    for title in titles:
        title = title.strip()
        if title:
            try:
                article = arxiv_api_calling(title, translation)
                articles.append(article)
            except Exception as e:
                return f'An error occurred while fetching details for "{title}": {e}', 500
    return render_template('results.html', articles=articles)

@app.route('/download_excel/<title>', methods=['GET'])
def download_excel(title):
    article = request.args.get('article')
    excel_file = create_excel_file(article, title)
    return send_file(excel_file, as_attachment=True, download_name=f"{title}.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/download_pdf/<title>', methods=['GET'])
def download_pdf(title):
    pdf_link = request.args.get('pdf_link')
    return send_file(pdf_link, as_attachment=True, download_name=f"{title}.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
