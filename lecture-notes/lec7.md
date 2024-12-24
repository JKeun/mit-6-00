### Lecture 7: Lists and mutability, dictionaries, pseudocode, introduction to efficiency 



List

- Mutable: 리스트는 변한다

- 리스트 요소를 assign 할 수 있음

  - `Ivys[1] = -15`
    - 리스트를 변화시킴
    - 변수의 바인딩을 다른 객체로 바꾸는 것
    - 오버로딩
    - ivys 는 여전히 같은 객체임
    - 그러나 ivys 의 요소들은 다른 객체임
  - 리스트는 객체의 순서임
    - 즉, `ivys[1] -> |   | -15 |   |   |`

- ```
  L1 = [1, 2, 3]
  L2 = L1
  print L2 -> [1, 2, 3]
  
  L1[0] = 4
  print L1 -> [4, 2, 3]
  
  print L2 -> [4, 3, 2]
  ```

  - L1 -> `| 1 | 2 | 3 |` <- L2
    - L1 과 L2 는 같은 객체를 바라보고 있기 때문에
    - L1을 변경하면 L2도 변하게 되는 것
    - 핵심 내용임 -> 두가지 다른 루트로 바인딩한 동일 객체라는 점

- ```
  a = 1
  b = a
  a = 2
  print b -> 1
  ```

  - a -> `| 1 |` <- b
    - a -x> `| 1 |` : a 를 2에 대입했을때 1과의 연결을 꺤 것임
    - a -> `| 2 |` : a를 다른객체 2에 바인딩 함
    - 왜냐하면 immutable 이기 때문에

- ```
  L1 = []
  print L1 -> []
  print L2 -> [4, 3, 2]
  ```

  - 이것도 위와 비슷한 개념
  - L1 이  [] 로 리바인딩 되는 순간, 기존 객체 [4, 3, 2]와는 연결이 끊기게 된다



Dictionaries

- 리스트와 동일하게 Mutable
- 리스트와 달리 정렬되지 않음 (Not ordered)
- 인덱싱을 일반화 함 (Generalize indexing)
- 모든 요소가 키 - 값 쌍임 <Key, value>
  - `EtoF[0]` : 순서가 없기 때문에 에러
  - `dictionary = {1:"one", 2: "two", "one": 1, "two": 2}` :  이것도 가능
  - 키, 밸류로 어떤 값도 사용 가능
- 왜 딕셜러니를 갖는가?
  - key, value 쌍인 곳에서 리스트를 가질 수 있음
  - 딕셔너리를 더하는 것은 어떤 컴퓨터적인 힘을 주진 않으나, 많은 표현적인 확시늘 주 프로그램을 더 깨끗하게 작성가능
  - 그리고 가장 중요한 것은 빠르다
    - 리스트로 만약 작업했다면, 키를 찾는 시간은 리스트의 길이에 선형적으로 증가함
    - 딕셔너리에서는 Hashing 이라는 기술을 이용 -> 일정 시간에서 키를 검색하도록 허용함, 얼마나 딕셔너리가 큰지 상관없음



Pseudocode (의사코드)

- 삼각형의 빗면 계산 예시

  - input value for base as float

  - input value for height as float
    - square root of b\*b + h\*h
      - save as float in hyp(빗변)

  - print out using value in hyp

- 주목

  - 모듈 방식의 개념을 사용 - 모듈의 순서를 리스트했음
  - 의사 코드가 나에게 값에 대한 정보를 말해줌 - ex. input float..
  - 제어의 흐름 -- 일어나는 순서를 알려줌
  - 추상화를 사용 -- 제곱근을 만들 방법에 대해서는 아무 이야기 하지 않음

- def Foobar 를 먼저 작성하는 것은 잘못된 방법이다

  - 순서가 무엇인지 대해 생각하는 것으로부터 시작해야한다

- ```python
  import math
  
  # Get base
  inputOK = False
  while not inputOK:
    base = input("Enter base: ")
    if type(base) == type(1.0): inputOK = True
  	else: print("Enter. Base must be a floating point number.")
  
  # Get height
  inputOK = False
  while not inputOK:
    height = input("Enter height: ")
    if type(height) == type(1.0): inputOK = True
  	else: print("Enter. Height must be a floating point number.")
  
  hyp = math.sqrt(base*base + height*height)
  
  print("Base" + str(base) + ", height" + str(height) + ", hyp" + str(hyp))
  ```

  - depensive programming

    - 유저가 실수로 입력하는걸 방지 -> 우리는 유저에게 의존해선 안된다.
    - 값을 입력하면 나는 확인할 수 있다. -> 타입을 체크 -> 실수형인가 확인
      - 만약 맞다면 OK
      - 아니라면 -> 작은 무한루프를 만들 것 (좋은 방법은 아니긴 함)
        - inputOK 변수를 만들어 타입이 맞으면 True, 아니면 에러 메세지하고 다시 while 루프 돌아감
    - 마지막 hyp 변수가 실수형이란 보장은 어디서하나?
      - 그건 계약에 의해서 -> 두 실수형을 제곱하면 실수가 나온다는 계약이 확실함

  - 위 코드에서 base 와 height 블록은 일치함 -> 명백한 패턴

    - 그다음 질문 -> 두 코든간에 다른점은 무엇인가?
    - 나는 현재 두가지를 제안함 -> 차이첨은 여기서 나옴
      - 입력을 요청할 때 내가 출력한 것은 무엇인가?
      - 실제로 옳지 않은 인풋을 받을떄 어떻게 출력한가?

  - 함수를 제작

    - 위 차이를 포착 -> 변하는 것을 식별하는 것

    - 그리고 그들 각각에게 변수 이름을 줌

    - 그리고 나서 이 변수 이름을 내부에 가진 계산의 나머지를 포착하는 함수를 작성

    - ```python
      def getFloat(reqestMsg, errorMsg):
        inputOK = False
        while not inputOK:
          val = input(reqestMsg)
          if type(val) == type(1.0): inputOK = True
        	else: print(errorMsg)
      	return val
      
      base = getFloat("Enter base: ", "Error: base must be a float")
      height = getFloat("Enter height: ", "Error: Height must be a float")
      
      hyp = math.sqrt(base*base + height*height)
      
      print("Base" + str(base) + ", height" + str(height) + ", hyp" + str(hyp))
      ```

    - 함수의 본체는 정확하게 위 계산과 동일

    - 유일한 다른 차이는 값을 리턴해야 하는 함수라는  > 값을 돌려줘야함

    - 핵심이 무엇인가

      - 함수 내부에서 모듈을 포착함

    - 이점

      - 읽을 코드가 적다 -> 디버깅이 쉽다
      - 기능의 구현과 실행의 구현을 분리했다는 것 (Separate implementation from functionality and implementation from use)
        - 위 함수를 사용하는 누구라도 그것의 내부에 무엇이 있는지 걱정할 필요가 없다는 것
        - 사용자와 구현자 사이를 분리함

  

  Efficiency -- orders of growth

  - choice of algorithm (알고리즘을 선택하는 것)
  - map problem into class of algorithms (문제를 알고리즘의 클래스로 만드는 것)
  - 측정해야할 measure: space & time
    - space: how much memory to complete
    - time: 우리가 이번 시간에 초점을 맞출 내용
      - 실행하고 얼마나 걸리는지?
        - 입력에 의존, 기계에 의존, 파이썬 버전에 의존, 프로그래밍 언어에 의존 ...
  - What is the number of basic steps needed as a function of input size?
    - 입력 사이즈의 함수로써 필요한 기본적인 단계의 수는 무엇인가?
    - 입력 사이즈는 무엇을 의미하나?
      - 불행하게도 문제에 의존함, 리스트 크기, 인티져 사이즈, ...
    - basic step 이 무엇인가?
      - 우리는 전형적으로 기본적인 단계로써 기계가 딸려 있는 내장된 초기 요소들을 사용할 것
        - 산술 연산, 비교, 메모리접근(Random Axcess Model)
      - 두번쨰 가정은 기본적인 초기 요소들이 일정한 시 계산하는데 같은 양의 시간이 걸린다는 가정
  - Random Access Model 예시
    - best case -- min
    - worst case -- max
      - 우리는 결과적으로 최악의 경우에 초점을 맞출 것임
      - 놀랄 만한 결가 없다는 것을 의미, 상한의 감각을 가짐
    - expected case -- avg
      - 구하기 힘들다. 입력의 분포를 알아야 가능하기 때문

  

  

