expenses = []
balance = 100000


def show_menu():
    print(f"\n--- 현재 잔액: {balance}원 ---")
    print("1. 지출 내역 추가")
    print("2. 지출 내역 보기")
    print("3. 카테고리별 통계")
    print("4. 종료")
    return input("원하는 메뉴 번호를 입력하세요: ")


while True:
    menu = show_menu()
    if menu == "1":
        item = input("항목 (예: 점심값): ")
        amount = int(input("금액 : "))
        category = input("카테고리 (식비/교통비/쇼핑/기타):")

        expenses.append({"항목": item, "금액": amount, "카테고리": category})
        balance -= amount
        print(f"'{item}' 내역이 추가되었습니다.")

    elif menu == "2":
        print("\n[지출 내역 목록]")
        for ex in expenses:
            print(f"- {ex['카테고리']} | {ex['항목']} : {ex['금액']}원")

    elif menu == "3":
        target = input("조회할 카테고리: ")
        total = 0
        for ex in expenses:
            if ex["카테고리"] == target:
                total += ex["금액"]
                print(f"\n[{target} 총 지출: {total}원]")

    elif menu == "4":
        print("프로그램을 종료합니다.")
        break
