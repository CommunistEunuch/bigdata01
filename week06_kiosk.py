# 아아 : 2000 # 라떼 2500

def order_process(idx):
    global total_price
    """
    주문 처리 함수 1) 주문 디스플레이 2)총 주문 금액 누산 3)수량 업데이트
    :return: 없음
    """
    print(f"{drinks[idx]}를 선택하셨습니다. 가격은 {prices[idx]}원 입니다.")
    total_price += prices[idx]
    amounts[idx] += 1


total_price = 0

drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스"]
prices = [2000, 2500, 3000]
amounts = [0,0,0]

menu_texts = ""

for j in range(len(drinks)):
    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]}원 "
menu_texts = menu_texts + f"{len(drinks)+1})주문 종료 :"

while(True):
    menu = int(input(menu_texts))
    if len(drinks) >= menu >= 1:
        order_process(menu-1)
    elif menu == len(drinks)+1:
        print("주문을 종료합니다.")
        break
    else:
        print(f"{menu}메뉴는 존재하지 않습니다. 다시 시도해주세요.")


print("총 거래 내용 영수증")
print("-------------------------------")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]}원 {amounts[i]}개 :{prices[i] * amounts[i]}원")
print("-------------------------------")
print(f"{total_price}원 입니다")