class MetodosOrdenamiento:
    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)    #sacar el tamaño del arreglo
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        
        return arreglo
    
    
    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo) ### sacar el tamaño del arreglo
        for i in range(n):
            hubo_cambio = False
            for j in range(j + 1, n - i - 1):
                if arreglo[i] > arreglo[j + 1]:
                    arreglo[i], arreglo[j + 1] = arreglo[j + 1], arreglo[i]
                    hubo_cambio = True

                if not hubo_cambio:
                    break
        return arreglo

    
    
    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j
            
            arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]

        return arreglo
        
        