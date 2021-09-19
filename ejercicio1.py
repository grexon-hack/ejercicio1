import math

puerta=float(input("la longitud de la puerta es: "))
muro=float(input("ingrese la longitud del muro: "))
cuerda=math.sqrt(puerta**2 + muro**2)

#polea
diametro=100
polea=math.pi*diametro

#chawbacca
chawbaca=polea*3

#tiempo para cerrar la puerta
tiempo=120
vel=polea/tiempo

#cantidad de chawbaccas
cantidad=math.ceil(cuerda/(chawbaca/100))


print(f"la longitud de la cuerda es:{cuerda:.1f}mts, la circunsferencia de la polea es: {polea:.1f}ctms y la velocidad que deben subir la puerta es: {vel:.1f}cmt/seg, y se necesitan {cantidad} chawbaccas")