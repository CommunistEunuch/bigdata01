# 아아 : 2000 # 라떼 2500
import sys
import kiosk as kk


while(True):
    try:
        menu = int(input(kk.display_menu()))
        if len(kk.drinks) >= menu >= 1:
            kk.order_process(menu-1)
        elif menu == len(kk.drinks)+1:
            print("주문을 종료합니다.")
            break
        else:
            print(f"{menu}메뉴는 존재하지 않습니다. 다시 시도해주세요.")
    except ValueError:
        print("문자를 입력할 수 없습니다. 다시 시도해주세요")
kk.print_receipt()