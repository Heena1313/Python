n= int(input("Enter the number of elements:"))
num=[]
for i in range (n):
    element=input(f"Enter element {i+1}:")
    num.append(element)
    print("The list:",num)

print("\n")
numbers=[18,45,33,77,17]
total = sum(numbers)
minimum=min(numbers)
maximum=max(numbers)
def fun():
    print("Total:",total)
    print("Maximum:",maximum)
    print("Minimum:",minimum)

fun()
print("\n")
my_tuple=tuple(numbers)
print("Tuple: ",my_tuple)
print("List: ",numbers)
numbers.append(73)

print("\n")
my_set=set(numbers)
print("My_set: ",my_set)
my_set.add(73)
my_set.add(7)
print("Elements added(73,7):",my_set)
my_set.remove(7)
print("Element removed(7):",my_set)

set1={10,4,19,20}
print("\n")
union=my_set.union(set1)
print("My_set: ",my_set)
print("Set1: ",set1)
print("Set combined: ",union)

set1.add(18)
intersection=union.intersection(set1)
print("Intersection: ",intersection)
print("\n")

my_dict={'name':'Srivalli','age':54}
print("Dictionary: ",my_dict)
print(my_dict['name'])
print(my_dict['age'])

my_dict['city']='Kakinada'
del my_dict['age']
print(my_dict.get('age','Not found'))
print('city' in my_dict)

print("Elements in dictionary:")
for key,values in my_dict.items():
    print(key,values)
