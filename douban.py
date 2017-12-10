import requests
from pyquery import PyQuery as pq 

def getdouban():
	a = 1
	for i in range(0,250,25):
		url = "https://movie.douban.com/top250?start=%s&filter=" %i
		r = requests.get(url)
		for movie in pq(r.content)(".item"):
			num = pq(movie).find(".rating_num").html()
			title = pq(movie).find(".title").html()
			desc = pq(movie).find(".inq").html()
			print("state:%s rate:%s name:%s desc: %s \n" % (a,num,title,desc))
			a += 1
print getdouban()