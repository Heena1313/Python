
a=int (input("Enter a weight in kg:"))
p=a*2.20
print(f"{a}kg in equal to {p} pounds")

for i in range(8,90,3):
    print(i,end=" ")
    
str="Programming"
list=list(str)
print(list)


arr=[1,3,5,7]
max(arr)

def fibonacci_loop(n):
   a, b = 0, 1
   for _ in range(n):
       print(a, end=" ")
       a, b = b, a + b
     
fibonacci_loop(10) 