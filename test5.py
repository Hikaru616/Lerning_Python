import time

students = [
    {'name': '田中', 'score': 85, 'subject': 'math'},
    {'name': '佐藤', 'score': 92, 'subject': 'english'},
    {'name': '鈴木', 'score': 78, 'subject': 'math'},
    {'name': '高橋', 'score': 95, 'subject': 'science'},
    {'name': '渡辺', 'score': 88, 'subject': 'english'}
]

def decorator(f):
    def wrapper(*arg, **kwarg):
        start = time.time()
        v = f(*arg, **kwarg)
        end = time.time()
        print(f"実行時間: {end - start}")
        return v
    return wrapper

@decorator
def high_score():
    result = {student["name"] : student["score"] for student in students if student["score"] > 80 and student["subject"] == "math"}
    # print(f"数学80点以上{result}")
    return result

high_score()
    

        