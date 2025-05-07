#import benchmarking as bm
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
from datetime import datetime


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
    
    
    tamanios = [500, 1000, 1500]
    resultados = []

    for tam in tamanios:
        arreglo_base = benchmark.build_arreglo(tam)

        for nombre, funcion_metodo in diccionario_mt.items():
            tiempo_resultado =benchmark.medir_tiempo(funcion_metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo_resultado)) ## el tupla es un conjunto de datos que no se modifica
        
    for tam, nombre, tiempo in resultados:
        print(f'Tamaño: {tam} Nombre: {nombre} Tiempo: {tiempo}')
    
    # Prepara datos para ser graficados
    # 1. Crear un diccionario o map para almacenar resultados por méetodos
    
    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja_mejorado": [],
        "seleccion": [],
        "shell": [],
        }
    
    
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
        
    """""
    plt.figure(figsize = (10,6))

    # Graficar los tiempos de ejecucion para cada metodo 
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label= nombre, marker= "o")
        
    plt.title("Comparacion de tiempo para cada metodo de ordenamiento")
    plt.xlabel("Tamnio de los arreglos")
    plt.xlabel("Tiempo de ejecucion")

    plt.legend()
    plt.grid(True)
    plt.tight_layout
    plt.show()
    
    

    x = [1,2,3,4,5]
    y = [2,4,6,8,10]

    # Crear un grafico de lineas
    plt.plot(x, y, label = "linea", color= "blue")

    #Agregar parámetros
    plt.title("Mi primer gráfico")
    plt.xlabel("Eje de la X")
    plt.xlabel("Eje de la Y")

    #Agregar leyenda
    plt.legend()

    #Cuadrícula
    plt.grid(True)

    #Mostrar mi ventana del grafico
    plt.show()
    """
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nombre_autor = "LEANDRO LOZADO"

    # Crear una figura con 2 subgráficos (1 fila, 2 columnas)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    fig.canvas.manager.set_window_title(f"{nombre_autor} - {ahora}")

    # Subgráfico 1: Comparación de tiempos
    for nombre, tiempos in tiempos_by_metodo.items():
        axs[0].plot(tamanios, tiempos, label=nombre, marker="o")

    axs[0].set_title("Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento")
    axs[0].set_xlabel("Tamaño del arreglo")
    axs[0].set_ylabel("Tiempo de ejecución (segundos)")
    axs[0].legend()
    axs[0].grid(True)

    # Subgráfico 2: Línea de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    axs[1].plot(x, y, label="Línea 1", color="blue")
    axs[1].set_title("Gráfico de Ejemplo con Matplotlib")
    axs[1].set_xlabel("Eje X")
    axs[1].set_ylabel("Eje Y")
    axs[1].legend()
    axs[1].grid(True)

    # Título global con nombre y fecha
    fig.suptitle(f"{nombre_autor} – {ahora}", fontsize=14, fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # deja espacio para el título
    plt.show()
