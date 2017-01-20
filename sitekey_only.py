from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


# sitekey retrieval
def get_sitekey():
	captcha_page = Request('http://www.adidas.com/us/ultra-boost-uncaged-shoes/BA9797.html', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
	                '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'})
	product_page = urlopen(captcha_page)
	soup = BeautifulSoup(product_page, 'html.parser')
	sitekey = soup.find('div', attrs={'class': 'g-recaptcha'})['data-sitekey']
	print(sitekey)


if __name__ == '__main__':
	get_sitekey()