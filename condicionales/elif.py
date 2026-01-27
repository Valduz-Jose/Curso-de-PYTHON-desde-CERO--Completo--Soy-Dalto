ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else if (elif  en python)
if ingreso_mensual > 10000:
  if ingreso_mensual-gasto_mensual < 0:
    print("estas en defecit")
  else:
    print("estas bien")
    
  print("estas bien economicamente en cualquier parte del mundo")

elif ingreso_mensual > 1000:
  print("estas bien economicamente en latinoamerica")

elif ingreso_mensual > 500:
  print("estas bien economicamente en Venezuela") 
else:
  print("Eres pobre")