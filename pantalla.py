import numpy as arreglo
from PIL import Image, ImageTk

datos = 1024
forma = 240


def Pantalla(color):
    
 
    frame = arreglo.zeros((forma, datos,3),'C' ,arreglo.uint8)

    for n in range(datos):
        frame[forma-n%forma-1,n,:]=arreglo.array(color)

    print(frame.shape,frame.dtype)
    im = Image.fromarray(frame)
    imagen = ImageTk.PhotoImage(image=im)

    return imagen
