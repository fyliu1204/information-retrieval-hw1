#Run in vagrant, pure shell & no UI
import nltk
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

def readtext(fn):
	f = open(fn, "r")		
	text = f.read()
	f.close()
	word = nltk.word_tokenize(text)
	word = [tmp.lower() for tmp in word]
	return word

def plotfig(dict):
	for tmp_value in dict:
		name = tmp_value
		word = dict[name]
	blog_hash = {}
	total_blog_number = 0
	for tmp_blog in word:
		if re.match('^[A-Za-z]*$',tmp_blog) and tmp_blog not in stopword:
			total_blog_number += 1
			if tmp_blog in blog_hash:
				blog_hash[tmp_blog] += 1
			else:
				blog_hash[tmp_blog] = 1

	blog_number = []
	for tmp_blog_hash in blog_hash:
		blog_number.append(blog_hash[tmp_blog_hash])

	blog_number.sort(reverse = True)
	blog_fre = {}
	for tmp_number in blog_number:
		if tmp_number in blog_fre:
			blog_fre[tmp_number] += 1
		else:
			blog_fre[tmp_number] = 1

	fig, ax = plt.subplots()
	x = []
	y = []
	for key_blog in blog_fre:
		x.append(key_blog)
		y.append(blog_fre[key_blog]/total_blog_number)
	ax.plot(x,y,'o')
	ax.set_xscale('log')
	ax.set_yscale('log')
	plt.savefig(name+'.png')
	return 0

stopword = readtext("stoplist.txt")
blogword = readtext("blog.txt")
spchword = readtext("congress_speech.txt")
blogdict = {'blog':blogword}
spchdict = {'speech':spchword}
plotfig(spchdict)
plotfig(blogdict)