# 아아 : 2000 # 라떼 2500
prices = [2000, 2500]
drinks = ["아이스 아메리카노", "카페 라떼"]

while(True):
    menu = input(f"1) {drinks[0]} {prices[0]}원 2) {drinks[1]} {prices[1]}원 3) 주문 종료")
    if menu == "1":
        print(f"{drinks[0]}를 선택하셨습니다. 가격은 {prices[0]}원 입니다.")
    elif menu == "2":
        print(f"{drinks[1]}를 선택하셨습니다. 가격은 {prices[1]}원 입니다.")
    elif menu == "3":
        print("주문을 종료합니다.")
        break
