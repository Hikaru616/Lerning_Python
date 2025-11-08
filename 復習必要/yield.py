def generator():
    yield 1
    print('aaa')
    yield 2
    print('bbb')
    yield 3
    print('ccc')
    
gen = generator()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)
    
def print_num(max):
    print('ジェネレーター作成')
    for n in range(max):
        print(f'n: {n}')
        yield n
    
gen = print_num(10)
for i in gen:
    print(f'i: {i}')
    
import sys

N = 10**6

def get_list():
    for i in range(N):
        yield i
    # return [i for i in range(N)]

list = get_list()
print(sys.getsizeof(list), 'bytes')