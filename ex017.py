import math
co = float(input('Cateto oposto:'))
ca = float(input('Cateto adjacente:'))
hipotenusa = math.hypot(co, ca)
print('A hipotenusa dos catetos {}, {} é {:.2f}'.format(co, ca, hipotenusa))