# vlan_checker.py

vlan = int(input("Ingrese el número de la VLAN: "))

if 1 <= vlan <= 1005:
    print("La VLAN está en el rango NORMAL.")
elif 1006 <= vlan <= 4094:
    print("La VLAN está en el rango EXTENDIDO.")
else:
    print("La VLAN ingresada no es válida (fuera de rango).")
