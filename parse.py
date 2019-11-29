from bs4 import BeautifulSoup
import requests

def get_html(url):
	a = requests.get(url)
	return a.text

def get_page_data(html):
	arr = []
	di = {}
	counter = 0
	counter1 = 0
	soup = BeautifulSoup(html,'lxml')
	a = soup.find_all('div')
	for i in a:
		counter += 1
		try:
			counter1 += 1
			i.find('p',class_='genre')
			ganre = i.find('p',class_='genre').find_all('a')
			s1 = ''
			for j in ganre:
				s1 += j.text
			arr.append(ganre)
			di['ganre'+str(counter1)] = s1 
		except:pass
		name = i.find('input').next.next.text
		author = i.find_all('a')[-1].text
		download1 = i.find_all('a')[-2].get('href')
		download2 = i.find_all('a')[-3].get('href')
		download3 = i.find_all('a')[-4].get('href')
		links = 'mobi - ' + 'https://www.flibusta.site' + download1 + '\n' + 'fb2 - ' + 'https://www.flibusta.site' + download2 + '\n' + 'epub - ' + 'https://www.flibusta.site' + download3 + '\n' 
		di['article'+str(counter)] = str(counter) + '.  ' + name + '-' +author
		di['download'+str(counter)] = links
		arr.append(name)
		arr.append(author)
	return di

def main_parse(name):

	url = 'https://www.flibusta.site/makebooklist?ab=ab1&t=%s&sort=sd2&' % name
	a = get_page_data(get_html(url))
	# a1 = ''
	# for i in a:
	# 	tmp = True
	# 	if type(i) == list:
	# 		for k in i:
	# 			a1+=k
	# 			tmp = False
	# 	if tmp == True:
	# 		a1 += i + '\n'
	return a
