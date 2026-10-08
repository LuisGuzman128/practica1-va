# Practica 1 - Vision Artificial
# Luis Axel Guzman Martinez
# CBTis 128

import cv2

print("====================================")
print("       PRACTICA 1 - VISION ARTIFICIAL")
print("====================================")

print("OpenCV instalado correctamente")
print("Version de OpenCV:", cv2.__version__)

imagen = cv2.imread("pug.jpg")

if imagen is not None:
    print("La imagen se cargo correctamente")
    print("Ancho:", imagen.shape[1])
    print("Alto:", imagen.shape[0])
else:
    print("No se encontro la imagen pug.jpg")

print("Programa ejecutado correctamente.")