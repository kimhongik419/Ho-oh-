# 배열
# 1. 파이썬에서 기본적으로 제공하는 배열( 기능이 적음)
# 2. 다른사람이 만든 배열 라이브러리 사용 ( 기능이 많고 복잡함)

# 로또 번호 7자리를 변수에 담겠다.
num1 = 7
num2 = 15
num3 = 19
num4 = 23
num5 = 27
num6 = 32
num7 = 45


# 7개의 숫자를 한곳에 담아서 처리하면 편하지 않을까?
# 배열의 탄생
lotto = [] # []비어있는 배열을 의미함


# lotto는 배열을 담고 있는 변수가 됨
# 내부에 값을 추가하는 함수를 가지고 있음
lotto.append(7) # -> 해당값을 배열에 넣어라
lotto.append(13)
lotto.append(25)
lotto.append(8)
lotto.append(20)
station = "탄방역"

print(lotto) # 배열은 순서가 보장됨

# 배열의 길이 확인 (값이 몇개 들어있는지)
print("배열의 길이:",len(lotto)) # -> 5개가 리턴됨

# 배열의 인덱싱, 슬라이싱

print(lotto[1]) # 13
print(lotto[0:3]) # 7,13,25
print(lotto[1:2]) # 13

# 배열  값  모두 제거
#lotto.clear() -> 빈배열이 됨.....

# 배열 값 제거
#lotto.pop(7) # 지우고자하는 인덱스 번호 입력

# 배열값제거
#lotto.remove (25) # 지우고자하는 값을 제거
lotto.clear()
lotto=[23,10,7,5,21,30]
print(lotto)

# 8 9 18 35 39 45
# 8 15 19 21 32 36

# 배열을 정렬하기
lotto.sort() # 오름차순 (값이 갈수록 커짐) 정렬이 이루어짐
print(lotto)


print("최솟값:", lotto [0]) # 최솟값 (로또)
lotto.sort( reverse = True) # 내림차순 정렬이 일어남
print(lotto)

lotto2 = [34,12,15,7,43,23]
# lotto 와 lotto2에 대해 각각 최솟값 최대값

print("최댓값:",lotto [0]) # 최대값 (로또)

lotto2.sort()
print("최솟값:", lotto2 [0]) # 최솟값 (로또2)

lotto2.sort(reverse = True)
print("최댓값:", lotto2 [0]) # 최대값 (로또2)

# 배열의 오름차순를 정렬한후 배열의 첫번째 값 꺼내기 (최소값)
#배멸의 마지막 값 꺼내기 (최대값)
# 배열의 오름차순 정렬 시키기
# lotto2.sort()
# 배열의 첫번째 값 꺼내
# print("최솟값", lotto2[0])
# 배열의 마지막 값 꺼내
# print("최댓값", lotto2[-1])

# 2차원 데이터를 나눈다면?
# 로또용지 (5000원) - 5줄
lotto1 = [2,7,14,15,18,20]
lotto2 = [5,9,16,25,28,44]
lotto3 = [4,7,24,25,38,41]
lotto4 = [6,12,14,25,33,38]
lotto5 = [3,8,17,21,23,37]

lotto = []
lotto.append(lotto1)
lotto.append(lotto2)
lotto.append(lotto3)
lotto.append(lotto4)
lotto.append(lotto5)

print(lotto)
print(lotto[1]) # = lotto2
print(lotto[2]) # = lotto3
print(lotto2[2]) # 로또 2의 값 16이 리턴됨
print(lotto[1][2]) # 인덱스1의 배열의 꺼낸후, 해당 배열의 인덱스 2번의 값을 구한다.

# 로또용지 (5줄) 3장 - 3차원데이터

books = "이것이자바다,자바의정석,데이터경영론"
# ["이것이자바다,자바의정석,데이터경영론"] -> 하나의배열에 담는것이 훨씬 편리하다 다루기 쉽다.
books.split(",")
print(books)
# booksArray = books.split(",")
# booksArray = ["이것이자바다","자바의정석","데이터경영론"]


koreatrain = ["ITX-새마을,ITX-마음,무궁화호,새마을호,ITX-청춘,KTX,KTX-산천,KTX-이음,KTX-청룡,SRT,누리로"]

koreatrain.split














