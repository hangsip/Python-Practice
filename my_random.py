import random
random_number = random.randint(1,100)
attempts = 0
print("숫자 맞추기 게임에 오신 것을 환영합니다!")
print("1부터 100 사이의 숫자 중 하나를 맞춰보세요.") 

while True:
    user_input = input("숫자를 입력하세요: ")
    a = int(user_input)  
    attempts += 1
    if a < random_number:
        print("up! 더 큰 숫자입니다.")
    elif a > random_number:
        print("down! 더 작은 숫자입니다.")
    else:
        print(f"정답입니다! {attempts}번 만에 맞히셨네요.")
        break 