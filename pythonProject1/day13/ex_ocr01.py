# sudo apt install tesseract-ocr-script-hang tesseract-ocr-script-hang-vert
# pip install pytesseract
# pip install Image
import pytesseract
# import Image
eng = pytesseract.image_to_string('./poem.png')
print(eng)
kor = pytesseract.image_to_string('./han.png', lang='Hangul')
print(kor)