# 반복문

# 콘솔창에 Hello를 10번 출력
for i in range (0, 10): # 0에서 9까지를 해당됨
    print ("Hello")
# range ( 0,10) 는 배열 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10))) # 배열 범위를 볼수있다.

for i in [0,1,2,3,4,5,6,7,8,9]:
    print("Hello")

# 콘솔창에 1부터 10까지 출력
# 반복문을 이용하는 가장 큰 이유 -> 중복코드 합치기
for i in range(1,11):
    print(i)

numArray = [2,5,3,4]
for i in numArray: # 일반 배열도 in 옆에 사용가능
    print(i)

stuArray = ["김호빵","이찐빵","박꿀빵"]
for i in stuArray:
    print(i)

# numArray의 모든 값에 3을 곱하기
print(numArray * 3) # [2, 5, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4]

# 배열 내 값 수정
print(numArray)  # [2, 5, 3, 4]
print(numArray[0]) # 2
print(numArray[0] * 3) # 6

numArray [0] = numArray [0] * 3
print(numArray[0]) # 6

numArray[1] = numArray [1] * 3
print(numArray[1])

numArray[2] = numArray [2] * 3
print(numArray[2])

numArray[2]  *= 3
numArray[3]  *= 3 # 대입연사자도 가능하며 위와 같은 값이 나온다.
print(numArray)

numArray = [2,5,3,4]
print(numArray)
# for 문으로 바꿔보기
numArray[0]  *= 3
numArray[1]  *= 3
numArray[2]  *= 3
numArray[3]  *= 3
print(numArray)

numArray = [2,5,3,4,8,9]


# i를 0,1,2,3 이 되도록하는 for문을 만들어주면 됨.
for i in range (0,len(numArray)): # numArray를 주면 됨 자동으로 반영됨. # 0~5
    numArray[i] *=3

print(numArray)

# 다른 사람이 만든 배열 라이브러리 numpy 라이브러리 사용
# numpy 라이브러리 불러오기
import numpy as np # as는 alias(별칭)의 약자

numArray = [2,5,3,4]
npArray = np.array([2,5,3,4])

print(numArray)
print(npArray)
print(type(numArray)) # <CLASS 'list'>
print(type(npArray)) # <CLASS 'numpy.ndarray'>

print(npArray  * 3 )
npArray = npArray * 3
print(npArray)

npArray *=3
print(npArray)
# 1부터 10까지 다 더하면?
# n(n+1)/2
# 10(10+1)/2
# i가 1부터 100까지 되도록 for 문 만들기
sum = 0
for i in range (20,41):
    sum += i
print(sum)

# 5 팩토리얼 값 5*4*3*2*1
# 10 팩토리얼 1*2*

Train = 1

for i in range (1,11):
    Train *= i

print(Train)

mul = 1
for i in range (1,11):
    mul *= i

print(mul)

# range로 거꾸로 배열 생성
for i in range (10, 0, -1):
    print(i)

# 1부터 30까지 숫자 중 홀수만 출력
# i가 1부터 30이 되도록 for문 생성 (=조건체크 -> 조건문 사용)

for i in range(1,31):
   if i % 2 == 1:
       print(i)


# 30부터 60까지 숫자 중 짝수만 다 더하면
sum = 0
for i in range(30,61):
    if i % 2 == 0:
         sum += i

print(sum)

# range 의 범위 조정
sum = 0
for i in range (30,61,2): # [30,32,34,36,38 ... 60] 2씩 증가 , 배열생성
    sum += i
print(sum)

# 어떻게 해야되나 이렇게 못해서야 원...
NameArray = ["김호빵","이찐빵","박꿀빵","김식빵","김붕어빵"]
sum = 0
for i in NameArray:
    print(i)
    fst=i[0]
    print(fst)
    if fst == "김":
        sum += 1

print(sum)

#*
#**
#***
#****
#*****
# 와 같이 출력되도록 반복문을 작성하기
# 빈 문자열(empty) 선언
star = ""
# 5번을 반복하는 for문 선언
for i in range(0,6):
    star += "*" # star = star + "*"
    print(star)
    # for 문이 반복될때마다 star에 "*" 를 추가한 후 출력

# 콘솔창에
# *****
# ****
# ***
# **
# *


for i in range (5,0,-1):
    print(star[0:i])


for i in range(5): # [0,1,2,3,4]
                   # # = 1,2,3,4,5
                   # ? = 5,4,3,2,1
                   # ? = !
                   # 5 - i = ?
    print(star[0:5-i])

# 트리만들기
# 트리 만들기
# *
# ***
# *****
# *******
star="*"



print(star)

for i in range (5): # 0,1,2,3,4
# i가 0 ,1 ,2 ,3 ,4
# *은 1, 3, 5, 7, 9 [i와 관계] -> 관계 2 * i + 1
#  는 4, 3, 2, 1, 0 [i와 관계] -> 관계 4 - i
    star = ""
    for k in range(2 * i + 1): # 바깥 for 문의 내부변수와 다른 변수명 사용함.
        star += "*"

    blank = ""
    for k in range(4 - i ):
        blank += " "

    print(blank + star )





























