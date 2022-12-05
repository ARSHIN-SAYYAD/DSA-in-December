myarr = []
n = int(input("How many no.s do u want to sort? "))


for i in range(n):
    x= int(input("Enter the number : "))
    myarr.append(x)
    

print("Unsorted array : ")
print(myarr)


def insertionSort(myarr):
    j = 0
    
    for i in range(1,n):
        key = myarr[i]
        j = i - 1

        while (j>=0 and myarr[j] > key):
            myarr[j + 1] = myarr[j]
            j = j - 1

        myarr[j + 1] = key



insertionSort(myarr)

print("\nSorted array :")
print(myarr)

'''
for i in range(len(myarr)):
    print(myarr[i], end=" ")
'''