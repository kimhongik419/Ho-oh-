from operator import truediv

# 코드 주석 처리 [컨트롤+ /]
# 콘솔창에 괄호 안에 텍스트 (문자열)을 출력하는 명령어
print("★멋있는 파이썬 배우기★")
# 변수선언
# 변수(Variable) 선언
# 변수란 값이 바뀔수있는 저장소를 의미
# 프로그래밍 언어에서 등호(=)는 등호 오른쪽의 값을 왼쪽에 저장해라 라는 의미임.

# 변수에 저장된 값을 확인
 # mirae
# 10000
fusion = 5000

print(fusion)
print(5000)

# 변수는 텍스트도 가능함
ITX="ITX-새마을"
mina = "미나"
print(mina)
print(mina)
print(ITX)

# mirae 에 5000추가하여 15000 담기
mirae = 15000
print(mirae)

navi = "네비" # navi 변수가 선언되기전에 사용 할수없음
print (navi)

# 변수의 타입 (type)
a = 10
print(a)

# 변수의 타입을 확인
# type() 괄호안에 변수를 넣으면 변수의 타입을 리턴 , 숫자는 소수점이 있거나 없거나 하는 2가지 형태가 있다.
# 정수 (integer)
print(type(a)) # class int -> 숫자 ( 정수)
# 변수 b의 타입을 콘솔에 출력하기
b = 3.14
print (b)
print(type(b)) # <class 'float'> -> 소수(float)

# 변수 C에 문자열 "몽키" 를 담고,
# 변수 C의 타입에 콘솔창에 출력하기
c="몽키"
print(type(c))
# 문자열은 문자들의 집합으로, <class 'str'> -> 영어로 string

# 불리언 타입
# 참/거짓, true/False을 나타내는 값 \
d = False # <class 'bool'> 불리언을 나타냄

print(type(d))

# 개발할때 혼동하기 쉬운 변수 타입
# 주민등록번호 앞자
e = 961028
print(type(e))

# 주민번호 앞자리 030320
# 네임태그(명칭)과 같이 사용되는 숫자값은 문자열 타입으로 사용함

# 해당 숫자를 이용해서 사칙 연산을 할것이 아니라면 문자열 타입 사용함

# 생년만 문자열로 확보한 경우
year = 1997
# 자동으로 나이계산을 해야되는 경우
# 문자열 타입과 숫자타입은 연산이 불가능하다
# 타입을 변환하고 난 뒤에 연산을 수행한다.
# str 타입의 year, int 타입으로 변환
age = 2024 - int(year)



 # 실행순서
 # age = 2024 - int(year)
 # age = 2024 - int("1993")
 # age = 2024 - 1993
 # age = 31

 # str -> int 타입이 변환되네?



# h = int(G)

#print(h)

# 오로지 숫자로만 이루어진 문자열만 int 타입으로 변환 가능함

#h = int (g)
#print (h)

# 사칙연수 +(덧셈) -(뺄셈) *(곱셈) /(나누기)

a = 10
b = 3
c = a+b
print(c)
# 실행순서
# C = a+b
# c= 10+ b
# c= 10+ 3
# c = 13
d = a-b
print (d)

print ( a/b)
print (b*a)

# 변수 a 와 변수 b 값을 더한 c에 저장, 꼭 변수를 담을 필요 없다
# HTML/CSS -> Visual studio vs코드 , 파이썬 코드 IDE


# 나머지 연산자 (%)
# 10을 3으로 나누면 나머지 1
print (a%b)

# 3을 10으로 나누면 나머지 3
print (b%a)

# 숫자형 문자열 -> int 변환
# int -> str 변환?


# 문자열 타입 + 문자열 타입  \
# 두 문자열이 합쳐진다.
apple = "사과"
banana = "바나나"
print (apple + banana)

# 기존코드와 이름충돌을 피하는 방법
v_sum = apple + banana
print (v_sum) # 사과 바나나


price = 3000
# 사과 3000
# str + int 시 애러 발생
# int -> str 변환이용
# str + str
v_sum = apple + str(price)
print(v_sum)
# v_sum = apple + str (price)
# v_sum = "사과" + str (price) # 라인복사 (컨트롤 + 알트 + 방향키아래)
# v_sum = "사과" + str (3000)
# v_sum = "사과" + str (3000)

#Pycharm -> 컨트롤 + D 라인복사
#Eclipse -> 컨트롤 + alt + 방향키
#컨트롤 + Z 실행취소
#컨트롤 + Y 실행취소반대
#컨트롤 + D 라인삭제
#vs코드 -> 다음 통일은 가능함.

# 사과: 3000 가 되도록 연산하기
ttt = ":"
print(apple + ttt + str(price))

v_sum= apple + ":" + str(price)
print(v_sum)

money = 13000
print ("money" +str(money))
print ("money:",money) # 출력될때 붙어서 출력됨

# 변수값에 사칙연산하기
# 용돈을 받아서 money에 값 추가하기
money = money + 30000
print(money)

money = money*2
print(money)
# 대입연산자방법
# money에 14000 더해라
money += 14000
print (money)
# money를 5로 나누기
money /= 5
print(money)
money /= 5
print(money)
































