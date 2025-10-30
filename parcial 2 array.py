def invertir_array(lista):
    return lista[::-1]
n = int(input("¿Cuántos elementos tendrá el array? "))
array = []
for i in range(n):
    valor = input(f"Ingresa el elemento {i + 1}: ")
    array.append(valor)
array_invertido = invertir_array(array)
print("Array original:", array)
print("Array invertido:", array_invertido)
