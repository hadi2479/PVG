#PDF merge하기

import fitz  # PyMuPDF
import os
import re

def extract_number(filename):
    numbers = re.findall(r'\d+', filename)  # 파일명에서 숫자 추출
    return int(numbers[0]) if numbers else float('inf')  # 숫자가 없으면 큰 값 부여

def merge_pdfs(input_folder, output_pdf):
    pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".pdf")],key=extract_number)
    merger = fitz.open()

    for pdf in pdf_files:
        pdf_path = os.path.join(input_folder, pdf)
        doc = fitz.open(pdf_path)
        merger.insert_pdf(doc)
        doc.close()

    merger.save(output_pdf)
    merger.close()
    print(f"PDF 병합 완료: {output_pdf}")

# 사용 예시
input_folder = r"C:\Temp\2025"  # PDF 파일이 있는 폴더 경로
output_pdf = "merged2.pdf"  # 결과 파일명

print(input_folder)
merge_pdfs(input_folder, output_pdf)
