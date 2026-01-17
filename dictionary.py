import random

vocab = {}


def show_menu():
    print("\n--- 영단어장 관리자---")
    print("1. 단어 추가")
    print("2. 전체 단어 보기")
    print("3. 단어 퀴즈")
    print("4. 종료")
    return input("메뉴 선택: ")


while True:
    menu = show_menu()
    if menu == "1":
        word = input("영어단어: ")
        mean = input("뜻: ")
        vocab[word] = mean
        print(f"'{word}' 단어가 추가되었습니다.")
    elif menu == "2":
        print("\n[전체 단어 목록]")
        for word, mean in vocab.items():
            print(f"{word}: {mean}")
    elif menu == "3":
        if not vocab:
            print("퀴즈를 낼 단어가 없습니다.")
            continue
        quiz_word = random.choice(list(vocab.keys()))
        answer = input(f"'{quiz_word}'의 뜻은? ")
        if answer.lower() == quiz_word.lower():
            print("정답입니다!")
        else:
            print(f"땡! 정답은 '{quiz_word}'입니다.")
    elif menu == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~4번 중 선택해 주세요.")
