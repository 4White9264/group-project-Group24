import streamlit as st
import pandas as pd
from io import BytesIO
from Ctest_article import arxiv_api_calling

def create_excel_file(article):
    # Create a DataFrame from the article details
    df = pd.DataFrame([article])


    # Transpose the DataFrame to revert rows and columns
    df = df.transpose()

    # Add the heading of each article detail at the first column
    df.reset_index(inplace=True)
    df.columns = ['Heading', 'Details']

    # Create an in-memory output file for the Excel file
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Article Details')
        writer.close()  # Use close method instead of save

    output.seek(0)
    return output

# Title of the Streamlit App
st.title('ArXiv Article Summarizer and PDF Downloader')

# Input form for article title
article_title = st.text_input('Enter the article title:')
translation = 'English'  # Default translation language

if st.button('Fetch Article Details') and article_title:
    with st.spinner('Fetching details from arXiv...'):
        try:
            article = arxiv_api_calling(article_title, translation)

            # Display article details
            st.write(f"**ID:** {article['id']}")
            st.write(f"**Published:** {article['published']}")
            st.write(f"**Updated:** {article['updated']}")
            st.write(f"**Title:** {article['title']}")
            st.write(f"**Summary:** {article['summary']}")
            st.write(f"**Authors:** {', '.join(article['authors'])}")
            st.write(f"**PDF Link:** {article['pdf_link']}")
            st.write(f"**Summarized Summary:** {article['summarized summary']}")

            # Create Excel file
            excel_file = create_excel_file(article)

            # Add download button for the Excel file
            st.download_button(
                label='Download Article Details in Excel',
                data=excel_file,
                file_name=f"{article_title}.xlsx",
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

            # Add download button for the PDF file
            if article['pdf_link'] != 'N/A':
                st.download_button(
                    label='Download PDF',
                    data=article['pdf_link'],
                    file_name=f"{article_title}.pdf",
                    mime='application/pdf'
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
