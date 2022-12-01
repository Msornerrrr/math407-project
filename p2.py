import matplotlib.pyplot as plt

## print first n Champernowne number
# @precondition: n >= 0
def Champernowne(n):
    str = ""
    for i in range(0, n):
        str += bin(i)[2:]
    return str

## print first n Copeland-Erdos
# @precondition: n >= 0
def Copeland_Erdos(n):
    str = "01"
    primeList = []
    i = 2
    while n != 0:
        # skip all composite numbers
        for j in primeList:
            if i % j == 0:
                i += 1
                continue

        str += bin(i)[2:]
        primeList.append(i)
        i += 1
        n -= 1
    return str
            
## determine the 
def ratio(sequence):
    count_0 = 0
    count_1 = 0
    for digit in sequence:
        if digit == '1':
            count_1 += 1
        elif digit == '0':
            count_0 += 1
    
    if count_0 == 0:
        return count_1
    return count_1 / count_0

## 
n = 40000
index_list = []
Champernowne_list = []
Copeland_Erdos_list = []

i = 8
while i < n:
    str1 = Champernowne(i)
    str2 = Copeland_Erdos(i)
    index_list.append(i)
    Champernowne_list.append(ratio(str1))
    Copeland_Erdos_list.append(ratio(str2))
    i *= 2

# str = Champernowne(10000)
# print(ratio(str))

plt.plot(index_list, Champernowne_list, 'b')
plt.plot(index_list, Copeland_Erdos_list, 'g')
plt.show()