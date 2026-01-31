#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max =  100 - dalto_curso / otros_cursos_max * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio =100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto =100 - dalto_curso * 1000 // crudo_dalto / 10


print("------------------------------")
print("El Curso de Dalto dura un")
print(f'{diferencia_con_min}% menos que el mas rapido')
print(f'{round(diferencia_con_max, 2)}% menos que el mas lento')
print(f'{diferencia_con_promedio}% menos que el promedio')
print("------------------------------")

print(f'El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio removido')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio ')

print("------------------------------")
#Mostrando diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio / dalto_curso * 10, 2)} horas de otros cursos')
print(f'Ver 10 horas de este curso equivale a ver {round(dalto_curso / otros_cursos_promedio *10, 2)} horas del curso')
