r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
mat = []

for i in range(r):
    mat.append([])
    for j in range(c):
        x=int(input("Enter the element"))
        mat[i].append(x)
#changes
		
print(mat)