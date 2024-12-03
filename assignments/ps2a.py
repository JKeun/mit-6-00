# 정확하게 구매할 수 없는 맥너겟 수량을 객체로 하여 1로 시작하라
# 가능한 객체 n에 대하여
    # 음수가 아닌 a, b, c 에 대하여 6a+9b+20c=n 을 테스트
    # 만약 아니라면, n 을 저장하라
# 테스트를 통과한 6개의 순차적인 값들이 있다면 솔루션을 통과한 것
# 마지막 저장된 answer (솔루션의 마지막 n이 아니다) 가 정답이다

n = 1
consecutive = 0
answers = ()
while consecutive < 6:
    solution = (0, 0, 0)
    for a in range(0, n//6+1):
        for b in range(0, n//9+1):
            for c in range(0, n//20+1):
                if 6*a+9*b+20*c == n:
                    solution = (a, b, c)
    
    if solution == (0, 0, 0):  # if there's no solution
        consecutive = 0  # reset count
        answers += (n,)  # add n into answers
    else:  # if threr's solution
        consecutive += 1  # increase count

    n += 1  # increase n

print("Largest number of McNuggets that cannot be bought in exact quantity:", answers[-1]) 
