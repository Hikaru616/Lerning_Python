import time

def decorator_func(func):
    def wrap():
        start = time.time()
        print("Hello")
        func()
        end = time.time()
        print(end - start)
    return wrap

@decorator_func
def introduce():
    print("World")
    
# introduce()

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        result = func(*args, **kwargs)
        print(f"完了: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

# print(add(2, 3, name = "ABC"))


def time_log_decorator(f):
    def wrapper(*arg, **kwarg):
        start_time = time.time()
        print(arg, kwarg)
        v = f(*arg, **kwarg)
        end_time = time.time()
        print(end_time - start_time)
        print(f'結果 : {v}')
        return v
    return wrapper
        
@time_log_decorator
def calculator(a, b):
    for _ in range(5):
        a += b
    return a

# calculator(3, 5)


def repeat(times):
    def decorator(f):
        def wrapper(*arg, **kwarg):
            start_time = time.time()
            v = f(*arg, **kwarg)
            for _ in range(times):
                v += v
            end_time  = time.time()
            print(end_time - start_time)
            print(f"結果: {v}")
            return v
        return wrapper
    return decorator

@repeat(5)
def caluclator2(a, b):
    for _ in range(b):
        a += b
    return a

# caluclator2(3, 5)


def greetCount(f):
    count = 0
    def wrapper(*arg, **kwarg):
        nonlocal count
        count += 1
        print(f"呼び出し{count}回目")
        v = f(*arg, **kwarg)
        return v
    return wrapper

@greetCount
def greet():
    print("hello")
    
greet()
greet()
greet()