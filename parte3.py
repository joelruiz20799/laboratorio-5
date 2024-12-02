# Lista de estudiantes
estudiantes = ["Ana", "Luis", "Carlos", "María"]

for estudiante in estudiantes:
    print(estudiante)

# Diccionario de contacto
contacto = {
    "nombre": "Juan Pérez",
    "correo": "juan.perez@example.com"
}

for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

# Agregar elementos a lista o actualizar diccionario
tareas = []

while True:
    tarea = input("Introduce una tarea (o escribe 'salir' para terminar): ")
    if tarea.lower() == "salir":
        break
    tareas.append(tarea)

print("Tus tareas son:")
for tarea in tareas:
    print(f"- {tarea}")

contactos = {
    "Juan": "juan@mail.com",
    "Ana": "ana@mail.com"
}

nombre = input("¿Qué nombre quieres agregar o actualizar? ")
correo = input(f"Introduce el correo de {nombre}: ")
contactos[nombre] = correo

print("Lista de contactos actualizada:")
for nombre, correo in contactos.items():
    print(f"{nombre}: {correo}")
