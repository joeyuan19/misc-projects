from selenium import webdriver
from random import randint

import subprocess

if __name__ == "__main__":
	browser = None 
	movie_url = "http://movies.netflix.com/WiGenre?agid=6548"
	login_url = "https://signup.netflix.com/#do-login"
	login_url = "https://signup.netflix.com/login"
	try:
		browser = webdriver.Firefox()
		browser.get(login_url)
		
		#sign_in = browser.find_elements_by_xpath("//a[@href='do-login']")
		#sign_in[0].click()
		
		num_options = 5


		email = browser.find_element_by_xpath("//input[@id='email']")
		email.send_keys("kathleenoc@earthlink.net")
		
		password = browser.find_elements_by_xpath("//input[@id='password']")
		password[0].send_keys("hobbes210")

		login = browser.find_elements_by_xpath("//button[@id='login-form-contBtn']")
		login[0].click()

		browser.get(movie_url)
		xpath = "//div[@class='" + u'agMovie agMovie-lulg mrNR' + "']/span/"
		
		i = 0
		limit = 200
		while i < limit:
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			i += 1
			print i

		movies = browser.find_elements_by_xpath(xpath + 'a' )
		#print movies
		names = browser.find_elements_by_xpath(xpath + 'img')
		rand = []
		for i in range(num_options):
			rand.append(randint(0,len(movies)))

		#rand_path = "//div[@class='agMvoieSet asMovie-lulg mrTV-MA']/div[" + str(r) + "]/a"
		#rand_movie = browser.find_elements_by_xpath(rand_path)

		i = 1
		for r in rand:
			print "[" + str(i) + "]",  names[r].get_attribute('alt') + ":"
			print "    ", movies[r].get_attribute('href')

	finally:
		if browser:
			browser.close()
	


