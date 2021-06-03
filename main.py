"""
Reto 3. Hallemos al sospechoso
Yenifer Barco Castrillón
Mayo 24-2021
"""

#==========================================================
#    Librerias utilizadas
# =========================================================

#==========================================================
#    Definicion de funciones(Dividir)
# =========================================================
def sector(x,y):
    """ 
    Parameters
    ----------
    x,y:float
     valor de las coordenadas del sospechoso
    """ 
    #Verificar si esta dentro del sector
    if 2<=x<=8 and 2<=y<=9:
        
        #Verificar si se encuentra en las antenas
        if (x==2 and y==3) or (x==2 and y==9) or (x==5 and y==6) or (x==8 and y==9) or (x==8 and y==3):
            print("")
        else:
            #Verificar si esta sobre la linea roja
            #Sector 1y 2
            if (2<=x<=8 and y==9) or (6<=y<=9 and x==5):
                print("Deniska está entre el Sector 1 y 2")
            elif (2<=x<=8 and y==3) or (3<=y<=6 and x==5):
                print("Deniska está entre el Sector 3 y 4")
            elif (3<=y<=9 and x==2) or (2<=x<=5 and y==6):
                print("Deniska está entre el Sector 1 y 3")
            elif (5<=x<=8 and y==6) or (3<=y<=9 and x==8):
                print("Deniska está entre el Sector 2 y 4")
            #Verificar en que sector se encuentra
            elif 2<x<5 and 6<y<9:
                print("S1")
            elif 5<x<8 and 6<y<9:
                print("S2")
            elif 2<x<5 and 3<y<6:
                print("S3")
            elif 5<x<8 and 3<y<6:
                print("S4")
    else:
        print("Deniska ha escapado")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

coordenada_x = float(input("Por favor ingrese a X: "))
coordenada_y = float(input("Por favor ingrese a y: "))
sector(coordenada_x,coordenada_y)
