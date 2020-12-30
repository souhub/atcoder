import math

a, b, C = map(float, input().split())

sinC = math.sin(C*math.pi/180)

h = b*sinC

cosC = math.pow(1-sinC**2, 1/2)
if C == 90:
    cosC = 0
if C > 90:
    cosC = -cosC

s = (1/2)*a*h

c = math.pow(a**2+b**2-2*a*b*cosC, 1/2)

l = a+b+c

print(s, l, h)
