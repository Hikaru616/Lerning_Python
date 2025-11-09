list_a = [1, 2, 3, 4, 5]
map_a  = map(lambda x : x**2, list_a)
map_b = (x**2 for x in list_a)

print(map_a)
print(list(map_a))
print(list(map_b))


map_c = (x**2 for x in list_a)

man = {
    "name" : "Ichiro",
    "age" : "18",
    "country" : "Japan"
}

# map_man = map(lambda x : x + ',' + man.get(x), man)

map_man = (x + ',' + man.get(x) for x in man)

print(list(map_man))

def calculate(x, y, z):
    if z == 'plus':
        return x + y
    elif z == 'minus':
        return x - y
    
map_sample = map(
    calculate, range(5), [5,5,5,5,5], ['plus', 'minus', 'plus', 'minus', 'plus']
)
import random
map_sample2 = [
    calculate(x, y, random.choice(['plus', 'minus'])) for x, y in zip(range(5), [5,5,5,5,5])
]

print(list(map_sample))
print(list(map_sample2))

map_sample3 = [
    calculate(x, y, z) for x, y, z in zip(range(5), [1, 2, 3, 4, 5], ['plus','minus','plus','minus','plus'])
]

print(list(map_sample3))