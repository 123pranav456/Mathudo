import math as m
import decimal as d
a=m.tan(m.radians(30))
z=d.Decimal(a)
d = z.quantize(d.Decimal('.1'))
print(d)