numbers = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in numbers if x > 3]
print(squares)

result = [x if x > 0 else 0 for x in range(-2, 3)]
print(result)

words = ['apple', 'banana', 'cherry']
word_length = {word: len(word) for word in words}
print(f"単語の長さ : {word_length}")

scores = {"Alice":85, "Bob":75, "Charlie":90}
passed = {
    name : score
    for name, score in scores.items() if score > 80
}

print(passed)
import math
sqrt_set = {math.sqrt(x) for x in range(10)}
print(sqrt_set, type(sqrt_set))

text = "Hello World"
vowels = { char.lower()
         for char in text if char.lower() in "aiueo"    
}

print(vowels)

large_numbers =  (
    x**2
    for x in range(1000000) if x % 1000 == 0)

for _ in range(5):
    print(next(large_numbers))
    
print(type(large_numbers))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = (
    x for x in range(1, 100) if is_prime(x)
)

for _ in range(5):
    print(next(prime_numbers))
    
numbers = range(1, 11)
expensive_calc = [
    (n, result)
    for n in numbers
    if(result := n**2 + n*3) > 20
]

print(expensive_calc)

# text = ['apple', 'banana', 'cherry', 'pine']
# long_words = {word:length
#               for word in text
#               if(length := len(word)) > 4
#     }

text = ['apple', 'banana', 'cherry', 'pine']
long_words = { word : word_n
    for word in text if (word_n := len(word)) > 4
}

print(long_words)

sales_data = [
    {"product":"A", "price":100, "quantity":5},
    {"product":"B", "price":200, "quantity":3},
    {"product":"C", "price":300, "quantity":6}
]

# high_revenue = {
#     item["product"]: revenue
#     for item in sales_data
#     if(revenue := item["price"] * item["quantity"]) > 500
# }

# print(high_revenue)

sales_data2 = [
    {"product":"A", "price":100, "quantity":5},
    {"product":"B", "price":200, "quantity":3},
    {"product":"C", "price":300, "quantity":6}
]

high_revenue2 = {
    item["product"] : revenue2
    for item in sales_data2
    if(revenue2 := item["price"] * item["quantity"]) > 500
}

print(high_revenue2)