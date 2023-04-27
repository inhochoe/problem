import random

chance = 10

count = 0

answer = random.randint(10, 100)
while True:
    user_input = int(input("10~100 사이의 숫자를 입력하세요:"))
    count = count + 1
    print(f'{count}회 입력하였습니다')
    if user_input > answer:
        print("down")
    elif user_input < answer:
        print("up")
    else:
        print("정답입니다")
        chance = int(input("입력횟수를 정해주세요:"))
        count = 0
        continue
    if count == chance:
        print('game over:입력횟수를 초과하였습니다')
        break
print("게임이 종료됩니다")
