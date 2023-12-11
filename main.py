import streamlit as st
import PyPDF2 as pdf

uploaded_file = st.file_uploader("Загрузить пдф", type=["pdf"])

lst = []
output_pdf = pdf.PdfWriter()

if uploaded_file:
    reader = pdf.PdfReader(uploaded_file)

    for i in range(len(reader.pages)):
        text = reader.pages[i].extract_text()
        sku = (text.split()[3].split('-')[1])
        lst.append(f'{sku}-{i}')

    lst.sort()

    for value in lst:
        page_num = int(value.split('-')[1])
        obj = reader.pages[page_num]
        output_pdf.add_page(obj)

    with open(r'output.pdf', "wb") as writefile:
        output_pdf.write(writefile)

    with open("output.pdf", "rb") as f:
        st.download_button("Скачать пдф", f, "output.pdf", use_container_width=True)

