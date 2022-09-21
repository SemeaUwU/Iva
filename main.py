#Nombre: scott orellana curso: 4°B
print("cantidad de productos:")
prods = int(input())
i=0
sub=0
while i<prods:
  print("producto",i+1," valor:")
  val = int(input())
  print("cantidad")
  cant = int(input())
  subpro=val*cant
  sub=sub+subpro
  i+=1
iva = sub * 0.19
total = sub + iva
print("se vendieron:",prods,"productos")
print("subtotal: ",sub)
print("iva 19% ",iva)
print("total: ",total)