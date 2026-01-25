def analyze_diary():
    print("\n" + "=" * 35)
    print("--- 인공지능 감정 분석 일기장 (Lite) ---")
    print("=" * 35)

    content = input("오늘 하루는 어땠나요? 자유롭게 적어주세요:\n> ")

    # '뿌리' 단어만 등록하면 "기쁘다", "기쁨", "기뻤어"를 모두 찾아냅니다.
    good_roots = [
        "행복",
        "기쁘",
        "즐거",
        "사랑",
        "성공",
        "감사",
        "뿌듯",
        "최고",
        "웃음",
    ]
    bad_roots = ["슬프", "화나", "짜증", "실망", "후회", "외롭", "우울", "최악", "실패"]

    score = 0
    # 문장 안에 감정의 뿌리가 포함되어 있는지 검사 (자바 없이 가능!)
    for root in good_roots:
        if root in content:
            score += 1
    for root in bad_roots:
        if root in content:
            score -= 1

    print(f"\n[분석 결과] 점수: {score}점")
    if score > 0:
        print("참 긍정적인 하루였네요! 😊")
    elif score < 0:
        print("조금 힘든 날이었군요. 기운 내세요! ☕")
    else:
        print("평온한 하루였네요. 🌿")


analyze_diary()
