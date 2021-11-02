#uso de bucle while

from time import sleep
temp = 10

while temp < 15:
    temp+=1
    print("La temp está "+str(temp)+" grados")
    print("aumento en 1ºC")
    sleep(1)

print("Temp >= 15ºC")