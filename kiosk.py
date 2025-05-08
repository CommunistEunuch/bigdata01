drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
prices = [2000, 2500, 3000, 3200]
amounts = [0] * len(drinks) #오히려 현재 코드에서는 이쪽이 더 빠를 수 있음.


total_price = 0

#할인 적용 정책 : 원
DISCOUNT_THRESHOLD = 10000 #할인이 적용되는 임계값
DISCOUNT_RATE = 0.1 #할인율

menu_texts = ""

def order_process(idx:int) -> None: #타입 힌트
    global total_price #전역 변수
    """
    주문 처리 함수 1) 주문 디스플레이 2)총 주문 금액 누산 3)수량 업데이트
    :param idx: 고객이 선택한 메뉴 -1 (index, 정수)
    :return: 없음
    """
    print(f"{drinks[idx]}를 선택하셨습니다. 가격은 {prices[idx]}원 입니다.")
    total_price += prices[idx]
    amounts[idx] += 1

def display_menu() -> str:
    """
    음료 선택 메뉴 디스플레이 함수
    :return: 음료 메뉴 및 주문 종료 문자열 (문자열)
    """
    print("="*30)
    menu_texts =''.join(f"{j+1}) {drinks[j]} {prices[j]}원\n " for j in range(len(drinks)))
    menu_texts = menu_texts + f"{len(drinks)+1} 주문 종료 : "
    return menu_texts

def print_receipt() -> None:
    """
    영수증 출력 기능
    :return: 없음
    """
    print(f"{'총 거래':^20} 내용 영수증")
    print("-------------------------------")
    for i in range(len(drinks)):
        if amounts[i] > 0:
            print(
                f"{drinks[i]:^{max(map(len, drinks)) - len(drinks[i]) + 10}} {prices[i]:^{max(map(len, drinks)) + len(drinks[i])}}원 {amounts[i]}개 :{prices[i] * amounts[i]}원")
    print("-------------------------------")

    discounted_price = discount_rate(total_price)
    discount = total_price - discounted_price

    print(f"할인 전 금액{total_price}원")
    if discount > 0:
        print(f"할인 금액{discount}원")
        print(f"할인 적용 후 지불하실 총 금액{discounted_price}원")
    else:
        print(f"할인이 적용되지 않았습니다. \n 지불하실 총 금액은 {discounted_price}입니다.")


def test() -> None :
    """
    앞으로 키오스크에 추가 할 기능
    :return: 
    """
    pass

def discount_rate(price: int) -> float :
    """
    총 금액이 임계 금액을 넘어서면 할인율 적용하는 함수
    :return 할인 적용한 금액
    """
    global DISCOUNT_THRESHOLD, DISCOUNT_RATE

    if(price > DISCOUNT_THRESHOLD):
        return price * (1-DISCOUNT_RATE)
    else:
        return price