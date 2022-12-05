from array import *


myarr = array('i',[])
n = int(input("How many no.s do you want to sort?  "))

for i in range(n):
   x = int(input("Enter the number : "))
   myarr.append(x)

print("\nUnsorted array : ")
for i in range(len(myarr)):
   print(myarr[i],end=" ") 

def selectionSort(myarr):
   
   for i in range(0,n-1):
      min = i

      for j in range(i+1,n):
         if(myarr[j] < myarr[min]):
            min = j

      if(min != i):
         myarr[min], myarr[i] = myarr[i], myarr[min]
        


selectionSort(myarr)

print("\n\nSorted array : ")
for i in range(len(myarr)):
   print(myarr[i],end=" ") 

print("\n")

