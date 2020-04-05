import math
an = float(input('Informe um ângulo:'))
sen = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('SENO {:.2f}\nCOSSENO{:.2f}\nTANGENTE{:.2f}'.format(sen, co, tang))
