demo = [1,'hola',23.4,"mundo",[1,2,3]]
colors = ["rojo","amarillo","azul"]

numberList = list((1,2,3,4))

r = list(range(1,101))
# print(r)
# print(dir(colors))
print("rojo" in colors)

# colors.extend(["violeta", "rosado"])
# colors.extend(('blanco', 'negro'))

# colors.insert(-1, "marron")
colors.insert(len(colors), "fucsia")

# colors.pop()
colors.remove("rojo")

colors.sort(reverse=True)

print(colors.index('azul'))

print(colors)