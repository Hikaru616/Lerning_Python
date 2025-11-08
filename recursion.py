# def factorial(n):
#     if n <= 1 :
#         return 1
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result

# print(factorial(5))


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))