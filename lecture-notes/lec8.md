### Lecture 8: Complexity; log, linear, quadratic, exponential algorithms



Complexity, Efficiency, Orders of growth

- design decision
- 새로운 문제를 가장 유사한 알고리즘으로 생각할 수 있어야함



Iterative exponent

```python
def exp1(a, b):
  ans = 1
  while (b>0):
    ans *= a
    b -= 1
  return ans
```

- 루프를 통해 반복

  - 얼마나 많은 시간이 드는가?

  - 얼마나 많은 단계가 드는가?

    - WHILE loop (내부에 총 3단계 존재)
      - 단계1: b>0 비교
      - 단계2: ans **= a 곱셈
      - 단계3: b -= 1 뺼셈
    - 얼마나 많은 루프를 돌려야하는가?
      - b 타임
    - 3번의  b타임을 거쳐야 함
      - 3b steps
    - 루프를 나왔을때 2단계를 더 가짐
      - `2 + 3b steps`

  - if

    - b=300 -> 902
    - b=3000 -> 9002
    - b=30000 -> 90002

  - 복잡성을 고민할떄

    - 문제가 크기가 커짐에 따라 덧셈의 정수 2는 아무것도 아님 (전형적으로 추가된 정수는 의미없음)
    - 곱셈의 정수 3 는 어떤 의미에서 중요한 것이 아님
      - 문제는 그 수가 얼마나 큰가?
      - 전형적으로 곱셈의 정수 또한 걱정하지 않아도 됨
    - 정말로 걱정해야 하는 것은 문제의 크기가 점점 커지면서 이것이 어떻게 커지는가? 비용이 어떻게 증가하는가이다

  - Rate of growth as size of problem growth

    - Asymptotic notation (점근 표기)

    - Big O notation

      - upper limit to growth of function as input gets large

      - 입력값이 커짐에 따라 함수의 상한에 한계를 가짐

      - $$
        f(x) \subseteq O(n^2)
        $$

        - 상한한계: n의 제곱보다 크지 않다
        - x는 입력, n은 x의 크기를 측정
          - n -- measure size of x

  - 위 예시에서 증가를 어떻게 특정지을 수 있는가?

    - 문제의 크기
    - upper bound 는 중요하지 않음
    - 이 함수가 증가 할 때 가장 작은 크기의 클래스는 무엇인가? 중요
    - `O(b)`: order b = **Linear**
      - b를 증가하면 문제도 선형적으로 증가함



```python
def exp2(a, b):
  if b == 1:
    return a
  else:
    return a*exp2(a, b-1)
```

- Recursive exponent
  - `t(b)`: 문제를 풀기 위한 사이즈가 b일 경우 그 문제를 푸는데 걸리는 스텝
  - `t(b) = 3 + t(b-1)`
    - b를 비교, b에서 1을 뻄, a를 곱함 -> 총 3단계
    - 그리고 사이즈 b-1의 문제를 해결할 수 있는 어떤 숫자든지 더함
    - Recurrence relation
      - `t(b-1) = 3 + 3 + t(b-2)`
      - `t(b) = 3k + t(b-k)`
      - `Done: b-k=1 -> k=b-1`
  - 기본 단계로 내려가 보면,
    - 사이즈 = 1 로 문제를 해결해봄
    - k = b-1 이면
      - `t(b) = 3(b-1) + t(1)`
      - `t(b) = 3b - 3 + 2 = 3b -1` 
        - `t(1)`은 b==1 비교, return a -> 총 2단계임
  - `O(b)` = linear



```python
def exp3(a, b):
  if b == 1:
    return a
  if (b%2)*2 == b:
    return exp3(a*a, b/2)
  else:
    return a*exp3(a, b-1)
```

- a^b

  - `a^b = (a*a)^(b/2)  -- b is even`
    - `ex. 2^4 = (2^2)^(4/2)`
    - 곱하기와 나누기는 원초적 연산임
    - 이 한단계에서 이 문제를 절반으로 줄였음
  - `a^b = a*(a^(b-1))  -- b is odd`
    - b가 홀수라면, b-1 은 짝수임
    - 그럼 다음단계에서 또 다시 문제를 절반으로 줄일 수 있다는 것

- What is O(n)?

  - b is even

    - `t(b) = 6 + t(b/2)`
      - b==1 비교 1단계
      - 짝수인지 비교하는 3단계
        - 나머지구하기 (b%2)
        - 곱하기 (*2)
        - 비교 (== b)
      - 짝수일 경우 연산 2단계
        - 곱하기 (a*a)
        - 나누기 (b/2)
      - 총 6개의 단계와 b/2 사이즈의 문제를 풀기위한 재귀적 방법 추가 진행 (recursive)

  - b is odd

    - `t(b) = 6 + t(b-1) = 12 + t((b-1) / 2)`
      - 처음 4단계는 같음 -> 1인지 확인, 짝수인지 확인까지는 동일
      - 홀수일 경우
        - 곱하기 (a*exp)
        - 빼기 (b-1)
      - 총 6단계와 b-1 사이즈의 문제를 풀기위한 재귀적 방법 추가 진행
      - 그리고 다음단계에서 짝수로 재귀하면서
        - 다시 추가적으로 `6 + t((b-1) / 2)`

  - `t(b) = 12 + t(b/2)`

    - `= 12 + 12 + t(b/4)`
    - `= 12 + 12 + + 12 + t(b/8)`
    - `= 12k + t(b / 2^k)`

  - 언제 base case 에 도달하는가?

    - $$
      b / 2^k = 1 일때, 즉 k = log_2b
      $$

  - `O(logb)` = **Logarithmic**

    - 문제의 크기를 절반으로 줄임, 로그



```python
def g(n,m):
  x = 0
  for i in range(n):
    for j in range(m):
      x += 1
  return x
```

- 2개의 루프
  - 내부 루프 -> m번 진행
  - 외부 루프 -> n번 진행
- `O(n*m)`
  - 만약 m=n 이라면 -> `O(n^2)`
  - **Quadratic**



하노이 타워

- 문제를 작은 문제의 재귀로 생각
  - 사이즈 n-1 무더기를 여분의 스팟으로 옮김
  - base 디스크를 옮기고자 하는 스팟으로 옮김
  - 사이즈 n-1 무더기를 base 디스크 위로 옮김

```python
def Towers(size, fromStack, toStack, sparseStack):
  if size = 1:
    print("Move disk from", fromStack, "to", toStack)
  else:
    Towers(size-1, fromStack, sparseStack, toStack)
    Towers(1, fromStack, toStack, sparseStack)
    Towers(size-1, sparseStack, toStack, fromStack)
```

- 이 알고리즘의 복잡성은 무엇인가?
  - `T(n) = 1 + T(1) + 2T(n-1) = 3 + 2T(n-1)`
    - size 비교 1번
    - n=1 타워 1개
      - T(1) -> size 비교 1번, 이동(프린트) 1번 -> 총 2개
    - n=size-1타워 2개
  - `T(n)`
  - `= 1 + T(1) + 2T(n-1)`
  - `= 3 + 2T(n-1)`
  - `= 3 + 2 * (3 + 2T(n-2)) = 3 + 2*3 + 4T(n-2)`
  - `= 3 + 2*3 + 4 * (3 + 2T(n-3)) = 3 + 2*3 + 4*3 + 8T(n-3)`
  - `= 3(1+2+4+ ... + 2^(k-1) + 2^k T(n-k)`
- `O(2^n)`
  - **Exponential**
  - 이 반복적 콜은 2가지의 작은 사이즈의 문제들이 있음
  - 그리고 이 특성이 큰 차이점을 만들어냄



n = 1000, nanosecond speed

- Log  -->  10 nanosec    (if 10 millisecs)
- Linear  -->  1 microsec    (then 10 sec)
- Quadratic  -->  1 millisec    (then 16 min)
  - 이차 알고리즘도 빠른 것이 아님
- Exponential  -->  10^284 years!
  - Boom
  - 무조건 피하는게 상책



알고리즘의 종류들을 알고 알고리즘의 복잡성에 알고리즘의 성능을 알아서 매치하길 바람

- Linear
  - 선형 알고리즘은 한번 지나갈 때, 불변의 양인 1로 문제를 줄여나가는 경향이 있음
  - 문제의 크기가 n인 곳에서 n-1 인 곳까지
- Logarithmic
  - 전형적인 로그 알고리즘은 여러분이 어떤 승인자로 문제를 감소시키는 것
  - 절반으로, 1/3 으로, ...
- Quadratic
  - 2차 알고리즘은 2배집합, 3배 집합의 것들은 2차 알고리즘이나 큐빅 알고리즘과 같음
  - 더블 루프 2차 알고리즘은 여러분이 어떤 것의 하나의 세트를 하고 있고
  - 다른 몇 배의 것을 하고 있기 때문
- Exponenital
  - 지수 알고리즘은 문제 한가지를 형식적으로 줄여나가
  - 더 작은 사이즈를 갖는 2개 혹은 더 많은 부분 문제들로 만들 떄임



Search a sorted list

```python
def search(s, e):
  answer = None
  i = 0
  numCompares = 0
  while i < len(s) and answer == None:
    numCompares += 1
    if e == s[i]:
      answer = True
    elif e < s[i]:
      answer = False
    i += 1
  print(answer, numCompares)
```

- what is orders of growth?
  - `Linear`
  - 리스트를 따라 내려가고 있음 -> `O(len(s))`
  - 질문
    - 내가 찾고자 하는 것보다 리스트의 요소가 클 경우 나머지를 버리는데 이는 복잡성을 줄이는데 도움이 안되나?
    - 답은 도움이 안된다. 최악의 케이스까지 갔을때 아무 도움이 안됨 (찾고자 하는 것이 마지막에 있거나, 없는 경우)
    - 복잡성은 그대로 Linear 임
- 어떻게 문제를 줄일 수 있는가?
  - 절반을 pick 해서 그 값이 맞는지, 그 값보다 큰지 작은지 판단
  - 만약 맞다면 lucky
  - 만약 다르다면 나머지 부분을 버림
  - 여기서 왜 절반을 pick 하는게 적절한가?
    - 최악의 수를 피할 수 있기 때문, 어쨌든 최소한 매 단계마다 절반을 버릴 수 있음을 보장한다
  - 그렇다면 Order of growth 는 무엇인가?
    - Logarithmic -- 매번 문제를 절반으로 잘랐기 때문
    - 우리는 여기서 추가적으 해야하는 것을 더 해보겠음

```python
def bsearch(s, e, first, last):
  print(first, last)
  if (last - first) < 2:
    return s[first] == e or a[last] == e
  mid = first + (last - first)/2
  if s[mid] == e:
    return True
  if s[mid] > e:
    return bsearch(s, e, first, mid-1)
  return bsearch(s, e, mid + 1, last)

def search1(s, e):
  print(bsearch(s, e, 0, len(s) -1 ))
  print("Search complete")
  
def testSearch():
  s = range(0, 1000000)
  input("basic, -1")
  print(search(s, -1))
  input("binary, -1")
  print(search1(s, -1))
  
  input("basic, end")
  print(search(s, 1000000))
  input("binary, end")
  print(search1(s, 1000000))
  
  input("basic, partway")
  print(search(s, 1000000))
  input("basic, larger end")
  print(search(s, 10000000))
  input("binary, partway")
  print(search1(s, 1000000))
  input("binary, larger end")
  print(search1(s, 10000000))
```

- 끝 값 - 처음 값 이 2보다 작다면, 그 리스트 안에 남은 요소가 2개보다 적다면 -> 그 두개 요소를 확인할 수 있 -> return

- 중간 부분을 절반으로 지정하고

  - 만약 중간지점에 있다면 return
  - 만약 내가 찾는 값보다 크다면 다시 절반을 또는 아니라면 다른 절반을 진행함

- 테스트의 의미

  - 찾고자 하는 값이 -1일떄
    - 이미 찾고자 하는 리스트의 범위 밖이므로
      - 선형은 바로 첫번쨰 시도에서 답을 리턴
      - 로그는 몇번 진행하다 답을 리턴
  - 백만개 리스트에서  백만을 찾을 떄
    - 선형은 어느정도 시간이 걸림
    - 로그는 아까 -1을 찾을떄와 동일한 스텝을 진행하고 답을 리턴
      - 끝단에 있는 값이므로 각 시간마다 반절을 잘라냈기 때문
  - 천만개 리스트에서 천만을 찾을떄
    - 선형은 백만개 때보다 10배 더 느림
      - 문제를 10배 늘림 -> 실행시간을 10배 더 걸리게 함
    - 로그는 백만개 때보다 겨우 한,두단계만 추가되어 답을 리턴
      - 문제를 10배 늘림 -> 하나의 단계만을 더함

- bi search 더 주의 깊게 보기

  - 1 을 찾는 것의 복잡성은 무엇인가?
    - 첫 단계 (last-first < 2 비교) -> 상수
    - 두번째 단계 (s[first] == e or s[last] == e) -> 상수로 보임
      - 잠깐, 지금 리스트 s에 accessing 하고 있음
      - 내가 리스트의 n번쨰 요소에 다다르게 하기 위해 얼마나 걸리게 될까?
      - 이것은 아마 초기 단계(Primitive step가 아닐 것임
      - 그리고 그것은 사실 내가 리스트에 저장하는 방법에 달려 있음
    - List of ints -- Logarithmic
      - 정수 타입의 리스트를 가진다면
      - 하나의 정수를 대표하기 위해 4개의 메모리 chunk 가 걸리게 될것
      - 예를 들어 i 번쨰 요소를 찾기 위해 단지 시작점을 갖고 리스트가 있는 메모리의 시작점에서 i의 4배를 보면 거기에 가기 위해 얼마나 많은 유닛이 있는지 말해줄 것
      - 그것은 내가 찾고 싶은 그 리스트의 i번쨰 요소의 메모리 주소가 됨
      - ith element -> stat + 4*i
      - 내가 찾고자 하는 곳을 가기까지 변함 없는 시간의 양만큼 걸린다는 의미
    - General lists ?
      - 여러가지 선택권이 있음
      - Linked List
        - 첫번째 요소가 실제 값을 갖는 리스트의 시작점을 가리키는 포인터를 가질 수 있음
        - 그리고 이것은 그 리스트의 다음 요소를 가리키게 될 것
        - 다르게 얘기하면 그 부분의 첫 번째 파트는 얼마나 많은 셀을 실제 값을 저장하기 위해 가져야 하는지의 몇몇 인코딩이 됨
        - 그리고 내겐 그 리스트의 다음 요소를 갖기 위한 곳을 내게 말해주는 방법
        - | val | point |  ->  | val | point |  ->  |  |  |
        - 문제가 있음
          - 그 리스트의 i번쨰 요소를 찾기 위해서 얼마나 긴 시간이 걸리나?
          - 첫 번쨰 장소에 가서 건너뛰기 위해 얼마나 많은 것을 지나야 할지 알아 낼 것이고
          - 두번쨰 장소에 가서 또 알아볼 것
          - 결국 문 밖으로 나오게 됨
          - 나는 내가 가는 길을 셀 것이고 그것은 그 리스트의 i번쨰 요소를 찾기 위해 리스트의 길이에서 선형으로 접근한다는 뜻
          - 그리고 그것은 복잡성을 증가시킴
      - 대안법 -- constant access
        - 메모리의 어떤 장소에 있는 리스트의 시작점을 갖는 것
        - 그리고 실제적인 값들을 가리키는 메모리 안의 성공적인 셀들을 하나씩 보는 것
        - 그것은 아마 몇몇의 임의적인 메모리 양에서부터 시작할 것
        - 그러한 경우 다시 첫번쨰 List of ints 로 돌아옴
        - 그리고 결과적으로 그 리스트에서 접근 시간은 변하지 않음
        - 대부분의 python 의 리스트가 취하는 방법
    - ![lec8-1](file:///Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec8-1.png)
  - 말하고자 하는것
    - 초기 단계가 무엇인지에 대하여 조심해야 한다는 것
    - 만약 제가 어떤 리스트의 i번쨰 요소인 정수에 접근한다고 가정한다면
    - 여러분은 제가 전에 했던 로그 분석처럼 보이는 그 분석의 나머지를 볼 수 없음
      - bsearch 는 로그 복잡성을 가지나
      - 초기 요소가 무엇인지에 따라 추가되는 복잡성이 다름, 즉 나의 초기 요소가 무엇인지 알아야 함

  

