from metodos_ordenamiento import MetodosOrdenamiento
import random
import time


class Benchmarking:
    # public Benchmarking
    def __init__(self):
        print('Benchmarking instanciado')
        
        self.mO = MetodosOrdenamiento()
        
        arreglo = self.build_arreglo(10000)
        
        tarea = lambda: self.mO.sort_bubble(arreglo)
        #milisegundos = self.contar_con_current_time_milles(tarea)
        nanosegundos = self.contar_con_nano_time(tarea)
        #print(f'Tiempo en milisegundos: {milisegundos}')
        print(f'Tiempo en nanosegundos metodo burbuja: {nanosegundos}')


        tarea = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo)
        nanosegundos = self.contar_con_nano_time(tarea)
        print(f'Tiempo en nanosegundos con metodo burbuja mejorado: {nanosegundos}')
        
        
        tarea = lambda: self.mO.sort_seleccion(arreglo)
        nanosegundos = self.contar_con_nano_time(tarea)
        print(f'Tiempo en nanosegundos con metodo seleccion: {nanosegundos}')
        
        
    def build_arreglo(self, tamano):
        arreglo = []
        for i in range(tamano):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo
    
    
    # milisegundos en segundos con # x = time.time()
    # nanosegundo con # x = time.time_ns()
    # ejecutar en tarea()
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)
    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio)/ 1_000_000_000.0
    
    
    
        
        
        
        
    