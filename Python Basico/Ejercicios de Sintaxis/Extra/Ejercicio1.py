

price_product = float(input("Escribe el precio del producto: "))
if price_product < 100:
    print ("El descuento aplicado es del 2%")
    discount_total = price_product * 0.02
else:
    print ("El descuento aplicado es del 10%")
    discount_total = price_product * 0.1


total = price_product - discount_total
print ("El precio final es de ", total)