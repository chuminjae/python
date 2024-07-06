c = list()
c = []
c = [1,2,3,4,5]
print(c[-1]) #뒤에서 첫번째 원소 출력
array = [i for i in range(20) if i %2 == 1] # 0에서 19까지 홀수 배열 생성
array = [i * i for i in range(1,20) if i*i != 361]
print(array[1:4]) #index 1번째 원소부터 3번째 원소까지
# n * m 크기의 2차원 배열 초기화
n = 3
m = 4
# 특정한 크기를 가지는 2차원 배열은 무조건 리스트 컴프리헨션을 사용해야한다.
array=[[0] * n for _ in range(m)]
print(array)
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