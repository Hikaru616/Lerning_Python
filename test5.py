import time

students = [
    {'name': '田中', 'score': 85, 'subject': 'math'},
    {'name': '佐藤', 'score': 92, 'subject': 'english'},
    {'name': '鈴木', 'score': 78, 'subject': 'math'},
    {'name': '高橋', 'score': 95, 'subject': 'science'},
    {'name': '渡辺', 'score': 88, 'subject': 'english'}
]

def time_measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        v = func(*args, **kwargs)
        end_time = time.time()
        print(f"実行時間 : {end_time - start_time}")
        return v
    return wrapper

def filter_transform_func(data, condition_func, transform_func):
    return [
        transform_func(item)
        for item in data if 
        condition_func(item)
    ]

@time_measure
def process_math_students(students):
    math_condition = lambda student : student['score'] >= 80 and student['subject'] == "math"
    transform_to_string = lambda student : f"{student['name']}さん : {student['score']}点"
    return filter_transform_func(students, math_condition, transform_to_string)
    
math_results = process_math_students(students)
print(f"数学80点以上 : {math_results}")


# def decorator(f):
#     def wrapper():
#         start = time.time()
#         v = f()
#         end = time.time()
#         print(f"実行時間: {end - start}")
#         return v
#     return wrapper

# @decorator
# def high_score():
#     result = {student["name"] : student["score"] for student in students if student["score"] > 80 and student["subject"] == "math"}
#     print(f"数学80点以上{result}")
#     return result

# high_score()

        