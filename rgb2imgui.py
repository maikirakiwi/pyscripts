import time

RGB = input('Enter rgb: ')
RGB = RGB.strip()
RGB = RGB.split(",")
r, g, b = RGB

r = int(r)
g = int(g)
b = int(b)

Ri = (r / 255)
Gi = (g / 255)
Bi = (b / 255)
print("{:0.2f}, {:0.2f}, {:0.2f}".format(Ri, Gi, Bi))
time.sleep(10)
exit()