import datetime

def create_diary():
    # 현재 날짜와 시간 가져오기
    now = datetime.datetime.now()
    
    # 일기 제목 입력 받기
    title = input("일기 제목을 입력하세요: ")
    
    # 일기 내용 입력 받기
    print("일기 내용을 입력하세요. 작성을 완료하려면 빈 줄에서 Enter 키를 누르세요.")
    content = ""
    while True:
        line = input()
        if line == "":
            break
        content += line + "\n"
    
    # 파일 이름 생성 (날짜와 제목을 이용)
    filename = now.strftime("%Y-%m-%d") + "-" + title + ".txt"
    
    # 파일에 일기 내용 저장
    with open(filename, 'w') as file:
        file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write("제목 : " + title + "\n")
        file.write(content)
    
    print("일기가 저장되었습니다.")

# 일기장 생성 함수 호출
create_diary()
