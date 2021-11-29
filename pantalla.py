import numpy as arreglo
from PIL import Image, ImageTk

datos = 480
forma = 240


def funcion_a_imagen(color):
    
    
    frame = arreglo.zeros((forma, datos,3),'C' ,arreglo.uint8)

    for i in range(datos):
        frame[forma-i%forma-1,i,:]=arreglo.array(color)

    print(frame.shape,frame.dtype)
    im = Image.fromarray(frame)
    imagen = ImageTk.PhotoImage(image=im)

 
    return imagen
