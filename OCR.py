import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def scanEng(pic):
	img = Image.open(pic)
	text = pytesseract.image_to_string(img)
	time.sleep(1)
	print(text)
	print("DOne")

def scanThai(pic):
	img = Image.open(pic)
	text = pytesseract.image_to_string(img,lang='tha')#thai 
	time.sleep(1)
	print(text)

scanEng("F:/fern/kedkanok_resume.png")

"""
Kedkanok
Pumsuwan

CONTACT DETAILS

Address: 137 Phahonyothin 59 Anusawari
Bangkhen, Bangkok 10220

Mobile : 0804535460

Email : fernkps1@gmail.com



ABOUT ME

PROFESSIONAL HISTORY

- Extroverted individuals prefer group
activities and get energized by social
interaction

aCommerce.Co,LTD | 2017 - present - Like to set specific goals and accomplish
each day

- I'm looking for an opportunity to work
with strong passion challenge and look
forward company

Social Media Specialist

- Customer service B2C order transaction on
e-marketplace

- Coordinate client B2B with Elca, L'Oreal, Unilever and
Unicharm

- Make report customer feed back

- Support supply-chain in stock for analytics promotion

campainge
RELEVANT SKILLS
INTERNSHIP HISTORY - Sale and Operation marketing
- Microsoft Office
Lost Property Department - Time management skill management
report and document preparation
A.0.T (Airports of Thailand Public Company - Positive-thinking, flexible friendly
Mbnediioe) | Jetaetehy= listen ANP atmosphere of collaboration with
- Provides assistance for customers who have teamwork
lost items. Answers phone and in-person - Ability to work as part of a team as well
inquiries regarding lost items as independently
inquiries regarding lost items as independently

- Accepts found items from multiple sources
and enters items in computerized system

LANGUAGE

- Thai
EDUCATIONAL HISTORY - English

Silpakorn University - French

Graduated 2012-2017

- B.Ain Faculty of Management Science, Tourism
Management GPA 3.21 | graduated as the second class
honors

**References Available Request**
"""