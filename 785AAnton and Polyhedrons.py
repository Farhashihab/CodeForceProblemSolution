n = int(input())
su = 0
for i in range(n):
    k = input()
    if k == "Tetrahedron":
        su += 4
    elif k == "Cube":
        su += 6
    elif k == "Octahedron":
        su += 8
    elif k == "Dodecahedron":
        su += 12
    else:
        su += 20

print(su)
