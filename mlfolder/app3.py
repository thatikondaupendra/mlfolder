print('//while loops')
i=1
while i<=10:
    print(i*"*")
    i+=1
while i<=20:
    print(i)
    i+=1
print('//list')
name=['bharath','upendra','purushotham']
print(name[0])
print(name[-1])
print(name[-2])
print(name[0:2])
print(name)
print("//list methods")
numbers=[1,2,3,4,5]
numbers.insert(0,-1)
numbers.remove(3)
print(numbers)
print(3 in numbers)
print(len(numbers))
print('for loops')
numbers=[1,2,3,4,5]
for item in numbers:
    print(item*'8')
    for item in numbers:
        print(item*'9')
numbers=range(5)
print(numbers)
for number in numbers:
    print(number)
print('/5-10')
numbers=range(5,10)
for n in numbers:
    print(n)
numbers=range(5,10,2)
for n in numbers:
    print(n)
print('//tuples')
numbers=(1,2,3)
print(numbers.count(2))