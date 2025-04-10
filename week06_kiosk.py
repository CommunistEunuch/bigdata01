# 아아 : 2000 # 라떼 2500
prices = [2000, 2500]
drinks = ["아이스 아메리카노", "카페 라떼"]
amounts = [0,0]
total_price = 0
#order_list = ""
while(True):
    menu = input(f"1) {drinks[0]} {prices[0]}원 2) {drinks[1]} {prices[1]}원 3) 주문 종료 : ")
    if menu == "1":
        print(f"{drinks[0]}를 선택하셨습니다. 가격은 {prices[0]}원 입니다.")
        total_price += prices[0]
        amounts[0] += 1
        #order_list += order_list + drinks[0] +'\n'
    elif menu == "2":
        print(f"{drinks[1]}를 선택하셨습니다. 가격은 {prices[1]}원 입니다.")
        total_price += prices[1]
        amounts[1] += 1
        #order_list += order_list + drinks[1] +'\n'
    elif menu == "3":
        print("주문을 종료합니다.")
        break
    else:
        print(f"{menu}메뉴는 존재하지 않습니다. 다시 시도해주세요.")

#print(f"{order_list}")
print(f"{drinks[0]} {prices[0]}원 {amounts[0]}개 :{prices[0] * amounts[0]}원")
print(f"{drinks[1]} {prices[1]}원 {amounts[1]}개 :{prices[1] * amounts[1]}원")
print(f"{total_price}원 입니다")