n = int(input())
temp = []

# Reading input strings
for i in range(n):
    s = input()
    temp.append(s)

# Processing each string
for i in range(n):
    even_chars = []
    odd_chars = []
    
    # Separating even and odd indexed characters
    for j in range(len(temp[i])):
        if j % 2 == 0:
            even_chars.append(temp[i][j])
        else:
            odd_chars.append(temp[i][j])
    
    # Printing the result for each string
    print(''.join(even_chars), ''.join(odd_chars))
