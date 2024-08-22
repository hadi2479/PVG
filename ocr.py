from PIL import Image
import pytesseract

# Tesseract의 경로를 명시해 줍니다. (윈도우 환경에서만 필요)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지 파일을 열고 OCR을 수행합니다.
image = Image.open('example_image.png')
text = pytesseract.image_to_string(image, lang='eng')

print(text)
