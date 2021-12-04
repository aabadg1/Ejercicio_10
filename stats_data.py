# Ejercicio 13 de clase

import statistics as st


class StatsData:

    def __init__(self, lista):
        self.l_data = lista
        self.media = st.mean(lista)
        self.varianza = st.variance(lista)
        self.mediana = st.median(lista)
