from stats_data import StatsData

lista = []

elem = ""

while(elem.lower() != "fin"):
    elem = input("Introduce un numero (fin para terminar): ")
    if(elem.lower() != "fin"):
        lista.append(float(elem))

sd = StatsData(lista)

print('Lista de numeros:', sd.l_data)
print('Media:', sd.media)
print('Mediana:', sd.mediana)
print('Varianza:', sd.varianza)
