import numpy as np
import math

rango= 1024

cosenoEnCero=[math.cos(i/rango*math.pi)/2 for i in range(rango)]
rampaArriba=[i*rango for i in rango]
escalon=[int((2*i))>rango) for i in range(rango)]
