# # # # # # # # # # print("오늘 파이썬 첫날^^\\")
# # # # # # # # # #주석이란?
# # # # # # # # # #주석은 컴퓨터에게 명령을 전달하는 내용에서 예외처리하는 문법이다
# # # # # # # # # #문서편집기에 작성은 하지만 컴퓨터가 번역을 해서 실행할 때 제외된다
# # # # # # # # # #주석은 크게 행(줄)주석과 블럭 주석으로 나뉘게 된다
# # # # # # # # # #행주석은 #기호 뒤에 모두 주석처리된다.
# # # # # # # # # #단 줄이 바뀌면 해제된다
# # # # # # # # # #블럭주석은 ''' 따옴표 3개로 시작지점을 표기하고 ''' 다시 끝부분에 닫아준다
# # # # # # # # # #따옴표와 따옴표 사이가 하나의 블럭으로 지정되며 모두 예외처리된다.
# # # # # # # # # print("hello")#주석은 그 행의 설명을 다는 용도로 사용되거나
# # # # # # # # # #이렇게 불필요한 코드를 예외처리할 때 사용된다 print("hello")
# # # # # # # # # #코딩을 하면서 작성한 코드는 지우지 않아야 합니다
# # # # # # # # # print("python 첫날입니다")
# # # # # # # # # print("python을 시작해 볼까요")
# # # # # # # # #주석 단축키
# # # # # # # # #ctrl + / (주석이 설정/해제 스위칭됨)
# # # # # # # # #ctrl + k + c (주석이 누적 적용됨)
# # # # # # # # #ctrl + k = u (주석이 누적 해제됨)
# # # # # # # # print("쌍따옴표 안의 내용 출력"); print("이어쓰기실행")
# # # # # # # # #일반적으로 코드는 한줄에 하나의 명령을 작성하는 것이 바람직하다
# # # # # # # # # -가독성이 떨어진다
# # # # # # # # # -에러가 발생할 경우 에러의 위치가 명확하지 못하다
# # # # # # # # #한줄에 여러개의 명령을 작성할 경우 ;으로 구분지어야 한다
# # # # # # # # #한줄에 간단히 표현되면서, 서로 연관성이 있을 경우 한줄에 여러개를 작성하기도 한다.
# # # # # # # # #SyntaxError: 문법 오류
# # # # # # # # print("이어쓰기"); print(); print(";(세미콜론이라 읽는다)")
# # # # # # # # #이스케이프문자
# # # # # # # # print("Hello"
# # # # # # # # "Python"
# # # # # # # # "Start")
# # # # # # # # print("hello\n"
# # # # # # # # " Python\n"
# # # # # # # # " Start")
# # # # # # # print("저의 이름은 홍길동입니다\n""저의 나이는 20살입니다\n""주소는 산골자기입니다")
# # # # # # # print("저의 이름은 홍길동입니다\n저의 나이는 20살입니다\n주소는 산골자기입니다")
# # # # # # print("123456781234567812345678123456781234567812345687")
# # # # # # print("Have\ta\t\tGood\tTime.")
# # # # # # print("124567\t"
# # # # # # "1\t"
# # # # # # "12345678\t"
# # # # # # "123")
# # # # # # print("대한민국\t만세\t대한독립\t만만세")
# # # # # print("쌍따옴표\"")
# # # # # print("훗 따옴표 '")
# # # # # print('쌍따옴표"')
# # # # # print('훗따옴표\'')
# # # # print("영희야 안녕")
# # # # print('"영희야 안녕"')
# # # # print("\"영희야 안녕\"")
# # # print('표현 \ 방식')
# # # print('표현 \2 방식')
# # # print('표현 \\2 방식')
# # # #print('표현 방식\') #SyntaxError: EOL while scanning string literal
# # # print('표현 방식\\')
# # print("========================\n\t/)/)\n\t( ..)\n\t( >♡\n    Have a good Time.\n========================")
# print("\t### 회비 정보 ###")
# print("="*40)
# print("이름\t나이\t전화번호\t회비")
# print("="*40)
# print("홍길동\t\"15\"\t010-123-1234\t\\20,000")
# print("임꺽정\t\"20\"\t010-234-2345\t\\30,000")
# print("김말이\t\"28\"\t010-345-3456\t\\50,000")
# print("-"*40)
# print("총합계\t\t\t\t\\100,000")
# print("="*40)