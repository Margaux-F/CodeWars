# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

#First program

def SumSquare(List):
    for term in List:
        term = (int(input("Enter a term : ")))**2
    return sum(List)


#Or :

def square_sum(numbers):
    for i in range(len(numbers)):
        numbers[i] = (numbers[i])**2
    return sum(numbers)

#Or : 

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

#Or with a map and a lambda functions : 

def square_sum(numbers):
    return (sum(map(lambda x: x ** 2, numbers)))    # map(lambda item: item[] expression, iterable) et on somme le tout avec sum()

print(square_sum([1,2]))

