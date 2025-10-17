def avg(marks):
    return sum(marks) / len(marks)
marks = []
for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)
average = avg(marks)

print(f"The average of the marks is: {average}")