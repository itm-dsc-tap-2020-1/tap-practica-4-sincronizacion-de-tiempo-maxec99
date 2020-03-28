import os
import ntplib
import datetime
from time import ctime

x = datetime.datetime.now()
print ("Fecha y hora ACTUAL de la maquina= %s" % x)

servidor_de_tiempo = "time-e-g.nist.gov"

print("\n Obteniendo la hor del servidor NIP:")
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time),"%a %b %d %H:%M:%S %Y")
print("Fecha y hora ACTUAL del servidor " + servidor_de_tiempo + ": " + str(hora_actual) + "\n")

y=((hora_actual-x)/2)
datetime.timedelta(3,1)
print("\n Ajuste:%s" %y)

hora_actual=hora_actual-y
print("\n Hora real ACTUAL:%s" %hora_actual)

print ("\n Ajustando reloj de la maquina.... " )
os.system(f"date --set '{hora_actual}'")
print("\n Ajustado con exito")
