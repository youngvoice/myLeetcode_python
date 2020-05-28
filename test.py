numRows = 4
numCols = 2
mask = [[m+n for m in range(numCols)] for n in range(numRows)]
new_mask = [[col for col in row] for row in mask]

print(mask)
print(new_mask)

if not 0:
    print("hello")