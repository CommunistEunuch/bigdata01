# 아아 : 2000 # 라떼 2500
import sys
#import kiosk as kk
from kiosk import print_receipt, display_menu, order_process, drinks

while(True):
    try:
        menu = int(input(display_menu()))
        if len(drinks) >= menu >= 1:
            order_process(menu-1)
        elif menu == len(drinks)+1:
            print("주문을 종료합니다.")
            break
        else:
            print(f"{menu}메뉴는 존재하지 않습니다. 다시 시도해주세요.")
    except ValueError:
        print("문자를 입력할 수 없습니다. 다시 시도해주세요")
print_receipt()
#test() #쓰지 않는 함수 방지
#print(total_price) #허용되지 않는 임포트 방지