import requests
import urllib.request
import time
from bs4 import BeautifulSoup

fics = []
options = {"15/dragon_ball_z": 61,
					 "16/dragon_ball_gt": 17,
 					 "14/dragon_ball": 10}
for option in options:
	for offset in range(options[option]):
		url = "https://fanfiction.com.br/categoria/{}/offset/{}".format(option, offset*10)
		response = requests.get(url)

		soup = BeautifulSoup(response.text, "html.parser")
		
		posts = soup.findAll("div", {"class": "blog_entry story_listing"})	
		for post in posts:
			# ver se o post é de 2015 pra tras
			#new_url = "https://fanfiction.com.br{}".format(
			#	post.findAll("p", {"class": "storytitle"})[0].findAll("a")[0].contents
			#	)
			#new_response = requests.get(url)
			#new_soup = BeautifulSoup(new_response.text, "html.parser")
			#print(new_soup.find("span", {"class": "label"}).find_parent("div").contents)
			#publicada_em = int(new_soup.findAll("b", string="Publicada:")[0].contents.split('/')[-1])
			#if publicada_em >= 2009 and publicada_em <= 2015:
			titulo = post.findAll("a")[0].contents
			usuario = post.findAll("a", {"class": "tooltip_userinfo"})[0].contents
			fics.append("{} ({})".format(titulo, usuario))
		time.sleep(1)
for fic in fics:
	print(fic)
