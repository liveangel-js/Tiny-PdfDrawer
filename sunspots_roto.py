#!C:\python27\python

from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from urllib import urlopen
from reportlab.graphics.charts.lineplots import LinePlot
import re

URL='http://www.swpc.noaa.gov/ftpdir/indices/DSD.txt'
data=[]
day=[]
month=[]
flux=[]
sunspot=[]


#retrive data
pattern=re.compile(r'.*?(\d{4})\s+(\d{2})\s+(\d{2})\s+(\d+)\s+(\d+)')
for line in urlopen(URL).readlines():
    result = re.match(pattern,line)
    if result==None:continue
    month.append(int(result.group(2)))
    day.append(int(result.group(3)))
    flux.append(int(result.group(4)))
    sunspot.append(int(result.group(5)))

drawing = Drawing(400,200)

#makeup data
times=[]
for x,y in zip(month,day):
    times.append(x+y/31.0)
print times
print sunspot
print flux
# draw plot
lp = LinePlot()
lp.x=50
lp.y=50
lp.height=125
lp.width=300
lp.data=[zip(times,sunspot),zip(times,flux)]
lp.lines[0].strokeColor=colors.blue
lp.lines[1].strokeColor=colors.red
drawing.add(lp)
renderPDF.drawToFile(drawing,'report.pdf','Sunspot')
    
