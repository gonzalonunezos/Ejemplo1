print "Hola"
# Buscar el minimo comun multiplo entre 2 numeros
# define a function
def lcm(x, y):
   """Esta función recibe dos enteros y devuelve el multiplo comum"""
 
   # cogemos el mayor de los dos
   if x > y:
       mayor = x
   else:
       mayor = y
 
   while(True):
       if((mayor % x == 0) and (mayor % y == 0)):
           lcm = mayor
           break
       mayor += 1
 
   return lcm
 
 
# solicitamos los dos numeros
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
 
print("El minimo comun multiplo de ", num1," y ", num2," es ", lcm(num1, num2))
