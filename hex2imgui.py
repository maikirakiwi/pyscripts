import time

h = input('Enter hex: ').lstrip('#')
RGB = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
r, g, b = RGB

Ri = (r / 255)
Gi = (g / 255)
Bi = (b / 255)
print("{:0.2f}, {:0.2f}, {:0.2f}".format(Ri, Gi, Bi))
time.sleep(10)
exit()