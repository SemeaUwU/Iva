#Juan Iturriaga 4B
#hola
a = input("Ingrese el nombre del producto: ")
b = int(input("Ingrese el precio del producto: "))
c = int(input("Ingrese las Unidades a llevar del producto: "))
st = b*c
IVA = (b*c)*0.19
pt = IVA+b*c

print("\n Producto : ", a, "\n", "Precio : ", b, "$", "\n", "Cantidad: ", c, "\n", "Subtotal: ", st,"$", "\n", "IVA: ", IVA ,"$", "\n", "Total: ", pt ,"$",)