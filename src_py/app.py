#import benchmarking as bm
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

# Archivo principal o main
if __name__ == "__main__":
    print("Funciona")
    #bm.Benchmarking()
    benchmark = Benchmarking()
    metodos = MetodosOrdenamiento()
    
    tam = 10000
    #tamanios = [5000, 10000, 10500]
    #for tam in tamanios:
    arreglo_base = benchmark.build_arreglo(tam)
    
    
    diccionario_mt = {
        "burbuja": metodos.sort_bubble,
        "burbuja_mejorado": metodos.sort_burbuja_mejorado_optimizado,
        "seleccion": metodos.sort_seleccion,
        "shell": metodos.sort_shell
        }
    
    
    tamanios = [5000, 10000, 10500]
    resultados = []

    for tam in tamanios:
        arreglo_base = benchmark.build_arreglo(tam)

        for nombre, funcion_metodo in diccionario_mt.items():
            tiempo_resultado =benchmark.medir_tiempo(funcion_metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo_resultado)) ## el tupla es un conjunto de datos que no se modifica
        
    for tam, nombre, tiempo in resultados:
        print(f'Tamaño:  {tam} Nombre:  {nombre} Tiempo:  {tiempo}')
    

