# 1부터 10까지의 수에 대한 약수 구하기

for num in range(1, 11):  # 1부터 10까지 반복
    divisors = []  # 약수를 저장할 리스트
    for i in range(1, num + 1):  # 1부터 해당 숫자까지 반복
        if num % i == 0:  # 나누어 떨어지면
            divisors.append(i)  # 리스트에 추가
    print(f"{num}의 약수: {divisors}")

////////////////////////
def func(a):
    # print(a)
    for i in range(1, a+1):
        if a%i==0:
            print(i, end=" ")
for i in range(1, 11):
    print(i, ":", end=" ")
    func(i)
    print()
////////////////////////
