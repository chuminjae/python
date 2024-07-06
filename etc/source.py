a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장   
print("%o" %n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

a = input()
n = int(a)
print("%x" % n)  #n에 저장되어있는 값을 16진수(hexadecimal) 형태 문자열로 출력
print("%X" % n)  #n에 저장되어있는 값을 16진수(hexadecimal) 형태 문자열로 출력 대문자 형태로

a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' %n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 다음에 n에 저장.

c = int(input())
print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드로 바꿔 출력. 

a,b = input().split(" ")
a = float(a)
b = float(b)
print(format(a/b, ".3f")) # 소수점 셋째 자리까지 반올림해서 출력

a = input()
#파이썬에서 실수 비트샤프트는 안됨
print(a<<1) # 비트샤프트 2진수 왼쪽으로 밀기 2배 증가
print(a>>1) # 비트샤프트 2진수 오른쪽으로 밀기 2배 감소
