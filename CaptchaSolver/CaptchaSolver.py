import pytesseract
from PIL import Image
from subprocess import check_output


def solve(path):
	return pytesseract.image_to_string(Image.open(path))

if __name__=="__main__":
	path = input('Input path to image:')
	print('Solving Captcha.......')
	print()
	print()
	text = solve(path)
	print('Extracted Text is: ',text)