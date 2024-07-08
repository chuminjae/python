a = 3
b = 4
aa = 3.14
aa = round(aa, 1) # aa = 3.1
print(a/b) # 나눗셈
print(a//b) # 몫
print(a%b)
print(a*b)
print(a**b) # 거듭제곱
print("\'Hello\'") #'Hello'
print("print(\"Hello\\nWorld\")") #print("Hello World")
a = input() # string으로 받아서 int or float으로 타입 변환 필요
a = input().split(" ") #공백 기준 입력 받기
# \n기준으로 안됨
b = input()
print(a, b) # a출력 공백 출력 b 출력
print(a, b, sep="") #a출력b출력
print(a)
print(b) # a랑 b사이 줄바꿈 한번
print(a, end = "")
print(b) # a랑 b사이 줄바꿈 없음
a = 3
while a != 4:
    a +=1
for i in range(4):
    if(i == 3):
        continue # continue만나면 다음원소로 넘어간다
# 함수 선언
def add(a, b):
    return a + b
add(3,7) # 10나옴
add(b = 7, a = 3) # 이렇게 parameter 지정해서 넣어도됨

#람다식 구현
print((lambda a,b: a +b)(3,7))

# global 변수
a = 0
def func():
    global a
    a+= 1

for i in range(10):
    func()
print(a) # 10 나옴 a를 전역변수로 선언

#입력
n = input()
#리스트로 받기
nn = list(map(int, input().split()))
## 변수로 받기
n,m,k = map(int, input().split())
# 빠르게 입력 받기
import sys
data = sys.stdin.readline().rstrip()
print(data)

#출력
answer = 7
print("출력할 변수는" + answer) # 이거는 불가능 str이랑int를 concatenate할수 없음
answer = str(answer) # 스트링으로 바꾸던가
# 콤마를 사용
print("출력할 변수는", answer)
#f-string을 사용
answer = 7
print(f"정답은{answer}입니다")
 
 #라이브러리
 # 내장함수 --> print(), input(), sort()같은 함수를 제공
 # itertools --> 반복되는 형태의 데이터를 처리하는 기능, 순열과 조합 라이브러리
 # heapq --> 힙 기능 제공 라이브러리(우선순위 큐 기능을 구현하기 위해 사용)
 # bisect --> 2진 탐색 라이브러리
 # collections --> deque, counter 같은 자료구조 포함
 
# 내장함수

# sum()
result = sum([1,2,3,4,5])
print(result)
# min(), max()
result = min(3,4,1,2)
print(result)
# eval() 수학 수식이 문자열로 들어오면 해당 수식 계산 결과를 반환
result = eval("(3 + 5) * 7")
print(result)
# sorted()
result = sorted([9,1,2,3,4]) # 오름차순 정렬
result = sorted([9,1,2,3,4], reverese=True) # 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75),('김글씨', 50)], key = lambda x:x[1], reverse= True)


# itertools
from itertools import permutations, combinations, product, combinations_with_replacement
data = ['A', 'B', 'C']
result = list(permutations(data,3)) # 순열 순서 상관 있음
result1 = list(combinations(data,2)) #조합 순서 상관 없음
result2 = list(product(data, repeat = 2)) # 순열인데 중복이 가능한 순열 
result3 = list(combinations_with_replacement(data,2)) # 조합인데 중복이 가능한 조합
print(result) 
print(result1)


# bisect 이진 탐색
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_right(a,x)) # 정렬된 순서 유지하면서 x를 삽입할때 가장 오른쪽 index
print(bisect_left(a,x)) # 정렬된 순서 유지하면서 x를 삽입할때 가장 왼쪽 index
def count_by_range(a, left_value, right_value):
    right =bisect_right(a, right_value)
    left = bisect_left(a, left_value)
    return right - left
a = [1,2,3,4,4,4,5,6,7,8,9]
print(count_by_range(4,4)) # 저 범위 내에 있는 숫자 개수 출력
print(count_by_range(1,3)) # 저 범위 내에 있는 숫자 개수 출력