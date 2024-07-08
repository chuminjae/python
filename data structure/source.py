c = list()
c = []
c = [1,2,3,4,5]
print(c[-1]) #뒤에서 첫번째 원소 출력
c = [0] * 13 # 리스트 초기화
# 거꾸로 출력
a = int(input())
b = input().split()
for i in range(a-1, -1, -1):
    print(b[i], end =" ")
array = [i for i in range(20) if i %2 == 1] # 0에서 19까지 홀수 배열 생성
array = [i * i for i in range(1,20) if i*i != 361]
print(array[1:4]) #index 1번째 원소부터 3번째 원소까지
# n * m 크기의 2차원 배열 초기화
n = 3
m = 4
# 특정한 크기를 가지는 2차원 배열은 무조건 리스트 컴프리헨션을 사용해야한다.
array=[[0] * n for _ in range(m)]
print(array)
# 2차원 입력 받는 법
b = [[0] * 19 for _ in range(19)]
for i in range(19):
    b[i]=list(map(int, input().split()))
# 1차원 배열 입력
    b=list(map(int, input().split()))
a = [1,2,3,4,5]
a.append(6) #6 삽입
a.sort() #오름차순 nlogn
a.sort(reverse = True) #내림차순 정렬
a.reverse() #리스트 원소 순서 반대로 n
a.insert(2,3) #인덱스 2에 3추가 n
a.count(3) #3인 원소의 개수 n
a.remove(3) #값이 3인 원소 하나 제거 n
# 특정 원소 전부 제거하고 싶다면
remove_set = [3,4]
a = [i for i in a if i not in remove_set]
print(a)
data = "do you know \"python\""
data1 = "yes"
print(data * 3) #data 3번 출력
data = data + " " +data1
print(data)
# 튜플 자료형 대입이 안됨
a = (1,2,3,4)
# a[1] = 3 대입 안됨 
# 사전 자료형 순서가 없음    키 - 값이 매치됨
data = dict()
data['a'] = "apple"
data['b'] = "banana"
data['c'] = "coconut"
print(data)
if 'a' in data:
    print(data['a'])
key_list = data.keys() # a, b, c
value_list = data.values() #apple, banana, coconut
print(key_list, value_list) # dict_keys(['a', 'b', 'c'])   dict_values(['apple', 'banana', 'coconut'])
# 집합 자료형 중복없고 순서 없음
data = set([1,1,2,3,4,5,5])
print(data)
data = {1,1,3,2,3,4,3,5,4,5}
print(data)
a = {3,4,7}
b = {2,3,4,7,8,10}
print(a|b) # 합칩합
print(a & b) # 교집합
print(a - b) # 차집합 a가 기준
data.add(4) #4 추가
data.update([5,6]) #5 6 추가 대괄호 넣을것
data.remove(3) #3 삭제

# heapq - 최소 힙트리
# h가 최소 힙트리 구조를 가지고 있음
# 이미 리스트가 존재한다면 heaq.heapify(list)
# heaq.heappop(h) --> 가장 작은 원소 제거 return
import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        print(h[i])
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#heapq - 최대 힙트리
import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        print(h[i])
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)


# collections
# deque 인덱싱 슬라이싱 불가
# 하지만 맨앞, 뒤에 삽입이나 삭제는 효과적
# 첫번쨰 원소 제거는 popleft() 삽입은 appendleft(x), 맨뒤 원소 제거는 pop() 삽입은 append(x)
from collections import deque
data=deque([2,3,4])
data.appendleft(1)
data.append(4)
print(data) #deque(1,2,3,4,4)
print(list(data)) # [1,2,3,4,4]

# couter 등장횟수를 센다
from collections import Counter
data = Counter(['red', 'blue', 'red', 'brown'])
print(data['blue'])
print(data['brown'])
print(dict(data)) # 사전 자료형으로 변환

# math
import math
print(math.factorial(5))
print(math.sqrt(7)) #루트 7
print(math.gcd(21,14)) # greatest common diviser
print(math.pi)
print(math.e)





