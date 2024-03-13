#Crearemos una frase ficitia en base a 3 preguntas
preguntas = ['Ingrese el nombre de su animal favorito', 'Ingrese su color favorito', 'Ingrese un calificativo']

def encuesta(lista):
    respuestas = []
    for pregunta in lista:
        print(pregunta)
        print("Ingrese su respuesta")
        respuestas.append(input('> '))
    print('La frase ficticia creada es: ')
    print(respuestas[0],respuestas[1],respuestas[2])



encuesta(preguntas)