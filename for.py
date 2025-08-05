# medicion de ejecucion 
import time
import os,sys
inicio=time.time()
for i in range(5):
    print(i)
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecución de para:", tiempoFinal)
time.sleep(5)  # Pausa de 2 segundos
if sys.platform == "win32":
    os.system('cls')  # Limpia la consola en Windows
else:
    os.system('clear')  # Limpia la consola en Unix/Linux


# ciclo mientras
inicio=time.time()
contador=0
while contador<=10:
    print(contador)
    contador+=1 # contador = contador +1  
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecución:", tiempoFinal) 
"""
    contador = contador +1 
    0  = 0 + 1
    1  = 1 + 1
    2  = 2 + 1
    3  = 3 + 1
    4  = 4 + 1 .....
"""