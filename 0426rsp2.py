import random


def match_result(user_input, computer_choice):
    print(f"당신은 {user_input}을 냈습니다")
    print(f"컴퓨터는 {computer_choice}를 냈습니다")
    if user_input == "가위":
        if computer_choice == "가위":
            return ("비겼습니다")
        elif computer_choice == "바위":
            return ("졌습니다")
        else:
            return ("이겼습니다")
    elif user_input == "바위":
        if computer_choice == "가위":
            return ("이겼습니다")
        elif computer_choice == "바위":
            return ("비겼습니다")
        else:
            return ("졌습니다")
    else:
        if computer_choice == "가위":
            return ("졌습니다")
        elif computer_choice == "바위":
            return ("이겼습니다")
        else:
            return ("비겼습니다")


options = ["가위", "바위", "보"]
computer_choice = random.choice(options)

while True:
    user_input = input("가위, 바위, 보 중에서 골라주세요: ")
    if user_input in options:
        break
    else:
        print("잘못 입력하셨습니다")


result = match_result(user_input, computer_choice)
print(result)
