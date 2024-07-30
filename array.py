import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

#indexing
print(numericArray[0])
print(numericArray[1])
print(numericArray[2])

# use of enumerate() function
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")