# 할 일을 저장할 빈 리스트 생성
todo_list = []

def show_menu():
    print("\n--- 할 일 목록 관리자 ---")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 삭제")
    print("4. 종료")
    return input("원하는 메뉴 번호를 입력하세요: ")

while True:
    choice = show_menu()

    if choice == '1':
        task = input("추가할 할 일을 입력하세요: ")
        todo_list.append(task)  # 리스트에 요소 추가
        print("추가되었습니다!")

    elif choice == '2':
        print("\[현재 할 일 목록]")
        if not todo_list:
            print("할 일이 비어 있습니다.")
        else:
            for index, item in enumerate(todo_list, start=1):
                print(f"{index}. {item}")

    elif choice == '3':
        if not todo_list:
            print("삭제할 항목이 없습니다.")
            continue
        
        try:
            num = int(input("삭제할 번호를 입력하세요: "))
            # 리스트 인덱스는 0부터 시작하므로 입력값에서 1을 뺍니다.
            removed = todo_list.pop(num - 1)
            print(f"'{removed}' 항목이 삭제되었습니다.")
        except (ValueError, IndexError):
            print("잘못된 번호입니다. 다시 확인해 주세요.")

    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~4번 중 선택해 주세요.")