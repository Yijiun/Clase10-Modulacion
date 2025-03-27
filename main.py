# Proyecto: [Clase 10 Modulos]
# Estudiante: [Yi Jiun Liu]
# Fecha de Inicio: [26/3/2025]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

from analisis_datos import *
#from analisis_datos.carga_datos import generar_lista_de_compras
#from analisis_datos.estadisticas import media

lista_compras = generar_lista_de_compras()
print(lista_compras)

precios = [precio for _, precio in lista_compras]
print(precios)

print('La media de nota es:' , media(precios))
print('la mediana de compra es:', mediana (precios))