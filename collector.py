import urllib.request
import re

class Collector:

    def __init__(self,hostname,firstpath):
        self.hostname = hostname
        self.firstpath = firstpath 


    def get(self,path = ''):
        path = self.firstpath if path == '' else path
        content = self.wget('http://' + self.hostname + path) 
        return self.parser(content)

    def wget(self,url): 
        return urllib.request.urlopen(url).read().decode('sjis')

    def parser(self,content):

        titlePattern = '<td width="66%" bgcolor="#CCCCFF">((昭和|平成).*?)</td>'
        datePattern = '<td width="66%" bgcolor="#CCCCFF">(?:昭和|平成).*</td><td width="34%" bgcolor="#CCCCFF"><div align="right">(.*?)</div></td>'
        speakerPattern = '<tr valign="top"><td width="66%" bgcolor="#CCCCFF">(.*)</td><td width="34%" bgcolor="#CCCCFF"><img width="1" height="1" src="/icons/ecblank.gif" border="0" alt=""></td></tr>'
        bodyPattern = '<HR width=98%>(.*)<HR width=98%>'
        prevPattern = '<a href="(.*&amp;To=Prev)">'
        nextPattern = '<a href="(.*&amp;To=NextMain)">' 

        title = re.search(titlePattern,content).group(1)
        date = re.search(datePattern,content).group(1) if re.search(datePattern,content) != None else ''
        speaker = re.search(speakerPattern,content).group(1) if re.search(speakerPattern,content)  != None else ''
        body = re.search(bodyPattern,content,re.MULTILINE + re.DOTALL).group(1)
        prevUrl = re.search(prevPattern,content).group(1)
        nextUrl = re.search(nextPattern,content).group(1)
        obj = {'title': title,'date': date,'speaker': speaker,'body': body,'prev': prevUrl,'next': nextUrl}
        #print(title)
        #print(date)
        #print(speaker)
        #print(body)
        #print(prevUrl)
        #print(nextUrl)

        return obj
