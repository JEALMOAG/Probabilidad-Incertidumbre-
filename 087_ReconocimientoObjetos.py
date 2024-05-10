"""
created on 12 Abril 20:32:19 2024
@author:Jesus Alejandro Montes Aguila
"""
'''
El código utiliza OpenCV para realizar la coincidencia de plantillas entre una 
imagen de entrada y una plantilla específica. Se cargan las imágenes, 
se convierten a escala de grises y se aplican varios métodos de coincidencia. 
Luego, se identifica la región donde la plantilla coincide mejor con la imagen
 de entrada y se dibuja un rectángulo alrededor de esa región. Finalmente, se 
 muestran las imágenes con el rectángulo dibujado y se espera a que el usuario 
 presione una tecla para mostrar el siguiente método de coincidencia.
 '''
import cv2
image = cv2.imread("personas.jpg")
#image = imagenOriginal.copy()
template = cv2.imread("template1.jpg")


image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

#cv2.imshow('personasGris', image_gray)

methods = [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED,cv2.TM_CCORR,cv2.TM_CCOEFF_NORMED\
           ,cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED]
for method in methods:
    res = cv2.matchTemplate(image_gray, template_gray, method=method)

    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
    print(min_val,max_val,min_loc,max_loc)
    if method == cv2.TM_SQDIFF or cv2.TM_SQDIFF_NORMED :
        x1,y1 = min_loc
        x2,y2 = min_loc[0] + template.shape[1], min_loc[1] + template.shape[0]
    else:
      x1,y1 = max_loc
      x2,y2 = max_loc[0] + template.shape[1],max_loc[1] + template.shape[0]   
    
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
    cv2.imshow("Image", image)
    cv2.imshow("Template", template)
 #   image_gray = imagenOriginal.copy()
    cv2.waitKey(0)
cv2.destroyAllWindows()