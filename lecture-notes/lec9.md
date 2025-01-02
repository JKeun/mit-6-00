### Lecture 9: Binary search, bubble and selection sorts 



지난주

- 복잡성, orders of growth
- 알고리즘
  - 선형 알고리즘
    - 한개 또는 일정한 양만큼 매 시간 문제의 사이즈를 줄인다는 것
    - 뺼셈 개념으로 문제가 작아짐
  - 로그 알고리즘
    - 빠름, 일정한 양만큼 문제의 사이즈를 줄인다는 것
    - 나눗셈 개념으로 문제가 작아짐
  - 이차 알고리즘
    - 다중 중첩 루프, 반복, 재귀 호출을 가진 것들
    - 선형 시간의 양, 선형 숫자를 여러번 반복하게 되면 이차 알고리즘이 됨
  - 지수 알고리즘
    - ex. 하노이의 탑
    - 지수 알고리즘을 선호하지 않음 -> 굉장히 빨리 커지기 때문



이진탐색 (binary search)

- 기본 전제

  - 정렬된 원소들의 리스트를 가지고 있음, 그 리스트 안에 특정 원소를 알고 싶음
  - 중점을 테스트해보고 찾던 것이 아니면 크거나 작은지 비교한 뒤 한쪽 절반을 취해 다시 반복

- 복잡도

  - log(n)
  - 반으로 나누는 특성
  - 항상 멈춘다는 것을 어떻게 생각했나?
    - 2개만 있는 리스트에 도달한다면 끝난다
  - 2^k = n -> k = log(n) -> k번 수행

- 일반화 (로그 스타일의 알고리즘)
  - Pick the mid point
  - Check to see if this is answer
  - If not, reduce to smaller problem, Repeat



Implement List

- Constant access
  - 메모리상에서 어떤 곳에 도달하기 위해 그리고 리스트의 어떠한 값을 얻기 위해
  - 어떤 원소를 찾고 싶은지 말하고, 이러한 원소들은 특정한 사이즈 안에 저장되어 있으며,
  - 그 인덱스에 4를 곱한 다음 start 에 더해주면 내가 가고자 하는 곳에 도달할 떄의 일정한 시간이 나오게 됨
  - 내가 찾고자 하는 것이 일정한 사이즈 안에 저장되어 있다는 걸 안다면 잘 작동 될 것
  - 그런데 리스트의 리스트를 가진다면? 이러한 경우에는 신중해야함
  - ![lec9-1](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-1.png)
- Linked List = Linear access
  - k번째 원소를 찾는데 얼마나 걸리나? 복잡도 = Linear
  - 한 개씩 밟아 가야 하기 때문
  - ![lec9-2](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-2.png)
- Python 의 방식
  - 위 Linked List 의 변형
  - 메모리 상의 값을 가리키는 포인터와 다음 원소를 가리키는 포인터가 쌍으로 존재
    - 이 쌍에서 메모리 상의 값을 가리키는 포인터만 따로 모아놓음
    - 포인터들의 리스트로 재조직함 (값 자체가 아니라, 값을 가리키는 포인터들의 모음)
    - 이것이 왜 좋은가? -> constant access 가 가능하기 때문
    - ![lec9-3](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-3.png)



정렬되지 않은 리스트를 가지고 있다면

- Should we sort before search?
- 얼마나 빠르게 정렬할 수 있는가?
  - Can we sort in sub-linear time? (선형보다는 적은 시간안에?) --> No
    - 적어도 하나씩 살펴봐야 하기 때문에 No
  - Can we sort in linear time? --> Probably Not
  - How fast can we sort? --> `n logn` time
- 무엇이 더 나은가? 한번 검색 case
  - 1번 - 정렬되지 않은 리스트가 있고 그것을 탐색 --> Linear case -> `n`
  - 2번 - 그것을 정렬하고 검색 --> `n logn + logn`
  - 일반적으로 n logn 이 n보다는 크다 --> 따라서 만약 한번만 검색을 한다면 선형 탐색을 사용하는게 유리
  - ![lec9-4](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-4.png)
- 무엇이 더 나은가? k search case
  - 1번 -  탐색 하기 위한 n 거게에 k배 -> Linear case -> `kn`
  - 2번 - Sort&Search case -> `n logn + k logn`
  - n 이 크거나 k가 많은 경우에는 `n logn + k logn` 이 더 작아질 것
  - ![lec9-5](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-5.png)
- Amortize the cose
  - 이것이 비용이 축소되는 것이 우리를 도와주는 부분
  - 우리가 무엇을 하려고 하는지에 따라 달라진다
  - 위 케이스에선 2개의 변수가 존재 -> 문제는 리스트의 길이가 무엇이냐는 것이고 얼마나 많이 그것을 검색할 것인가



Selection sort

- ```python
  def selSort(L):
      for i in range(len(L) - 1):
          print(L)
          minIndx = i
          minVal = L[i]
          j = i + 1
          while j < len(L):
              if minVal > L[j]:
                  minIndx = j
                  minVal = L[j]
              j = j + 1
          temp = L[i]
          L[i] = L[minIndx]
          L[minIndx] = temp
  ```

- 

- ![lec9-7](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-7.png)

  ![lec9-8](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-8.png)

  ![lec9-9](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-9.png)

- 첫번째
  - minIndx i = 0
  - minVal = 1
  - j 를 하나씩 옮겨가면서 1이 j번째 요소보다 크면 minIndx 를 변경하고 아니면 끝까지 반복
- 두번째
  - minIndx i = 1
  - minVal = 8
  - j를 하나씩 옮겨가면서 체크 -> 8은 3보다 크다 -> minIndx = 2 , minVal = 3
  - j를 그 뒤로 하나씩 옮겨가면서 나머지도 체크 -> 없음 -> 루프 끝
    - temp = 8 에 저장해두고, minIndx 가 가리키는 곳에 minVal = 3 을 넣어줌 -> 그리고 마지막으로 원래 3이 있던 자리에 temp=8을 넣어줌
- 무엇을 하고 있는 것인가?
  - 리스트의 뒤쪽에서 최소 값을 반견하고
  - 최소 값이 온 자리를 파악하고 있다가 값을 서로 교환해줌



Loop invariant (루프 불변성)

- 루프를 통과할 때 마다 항상 참이 되는 특성
- List is split into prefix & suffix, prefix is sorted, suffix is not
- 이 루프는 기본적으로 마지막 요소에서부터 시작하고, 리스트의 끝에 닿을 때 까지 1씩 증가해감
- 즉 중간 정도에서 정렬이 다 되어도 전체 리스트를 모두 검사하며 지나감
- ![lec9-10](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-10.png)
- 복잡도는 무엇인가?
  - quadratic -> n^2
  - 리스트를 하나씩 검사하며 내려감
    - 각 시작점에서 리스트의 나머지 부분을 보고 다음 장소에서 교환해야 할 원소는 무엇인지 결정함
    - 의문점
      - 리스트를 검사해 나갈때 남아있는 부분은 점점 작아진다
      - 그러나 이것도 일반적으로 생각한다면 평균적으로 리스트의 길이에 해당함
      - 따라서 n개의 것들을 n번 하게 되고 이는 이차 알고리즘이 됨



Bubble sort

- ```python
  def bubbleSort(L):
      for j in range(len(L)):
          for i in range(len(L)-1):
              if L[i] > L[i+1]:
                  temp = L[i]
                  L[i] = L[i+1]
                  L[i+1] = temp
          print(L)
  ```

- j -> 리스트 전체 길이만큼 이동함

- i -> 리스트를 이동하는데 j보다 1이 작음

  - 이것의 의미 -> 연속적인  짝을 보고 있음
    - i번째 원소와 i+first 원소를 봄
    - 만약 i번째 원소가 i+first 원소보다 크다면 세 개의 다른 집합들은 무엇을 할 것이냐 묻고 있음 -> 단지 그것들을 교환해줌

- 정렬의 관점에서 어떤 일을 하고 있는가?

  - 한번 통과하게 되면 결과가 어떻게 되는가?
  - 리스트의 마지막 원소는 어떤 것일까?
  - 한번 실행된 후에는 마지막 원소가 리스트에서 가장 큰 원소가 됨
  - 두번 째 실행 후에는 두번쨰로 큰 원소가 가장 큰 원소 다음에 놓이게 됨
  - 리스트 중에서 제일 가변운 항목이 물속의 커품처럼 제일 위로 상승하고, 그 다음 가벼운 것이 다음 자리로 상승하고 제일 무거운 것이 끝자리에 오기 때문에 말 그대로 버블 정렬이라 불림
  - 리스트를 지나면서 2개의 원소를 비교하고 큰 것을 옆에 놓는다. 

- ![lec9-11](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec9-11.png)

- 복잡도?

  - quadratic -> `O(len(L)^2)`



Bubble sort 개선

- ```python
  def bubbleSort(L):
      swapped = True
      while swapped:
          swapped = False
          print(L)
          for i in range(len(L) - 1):
              if L[i] > L[i+1]:
                  temp = L[i]
                  L[i] = L[i+1]
                  L[i+1] = temp
                  swapped = True
  ```

- 루프 안에서 어떻게 진행되는지 더 주의깊게 살펴본 것

- 그럼에도 불구하고 복잡도는 quadratic 이다 -> 최악의 경우를 찾아도 여전히 이차 임.



마지막 질문

- 이 알고리즘들 중에 무엇이 가장 낳은가? 삽입 정렬? 버블 정렬?
- 일반적으로 선택 정렬과 비교해서 버블 정렬은 몇 번을 교환하게 될까?
  - 잠재적으로 아주 많이 -> 왜냐하면 우리는 그것을 계속 하기 때문에 (안쪽 루프에서 매우 여러번 돌게 될 것)
- 그렇다면 선택 정렬에서는 몇 번 교환하게 되는가?
  - 한 번에 한 번씩
  - 잠재적으로 단지 한번 교환하게 됨, 루프 끝에서 매번 교환하게 될 것
- 그래서 이것은 사실 수행시간에 대한 성장차수가 같다는 것을 말해줌
- 그러나 아마도 선택 정렬은 더 효율적인 알고리즘일 것 -> 일정한 양만큼 계속해서 하지는 않기 때문
- 사실 찾아보면 버블 정렬이 사용된 것을 많이 보지 못할 것, 매우 비효율적이기 때문



우리는 정렬을 떻게 더 잘 할수 있을까?

- divide and conquer algorithm

- 위에서 나온 중요한 개념 -> 이 개념으로 풀 것

  - ```
    - Pick the mid point
    - Check to see if this is answer
    - If not, reduce to smaller problem, Repeat
    ```

- 전체 리스트를 한 번에 정렬하기 보다는 조각으로 나누고 그 조각들을 각각 정렬하고 다시 가져와 합침, 같은 작업을 반복