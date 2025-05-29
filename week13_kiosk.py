import kiosk as kk
import requests

if __name__ == "__main__":
    # url = ("http://naver.com/suwon?format=%C++%t&lang=ko") # 존재하지 않는 도메인이라  request가 존재
    # url = ("http://wttr123.in/suwon?format=%C++%t&lang=ko") # 존재하지 않는 서버
    url = ("http://wttr.in/suwon?format=%C++%t&lang=ko")
    try:
        response = requests.get(url)
        if response.status_code == 200 :
            print(response.text.strip())
        else :
            print(f"상태 코드 {response.status_code}")

    except Exception as e :
        print(e)
    kk.run()
    kk.print_receipt()
    kk.print_ticket_number()