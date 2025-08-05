# Tutorial Básico de Python: Ciclos, Fibonacci, Tiempo, Refactorización y GitHub

Este tutorial está diseñado para ayudarte a comprender algunos conceptos fundamentales de programación en Python, incluyendo estructuras de control, manipulación del tiempo, buenas prácticas de codificación, y cómo empezar con GitHub y Python profesionalmente.

---

## 🔁 Ciclos `for` y `while` en Python

Los ciclos son estructuras que permiten repetir bloques de código varias veces. En Python, los más comunes son:

### Ciclo `for`
Se usa cuando sabes cuántas veces quieres repetir un bloque de código.

```python
for i in range(5):
    print("Iteración:", i)
Ciclo while
Se usa cuando quieres repetir un bloque de código mientras se cumpla una condición.

python
Copiar
Editar
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
🧮 Explicación de la Serie de Fibonacci
La Serie de Fibonacci es una sucesión de números en la que cada número es la suma de los dos anteriores. Comienza típicamente con 0 y 1.

Código de ejemplo:
python
Copiar
Editar
n = 10  # Número de elementos
a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
Esta secuencia produce: 0 1 1 2 3 5 8 13 21 34

🖼️ Puedes ver este recurso gráfico explicativo en Canva:
🔗 Ver Canva - Serie Fibonacci
