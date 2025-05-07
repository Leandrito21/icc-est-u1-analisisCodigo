import matplotlib.pyplot as plt

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


