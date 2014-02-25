#C:\python27\python
#this is only prototype
from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50,50,'Hello, world',textAnchor='middle')
d.add(s)
renderPDF.drawToFile(d,'hellp.pdf', 'A simple PDF FILE')
