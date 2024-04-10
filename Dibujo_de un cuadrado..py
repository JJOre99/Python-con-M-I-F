import turtle

# Aca definimos la opcion turtle para una imagen cuadrada
t = turtle.Turtle()

# Con esta parte definimos los colores a ver en la presentacion
turtle.bgcolor("lightblue")
t.pensize(2)
t.color("red")

# Dibujamos en las posiciones declaradas
t.penup()
t.goto(-50, -50)  # Posición inicial del cuadrado
t.pendown()

# Dibujar el cuadrado
for _ in range(4):
    t.forward(100)  # Avanzar 100 unidades
    t.right(90)     # Girar 90 grados hacia la derecha

# Cerrar la ventana al hacer clic
turtle.done()