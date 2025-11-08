import time

def after(seconds, func):
    time.sleep(seconds)
    func()
    
def greeting(msg):
    def inner():
        print(msg)
    return inner
    
greet = greeting('Hello World')
aaa = greeting('aaa')
# after(3, greet)
# after(2, aaa)

def process_number(number, even_callback, odd_callback):
    if number % 2 == 0:
        even_callback(number)
    else:
        odd_callback(number)
        
def handle_even(number):
    print(f"{number}は偶数です")
    
def handle_odd(number):
    print(f"{number}は奇数です")
    
process_number(9, handle_even, handle_odd)