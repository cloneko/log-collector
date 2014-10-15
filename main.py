import Collector
import json

hostname = 'www2.pref.okinawa.jp'

okinawa = Collector.Collector(hostname,'/oki/Gikairep1.nsf/481e05e7edaca1db49256f540004c033/7fb73c2cf7988bc8492579e30024d9b5?OpenDocument')
#okinawa = Collector.Collector(hostname,'/oki/Gikairep1.nsf/481e05e7edaca1db49256f540004c033?OpenView')

logs = []

nextpath = ''
while True:
    content = okinawa.get(nextpath)
    nextpath = content['next']
    print(content)
    logs.append(content)
    if nextpath == '':
        break 

json.dump(logs,open('output.json','w'))
