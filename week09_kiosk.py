# 아아 : 2000 # 라떼 2500
import sys
import kiosk


while(True):
    try:
        menu = int(input(kiosk.display_menu()))
        if len(kiosk.drinks) >= menu >= 1:
            kiosk.order_process(menu-1)
        elif menu == len(kiosk.drinks)+1:
            print("주문을 종료합니다.")
            break
        else:
            print(f"{menu}메뉴는 존재하지 않습니다. 다시 시도해주세요.")
    except ValueError:
        print("문자를 입력할 수 없습니다. 다시 시도해주세요")
kiosk.print_receipt()