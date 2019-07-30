from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req



def checkprice(name=None):

	url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(name)
	webopen = req(url) #open website without open browser
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html,'html.parser')
	price = data.findAll('div',{'class':'col-xs-6'})
	st_title = price[0].text
	st_price = price[2].text
	text = "STOCK: {} PRICE: {} BAHT".format(st_title,st_price)
	print(text)


checkprice("TCAP")
