import Collector

hostname = 'www2.pref.okinawa.jp'

okinawa = Collector.Collector(hostname,'/oki/Gikairep1.nsf/481e05e7edaca1db49256f540004c033/7fb73c2cf7988bc8492579e30024d9b5?OpenDocument')

nextpath = ''
while True:
    content = okinawa.get(nextpath)
    nextpath = content['next']
    print(content)

