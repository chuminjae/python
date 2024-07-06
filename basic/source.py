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