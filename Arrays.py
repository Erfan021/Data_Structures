# ARRAYS

numbers = [1,2,3,4,5]

# random indexing --> O(1)
print(numbers[1])

numbers[1] = 200

print(numbers[1])

numbers[4] = 'Irfan'

print(numbers[4])

for num in numbers:
    print(num)
    
for i in range(len(numbers)):
    print(i)
    
print(numbers[0:2])

print(numbers[1:])

print(numbers[:-2])

numbers[4] = 6

# O(N)
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
        
print(maximum)