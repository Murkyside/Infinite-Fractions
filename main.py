# Timothy Gorst 2/12/2021
from guizero import App, Drawing
import math

w = 500
h = 500
pan = 200
scale = 10

app = App(width=w, height=h)
drawing = Drawing(app, width=w, height=h)

def transform(coord):
    return coord * scale + pan

z = 0
definition = 20 # change this for more or less detail
for a in range(-20*definition,10*definition):
  for b in range(-20*definition,10*definition):
    a = a/definition
    b = b/definition
    for k in range(40,1,-1):
      z = ((k-1j)*(a+b*1j))/(1+k*1j+a+b*1j+z)
    z = (z.real**2+z.imag**2)**(1/2)
    try:
      z = 140*math.log(z,10)
      drawing.rectangle(transform(a),transform(-b)-100,transform(a)+2,transform(-b)+2-100,color = (round(z),round(z),round(z)))
    except:
      pass
    a = a*definition
    b = b*definition
