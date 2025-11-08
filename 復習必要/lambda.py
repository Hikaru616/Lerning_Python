# f = lambda x: x + 10
# print(f(3))

f = lambda x, y: x + y

print(f(7, 9))

r = lambda x: "even" if x % 2 == 0 else "odd"
print(r(5))

a = lambda x, y = 2: x ** y
print(a(3))
print(a(3, 4))

def process_number(numbers, func):
    for number in numbers:
        print(func(number))
        
numbers = list(range(5))
process_number(numbers, lambda x: x + 3)