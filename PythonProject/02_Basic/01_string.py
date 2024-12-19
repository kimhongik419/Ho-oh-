#.start.py를 실행해서 메모리에 저장되었던 변수 등은
#.start.py의 실행이 끝나면 모두 사라짐
#print (money)
# 01_string.py 를 실행하면 start.py는 전혀 실행되지 않음
# 문자열 가지고 놀기
station = "정부청사역, 시청역, 탄방역"
print (station)
# 자동완성 단축키 ( 컨트롤 + 스페이스)
# 값이 나열되는것이 배열임.
# 문자열 = 문자들의 배열
# 글자수 확인
# length의 약자를 써서 len() 사용
print(len(station))

# 문자열의 인덱스 (넘버링)을 이용하여 특정 문자를 꺼내는 것.
print(station[1])
print(station[3])

# 어떤 문자열이든 첫번째 문자만 꺼내겠다.
stuA="ITX-마음"
stuB="무궁화호"
stuC="아이티엑스새마을호"



print(stuA[0])
print(stuB[0])
print(stuC[0])

# 어떤 문자열이든 마지막 문자만 꺼내겠다.
# stuA 의 마지막 문자의 인덱스 보고 결정한다. 글자수-1 (공백 모두 포함)

stuX = "김하얀푸른하늘꽃"
last = len(stuX) - 1

print(stuA[1])
print(stuB[3])
print(stuC[8])
print(stuX[7])
print(last)
print(stuX[last])
# 코드 자동 정렬 (포멧팅) 단축키 (컨트롤+shift+F) \
# -> 마지막 인덱스 번호를 알수가 있다. LEN -> 빼기 해주면 됨.
print(stuA[len(stuA) - 1])
print(stuB[len(stuB) - 1])

# 파이썬은 거꾸로 인덱스 번호를 부여해놓음
print(stuA[-1])
print(stuB[-1])
print(stuC[-5])

print(station[7])
print(station[-8])

# 문자열 내 특정 문자의 인덱스 번호 찾기
print(station.find("시")) #-> 해당 변수에서, 원하는 텍스를 어디의 인덱스 번호를 찾아줌
print(station.index("시"))

# 존재하지 않는 문자를 찾는 경우 차이점이 존재
print(station.find("응")) # -1 = 없다는 뜻
# 애러가 발생하면 프로그램의 동작이 멈춤
# 애러처리를 해주면 프로그램이 멈추지 않음
print("애러 처리 구문") # 애러가 발생하면 실행, 애러가 발생 안되면 실행x

print("재미있는 파이썬")

# 문자열에서 인덱스 번호를 이용해서 특정문자를 꺼내는 것을 인덱싱이라고 함,
print(station[3])

# 인덱스 번호를 이용해서 여러개의 문자를 꺼내는 것을 슬라이스 라함.
# 정부청사역은 인덱스 0,1,2,3,4
print(station[0:4]) # 0~3까지에 해당됨
print(station[0:5]) # 0~4까지에 해당됨

# 슬라이스에서 시청역 출력하기
print(station[7:10])

print(station[7:]) # 끊어야 곳이 적혀있지 않으므로 시청역부터 끝까지 표현됨

print(station[:10]) # 처음부터 10번까지 표현됨

# 변수 이름 짓는 방식

name = "정찬웅"

# 마나 포인트 (mana point)
# 1. 스네이크 방식
mana_point = 50

# 2. 카멜방식
manaPoint = 50

# 3. 요약방식 (Database 컬럼명에 자주 보임)
mp= 50





