# Task 1
def is_sorted(arr:list[int])-> bool:
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
        
    return True
 
lst = []
 

n = int(input("Enter number of elements : "))
 

for i in range(0, n):
    ele = int(input())
    
    lst.append(ele)  
 
print(lst)

print(is_sorted(lst))

#Task 2
def number_of_bread(bread:int):
    total=3.49*bread
    dis=total*0.06
    pay=total-dis

    return total,pay
n=int(input("enter how much breads do you want"))
print(number_of_bread(n))
























        

    







