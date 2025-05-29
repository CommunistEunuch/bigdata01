import datetime as datetime
import sqlite3
from cgi import print_form

import requests

drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
prices = [2000, 2500, 3000, 3200]
amounts = [0] * len(drinks) #오히려 현재 코드에서는 이쪽이 더 빠를 수 있음.
# url = ("http://wttr.in/suwon?format=%C++%t&lang=ko")
url = ("https://wttr.in/suwon?format=2")
total_price = 0

#할인 적용 정책 : 원
DISCOUNT_THRESHOLD = 10000 #할인이 적용되는 임계값
DISCOUNT_RATE = 0.05 #할인율

menu_texts = ""

def run() -> None:
    """
    키오스크 실행(구동) 함수
    :return: None
    """
    while True:
        try:
            menu = int(input(display_menu()))
            if len(drinks) >= menu >= 1:
                order_process(menu - 1)
            elif menu == len(drinks)+1:
                print("주문을 종료합니다")
                break
            else:
                print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
        except ValueError:
            print(f"문자를 입력할 수 없습니다. 숫자를 입력해주세요")


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
    print(get_weather_info())
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
        print(f"할인 금액{discount}원 ({DISCOUNT_RATE*100}% 할인)")
        print(f"할인 적용 후 지불하실 총 금액{discounted_price}원")
    else:
        print(f"할인이 적용되지 않았습니다. \n 지불하실 총 금액은 {discounted_price}입니다.")
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

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

def print_ticket_number() -> None:
    """
    주문 번호표 출력 함수
    :return: None
    """
    conn = sqlite3.connect('cafe.db')  # db instance open
    cur = conn.cursor()
    cur.execute('''
        create table if not exists ticket (
        id integer primary key autoincrement,
        number integer not null,
        created_at text not null default (datetime('now','localtime'))
        )
    ''')

    cur.execute('select number from ticket order by number desc limit 1')
    result = cur.fetchone()

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if result is None:
        number = 1
        cur.execute('insert into ticket (number, created_at) values (?,?)', (number,now))
    else:
        number = result[0] + 1
        cur.execute('insert into ticket (number, created_at) values (?,?)', (number,now))

    conn.commit()

    print(f"번호표 : {number}")

def get_weather_info() -> str:
    """
    날씨 정보 (https://wttr.in)
    :return:
    """
    try:
        response = requests.get(url)
        if response.status_code == 200 :
            #print(response.text.strip())
            return  response.text.strip()
        else :
            #print(f"상태 코드 {response.status_code}")
            return f"상태 코드 {response.status_code}"
    except Exception as e :
        #print(e)
        return e