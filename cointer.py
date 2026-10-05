xA = float(input("xA = "))
yA = float(input("yA = "))
xB = float(input("xB = "))
yB = float(input("yB = "))
if xA == xB:
    print("Pas de fonction affine")
else:
    a = (yB - yA) / (xB - xA)
    b = yA - a * xA
    print(f"f(x) = {a}x + {b}")