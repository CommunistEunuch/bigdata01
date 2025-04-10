# 아아 : 2000 # 라떼
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스"]
prices = [2000, 2500, 3000]
amounts = [0,0,0]
total_price = 0
while(True):
    menu = input(f"1) {drinks[0]} {prices[0]}원 2) {drinks[1]} {prices[1]}원 3) {drinks[2]} {prices[2]}원 4) 주문 종료 : ")
    if menu == "1":
        print(f"{drinks[0]}를 선택하셨습니다. 가격은 {prices[0]}원 입니다.")
        total_price += prices[0]
        amounts[0] += 1
    elif menu == "2":
        print(f"{drinks[1]}를 선택하셨습니다. 가격은 {prices[1]}원 입니다.")
        total_price += prices[1]
        amounts[1] += 1
    elif menu == "3":
        print(f"{drinks[2]}를 선택하셨습니다. 가격은 {prices[2]}원 입니다.")
        total_price += prices[2]
        amounts[2] += 1
    elif menu == "4":
        print("주문을 종료합니다.")
        break
    else:
        print(f"{menu}메뉴는 존재하지 않습니다. 다시 시도해주세요.")


print("총 거래 내용 영수증")
print("-------------------------------")
for i in range(len(drinks)):
    print(f"{drinks[i]} {prices[i]}원 {amounts[i]}개 :{prices[i] * amounts[i]}원")
print("-------------------------------")
print(f"{total_price}원 입니다")