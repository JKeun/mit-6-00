### Lecture 10: Divide and conquer methods, merge sort, exceptions



Search

- Ordered List
  - Binary search
  - `log n`
- Unordered List
  - Linear search
  - `n`
- to get order? (Sort)
  - `n log n`

-  if Single Search
  - linear search -> `n`                                    (better)
  - sort & search -> `n log n + log n`

- Amortize
  - 비용 안에서 factor 가 필요하다는 것과 함께 그것을 어떻게 이용할 것인가?
  - 일반적으로 하나의 리스트 안에서 한번 검색할 것이 아니라, 여러번 검색 할 것이라면?
  - linear search -> `kn`
  - sort & search -> `n log n + k log n`  (better)




Divide and Conquer ALgorithm

- logic
  - Split the problem into several subproblems of the **same** type
  - solve independently
  - combine solutions



Merge sort

- merge two lists

  - [3, 12, 17, 24], [1, 2, 4, 30]
    - `1<3, 2<3, 4<3, 4<12, 12<30, 17<30, 24<30`
    - `[1, 2, 3, 4, 12, 17, 24, 30]`
    - 7 comparisons
    - linear -> `O(n),  n -- sum of # of elements in each list`

- merge sort

  - divide list in half

  - continue until we have singlton list

  - merge of the sublists

    - ```
      [1, 4, 3, 6, 5, 2, 8, 7]
      [1, 4, 3, 6]
      [1, 4]
      [1]
      [4]
      merged [1, 4]
      [3, 6]
      [3]
      [6]
      merged [3, 6]
      merged [1, 3, 4, 6]
      [5, 2, 8, 7]
      [5, 2]
      [5]
      [2]
      merged [2, 5]
      [8, 7]
      [8]
      [7]
      merged [7, 8]
      merged [2, 5, 7, 8]
      merged [1, 2, 3, 4, 5, 6, 7, 8]
      ```

  - 이진 탐색의 경우와 다르다는 점을 기억

    - 우리는 확실히 그것들을 나누어 가지만, 그 결합은 사실 약간의 일을 필요로 함

  - Divide & Conquer 알고리즘을 사용할떄 기억해두고 싶은 것

    - 나누는 것의 이점을 정말 쓰고 싶지만, 만약 합치는 단게에서 결국 엄청난 일을 해야 한다면, 어떠한 것도 얻지 못할 수 있음
    - trade off 를 잘 찾는 것이 중요

  - Complexity

    - ![lec10-1](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec10-1.png)
    - 각각의 병합 연산들은 n
      - 크기가 1인 곳에서는 n번의 연산 (뎁스3)
      - 크기가 2인 곳에서는 n/2번의 연산 (뎁스2)
      - 크기가 4인 곳에서는 n/4번의 연산 (뎁스1)
      - 그래서 항상 n개의 원소들을 병합하게 됨
      - 이 트리의 각각의 레벨에서 n번의 연산을 하게 됨 -> `O(n) operationsof each level`
    - 레벨이 몇 단계까지 있나? -> 분할에 달려 있음
      - `log n`
      - 각각의 단계에서 문제를 절반씩 나눔
    - 따라서 각 레벨마다 n번의 연산을 log n 번 하게 됨
      - `n log n`



Hashing

- Collection of integers example

  - ```python
    def create(smallest, largest):
        intSet = []
        for i in range(smallest, largest+1):
            intSet.append(None)
            return intSet
        
    def insert(intSet, e):
        intSet[e] = 1
        
    def member(intSet, e):
        return intSet[e] == 1
    ```

  - Complexity?

    - `Constant`
    - 우리가 찾고자 하는 값이 리스트에 어느 곳에 있더라도 접근하는데 일정한 시간이 걸리도록 리스트를 디자인 해야 함
      - `member` 함수는 상수 시간이 걸림
        - `O(1)`

- Collection of Characters example

  - hash function 은 어떤 종류의 데이터도 정수들로 대응시켜주는 방법을 가지고 있음

  - ```python
    def hashChar(c):
        # c is a char
        # function returns a different integer in the rage 0-255
        # for each possible value of c
        return ord(c)
    
    def cSetCreate():
        cSet = []
        for i in range(0, 255):
            cSet.append(None)
            
    def cSetInsert(cSet, e):
        cSet[hashChar[e]] == 1
        
    def cSetMember(cSet, e):
        return cSet[hashChar(e)] == 1
    ```

  - 해쉬는 입력값을 정수로 바꾸어 줌

  - 해쉬 함수는 문자를 0부터 256 사이의 정수에 대응(map) 시킴

  - 어느정도 길이의 리스트를 만들어 놓고, 단순히 표시해주면 끝

  - 만약 string 집합을 나타낸다면

    - 기본적으로 그 해쉬 함수를 일반화 시키면 됨
    - Rabin-Karp 알고리즘
      - 여러분이 넣은 값을 정수들의 집합으로 대응(mapping) 해주는 것과 같음

  - 패널티는 무엇인가? trade off?

    - trade space for time
      - 일정한 접근 시간을 가지게 됨
      - 그러나 더 많은 공간을 사용하게 됨

  - 저장 공간 안에서 해쉬 함수로 내가 가지고 있는 입력 값을 어떻게 정확하게 하나의 값에 대응 시키는가?

    - 대답은 "할 수 없다"
    - 간단한 정수들의 경우 가능하나, 얼굴인식, 지문인식, 비밀번호 등과 같은 문제들에는 정확하게 하나의 출력값에 입력값을 대응시키는 해쉬 함수를 디자인하기 어려움
    - 따라서 일반적으로 하는 해쉬 디자인은 여러분이 문제를 다룰 수 있는 코드를 디자인 하는 것임
    - 고르게 분포하게 하는 해쉬 함수를 사용해야함

  - Hard to create

    - 좋은 해쉬 함수를 만드는것은 사실 어려운 문제



Exceptions

- 에러를 고치기 위해 탑레벨로 올라가는 것은 상당히 짜증나는 일임

- 많은 exception 의 경우 사실 프로그램 디자이너로서 처리할 수 있음

- unhandled

- handled

  - ```python
    def readPlot(requestMsg, errorMsg):
        while True:
            val = input(requestMsg)
            try:
                val = float(val)
                return val
            except:
                print(errorMsg)
    ```

    - 루프에서 하는 작업
      - input 을 요청하고, 받은 input 을 float 으로 변환함
      - float 을 시도해보고 성공하면 -> return val
      - 만약 그렇지 않다면, float 은 옳은 용어를 사용하기 위해 버려질 것이고 type 에러 같은 것을 보여줌
    - try - except block
      - try 블록을 실행하면 명령문을 실행해보고, 안된다면 except 으로 넘어감
      - float 에 적합한 입력을 넣을때까지 루프가 반복 

  - 일반화 하기

    - 단순히 어떤 입력 값을 가지고 싶고, 그것을 시험해본 다음 옳은 값을 얻어내는 방법을 알아내고 싶음
    - 그리고 그것이 polymorphic (여러 단계를 거치는 것) 이길 바람

  - ```python
    def readVal(valType, requestMsg, errorMsg):
        while True:
            val = input(requestMsg)
            try:
                val = valType(val)
                return val
            except:
                print(errorMsg)
    ```

    - 루프에서 하는 작업
      - input 을 묻고, value 가 옳은 type 인지 확인하기 위한 절차를 가짐
      - 동일함, 이것이 작동하면 건너뛰고, 작동하지 않으면 exception 을 내보냄
      - 매우 유용한 코드임 왜?
      - 내가 그것을 가지고 있다면, 몇 개의 파일 이름에 그것을 저장할 수 있고 나의 프로시저들로 그것들을 불러 올 수 있기 때문
      - 외부에서 입력값을 받는 표준적인 방법임

- exception 을 단지 한곳에서만 사용할 필요는 없음

  - ```python
    def getGrades(fname):
        try:
            gradesFile = open(fname, "r")
        except IOError:
            print("Could not open", fname)
            raise "GetGradesError"
        grades = []
        for line in gradesFile:
            grades.append(float(line))
            return grades
    
    try:
        grades = getGrades("grades.txt")
        grades.sort()
        median = grades[len(grades)/2]
        print("Median grade is", median)
    except "GetGradesError":
        print("Whoops")
        
        
    # Output (py2 기준)
    Could not open qlgrades.txt
    Whoops
    ```

    - getGrades
      - open 에 지역변수로 묶어두고 이것이 성공하면 아래 리스트로 변하는 것을 실행하고, 나중에는 스코어 중앙값을 계산하는 걸 할 수 있음
      - open 이 성공하지 못하면 특정한 종류의 예외가 발생함
        - IOError 를 가지는 except 를 넣었음
        - 만약 try 에서 예외가 발생하면 그것을 처리하기 위해 except IOError 로 간다고 말하고 있음
    - 다른 한편으로 만약 전역 단계 (median 을 구하는 과정) 에 있고
      - 몇몇 다른 예외들이 발생한다면 그것은 이름 붙여지지 않음
      - 그 절차가 다른 프로시저에 의해서 불려진다면 그것을 처리할 수 있는 exception 블록이 있는지 물을 것임
    - 만약 그렇지 않다면, 결국 탑 레벨에 도달할 때 까지 체인이 올라가게 됨
    - 실행시 어떤 일이 일어나는가?
      - getGrades 내의 try 에서 exception 을 발생시켰지만, IOError 는 아니였음
      - 그러면 전역 try의 exception 으로 돌아와 에러 메세지를 출력함 "Whoops"
    - 정리
      - try 해보고 만약 잘 작동하지 않고, 그 단계에서 에러가 나오는 exception 을 가진다면 
      - 아니면 이 레벨에서 단지 이 종류의 에러만 가질 수 있다면
      - 위로 통과하라
      - 그 exception 은 계속해서 호출들의 체인을 통화할 것
      - 탑 레벨에 도달할 때 까지
      - 그 단계에선 우리가 항상 보는 것처럼 에러처럼 보임
      - 그러나 그것이 에러가 발생하는 곳을 알려주고 있음



Exception vs assert?

- assert 의 목적은 기본적으로
  - 여기에 테스트를 할 조건들이 있다는 것을 말함
    - ex. 제약이 걸린 input 만을 받아야 함
  - 만약 그것이 사실이면, 코드의 나머지 부분을 실행하고, 사실이 아니라면 에러를 띄움
  - assert는 pre-conditions(사실이어야 하는 assert안의 조항들) 를 가지고 있고, 그리고 post-condition을 가짐
  - 즉, assert를 사용한다는 것은 만약 여러분이 내게 pre-condition 들을 만족시키는 입력 값을 준다면 내 코드는  post-condition 을 만족시킨다는 것을 보장하는 것임
  - assert 는 여러분으로 하여금 디버깅 시간과 테스팅 시간에서 조건을 확인할 수 있게 해준다는 점에서 좋음
  - 코드가 어떻게 돌아가고 있는 것인지 볼 때 사용할 수 있음
- excpetion
  - 내 함수를 가지고 여러분은 원하는 것을 할 수 있음
  - 그리고 어떤 것이 잘못되어 가고 있는지 여러분에게 말해줄 수 있음
  - 그리고 대부분의 경우에 스스로 그것을 처리할 수 있음
  - 그래서 가능한 많은 exception 들은 기대되지 않은 것들을 처리하려고 할 것임
  - 사실 잘못된 용어(당신은 그것을 기대했지만) 사용자가 기대한 것은 아니다
  - 일반적인 것들 외에도 그 자체가 조건들을 처리하기 위해 노력할 것
  - 그래서 어쩄든 여러분들은 그것을 사용할 수 있고, 만약 처리할 수 없다면 다른 누군가에게 그것을 처리하라고 할 것이고, 기대되지 않은 조건들에 대해서는 처리하는 사람이 없을 때에만 탑 레벨로 올라갈 것임
- 정리
  - assert 는 사용자에게 말하기 위해서 여러분이 넣은 것
    - ex. 이런 type 의 입력 값을 넣었는지 확인하세요, 그러나 그 나머지 코드들은 올바르게 잘 작동할 것이라는 것을 장담합니다
  - exception 과 excpetion handler 는 이렇게 말함
    - 여기에 이상한 경우가 발생했고, 그것들을 처리하기 위해 무엇인가 하고 싶은 것이 있다는 것을 말함
- 마지막으로 왜 우리는 exception 을 가지고 싶어 할까?
  - float 예제로 돌아가면, 만약 숫자들이 주로 안에 있기를 기대했다면 try 해보고 강제로 변환헀을 수도 있음
  - 그러나 문제는 사실 내가 기대하는 형태를 가졌는지 가지지 못했는지를 알고 싶다는 것임
  - 17번의 에러 호출이 나올 때까지 그 값이 많은 코드를 돌아다녀야 하는 것보다 input 을 넣을 때 처리가 된 exception 을 가지는 것이 훨씬 나음
  - 그리고 여러분은 그것이 어디서 발생했는지 단서도 얻을 수 없기 때문
  - exception 은 사용가능한 지에 대해 말할 때 매우 유용함
    - "제가 일반적으로 이런 움직임을 기대했습니다. 그러나 다른 경우가 발생할 수 있다는 것을 알고 있고, 여기 각각의 다른 경우들에 대해서 하고 싶은 것이 있습니다. 그러나 입력 값이 계속해서 지나가게 되는 것을 바라지는 않습니다" 라고 말해야 할 떄 유용하다는 말임.
  - 코딩을 훈련하는 것에 대해 말하자면
    - 여러분이 프로그램을 짤 때, 프로그램에 들어올 것을 생각하는 것에 대해 추정하는 것은 쉽다
    - 그것들이 무엇인지 정말로 알았다면, 검색으로 사용하라
    - 그러나 여기에 약간의 융통성이 있어야 한다고 생각하면, 사용자가 잘못된 곳에 빠지는 것을 원하지 않을 것이다
    - 결과적으로 exception 을 사용하는 것은 좋은 것이다

