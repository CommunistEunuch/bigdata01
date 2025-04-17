# 아아 : 2000 # 라떼 2500
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
prices = [2000, 2500, 3000, 3200]
#amounts = [0 for _ in range(len(drinks))] # 리스트 컴프리헨션 (리스트 축약) 가독성을 위해 _ 사용
amounts = [0] * len(drinks) #오히려 현재 코드에서는 이쪽이 더 빠를 수 있음.


total_price = 0


menu_texts = ""
def order_process(idx):
    global total_price #전역 변수
    """
    주문 처리 함수 1) 주문 디스플레이 2)총 주문 금액 누산 3)수량 업데이트
    :param idx: 고객이 선택한 메뉴 -1 (index, 정수)
    :return: 없음
    """
    print(f"{drinks[idx]}를 선택하셨습니다. 가격은 {prices[idx]}원 입니다.")
    total_price += prices[idx]
    amounts[idx] += 1

def display_menu():
    """
    음료 선택 메뉴 디스플레이 함수
    :return: 음료 메뉴 및 주문 종료 문자열 (문자열)
    """
    print("="*30)
    menu_texts =''.join(f"{j+1}) {drinks[j]} {prices[j]}원\n " for j in range(len(drinks)))
    menu_texts = menu_texts + f"{len(drinks)+1} 주문 종료 : "
    return menu_texts

#for j in range(len(drinks)):
#    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]}원 "
#menu_texts = menu_texts + f"{len(drinks)+1})주문 종료 :"



while(True):
    menu = int(input(display_menu()))
    if len(drinks) >= menu >= 1:
        order_process(menu-1)
    elif menu == len(drinks)+1:
        print("주문을 종료합니다.")
        break
    else:
        print(f"{menu}메뉴는 존재하지 않습니다. 다시 시도해주세요.")


print(f"{'총 거래':^20} 내용 영수증")
print("-------------------------------")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]:^{max(map(len,drinks))-len(drinks[i])+10}} {prices[i]:^{max(map(len,drinks))+len(drinks[i])}}원 {amounts[i]}개 :{prices[i] * amounts[i]}원")
print("-------------------------------")
print(f"{total_price}원 입니다")