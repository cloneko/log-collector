import urllib.request
import re



def wget(url): 
	return urllib.request.urlopen(url).read().decode('sjis')

def parser(contents):

	titlePattern = '<td width="66%" bgcolor="#CCCCFF">((昭和|平成).*?)</td>'
	datePattern = '<td width="66%" bgcolor="#CCCCFF">(昭和|平成).*</td><td width="34%" bgcolor="#CCCCFF"><div align="right">([^<]*?)</div><td>'
	speakerPattern = '<tr valign="top"><td width="66%" bgcolor="#CCCCFF">(.*)</td><td width="34%" bgcolor="#CCCCFF"><img width="1" height="1" src="/icons/ecblank.gif" border="0" alt=""></td></tr>'
	bodyPattern = '<HR width=98%>(.*)<HR width=98%>'
	prevPattern = '<a href="(.*&amp;To=Prev)">'
	nextPattern = '<a href="(.*&amp;To=NextMain)">'


	title = re.search(titlePattern,contents).group(1)
	date = re.search(datePattern,contents).group(1) if re.search(datePattern,contents) else ''
	speaker = re.search(speakerPattern,contents).group(1) if re.search(speakerPattern,contents) else ''
#	body = re.search(bodyPattern,contents,re.MULTILINE).group(1)
	prevUrl = re.search(prevPattern,contents).group(1)
	nextUrl = re.search(nextPattern,contents).group(1)
	print(title)
#	print(body)
	print(prevUrl)
	print(nextUrl)





parser(wget('http://www2.pref.okinawa.jp/oki/Gikairep1.nsf/481e05e7edaca1db49256f540004c033/7fb73c2cf7988bc8492579e30024d9b5?OpenDocument'))
