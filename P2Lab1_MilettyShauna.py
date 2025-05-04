#P2Lab1
#04/12/2025
#p2Lab1
#Usig math expressions
import math

#get radius from user
radius=float(input("Enter the radius:"))

#calculate circumfrence, radius and diameter
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#display results
print(f"The diameter of the circle is {diam: .1f}")
print(f"The circumference of the circle is {cir: .2f}")
print(f"The area of the circle is {area: .3f}")             
