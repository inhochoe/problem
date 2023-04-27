import random

answer = random.randint(0, 100)
while True:
    user_input = int(input())
    if user_input > answer:
        print("down")
    elif user_input < answer:
        print("up")
    else:
        print("정답입니다")
        break
print("게임이 종료됩니다")
