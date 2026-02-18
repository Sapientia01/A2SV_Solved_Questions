n = int(input())
res = 0
face = {
    "Tetrahedron" : 4,
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron": 12,
    "Icosahedron" : 20

}

for _ in range(n):
    res+= face[input()]

print(res)
