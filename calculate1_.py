def start_calculator():
    print("=" * 30)
    print("   스마트 사칙연산 계산기")
    print("=" * 30)

    while True:
        try:
            num1 = float(input("\n첫 번째 숫자를 입력하세요 "))
            operator = input("연산자를 입력하세요 (+, -, *, /) ")
            num2 = float(input("두 번째 숫자를 입력하세요 "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("오류: 0으로 나눌 수 없습니다.")
                    continue
                result = num1 / num2
            else:
                print(
                    "오류: 유효하지 않은 연산자입니다. (+, -, *, / 중 하나를 사용하세요.)"
                )
                continue
            print(f"결과: {num1} {operator} {num2} = {result}")
            quit_choice = input(
                "\n계속 계산하시겠습니까? (종료하려면 'q' 입력, 계속하려면 Enter):"
            )

            if quit_choice.lower() == "q":
                print("계산기를 종료합니다. 감사합니다!")
                break
        except ValueError:
            print("오류: 유효한 숫자를 입력하세요.")
            continue


start_calculator()
