import urllib.request
import re

class Collector:

    def __init__(self,hostname,firstpath):
        self.hostname = hostname
        self.firstpath = firstpath 
        self.titlePattern = '<td width="66%" bgcolor="#CCCCFF">((昭和|平成).*?)</td>'
        self.datePattern = '<td width="66%" bgcolor="#CCCCFF">(?:昭和|平成).*</td><td width="34%" bgcolor="#CCCCFF"><div align="right">(.*?)</div></td>'
        self.speakerPattern = '<tr valign="top"><td width="66%" bgcolor="#CCCCFF">(.*)</td><td width="34%" bgcolor="#CCCCFF"><img width="1" height="1" src="/icons/ecblank.gif" border="0" alt=""></td></tr>'
        self.bodyPattern = '<HR width=98%>(.*)<HR width=98%>'
        self.prevPattern = '<a href="(.*&amp;To=Prev)">'
        self.nextPattern = '<a href="(.*&amp;To=NextMain)">' 


    def get(self,path = ''):
        path = self.firstpath if path == '' else path
        content = self.wget('http://' + self.hostname + path) 
        return self.parser(content)

    def wget(self,url): 
        return urllib.request.urlopen(url).read().decode('sjis')

    def parser(self,content):


        try:
            title = re.search(self.titlePattern,content).group(1)
            date = re.search(self.datePattern,content).group(1) if re.search(self.datePattern,content) != None else ''
            speaker = re.search(self.speakerPattern,content).group(1) if re.search(self.speakerPattern,content)  != None else ''
            body = re.search(self.bodyPattern,content,re.MULTILINE + re.DOTALL).group(1)
            prevUrl = re.search(self.prevPattern,content).group(1)
            nextUrl = re.search(self.nextPattern,content).group(1)
            obj = {'title': title,'date': date,'speaker': speaker,'body': body,'prev': prevUrl,'next': nextUrl}
        except AttributeError:
            obj = {'title': '','date': '','speaker': '','body': '','prev': '','next': ''}

        return obj
