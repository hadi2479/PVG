A = 0

while True:
    A = A + 1
    print(A)
    if A >= 10:
        break  # 예시로 무한 루프를 멈추기 위해 설정한 조건
//////////////////////

import itertools

A = 0

for _ in itertools.cycle(range(1)):
    A = A + 1
    print(A)
    if A >= 10:  # 예시로 무한 루프를 멈추기 위해 설정한 조건
        break

