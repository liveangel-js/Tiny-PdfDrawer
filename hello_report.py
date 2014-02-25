#C:\python27\python
#this is only prototype
from reportlab.graphics.shapes import Drawing,String,PolyLine
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50,50,'Hello, world',textAnchor='middle')
d.add(s)
p = PolyLine([(0,0),(10,10),(10,0),(0,10)])
d.add(p)
renderPDF.drawToFile(d,'hello.pdf', 'A simple PDF FILE')
