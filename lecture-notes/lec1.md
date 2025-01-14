### Lecture 1: Goals of the course; what is computation; introduction to data types, operators, and variables



이 수업이 끝나면 얻게될 스킬들

- Computational thinking
- Understanding code
- Understanding abilities & limits
- Mappable into computation



Computatoin

- Think like a computer scientist
  - what is computation?
  - what is knowledge?
    - 서술적인 지식 vs 명령하는 지식
    - 서술적인 지식 -> 사실의 진술, 진실의 주장
      - 무엇을 테스트하는진 정의해주지만 어떻게 테스트하는지는 알려주지 않음
    - 명령하는 지식 -> 어떻게 하는가에 대한 진술
      - **레시피**, 순서대로 특정 명령들의 순서, 테스트의 반복과 멈추는 조건을 제시
      - computation
  - 어떻게 하면 쉽게 그 단계를 설계할 수 있는가?
    - 작은 회로를 만든다고 생각
    - 초기 컴퓨터 = fixed computer
      - calculator (계산기)
      - Atanasoff (선형 방정식 푸는 기계)
      - turing bombe (코드 해독 애런 튜닝 기계)
    - 훌륭한 회로란?
- Program is a recipe
  - fixed set of primitives can program anything
    - 초기 좋은 명령 셋트가 주어졌을떄, 좋은 프로그래머는 무엇이든 짤 수 있다
  - what is fixed set of primitives?
    - Turing 의 6개의 초기 명령들을 가지고 모든 프로그래밍을 할 수 있다
- Describe recipe -> need language
  - 최고의 언어는 없다
    - 각자의 어떤 영역에서 더 설명이 좋을 뿐
      - MATPLB ->  벡터와 행렬을 처리하는데 유리
      - C -> 데이터 네트워크를 제어하는데 유리
      - Lisp -> 복잡한 데이터셋트를 다룰때 유리
  - Python
    - 2008년 강의, 꽤 새로운 언어
    - 다른 언어들의 성분을 많이 가지고 있고, 이전 것들을 상속
    - 그러나 이 강의는 파이썬에 대한 강의는 아님, 생각을 설명하고 이해하기 위해 사용하는 언어일 뿐
    - 언어를 분류할 떄
      - High vs Low
        - Low -> 어셈블리 언어, 초기 명령들을 매우 간단한 연산을 통해 데이터를 메모리 한 영역에서 다른 영역으로 움직이는 것
        - High -> 설계자가 초기 명령들을 더 많이 만듦, 제곱근 계산도 초기 명령으로 정의할 수 있음
      - general vs targetted
        - 특정한 목적을 위한 언어인가? 아닌가?
      - interpreted vs compiled
        - 인터프리트된 언어 -> 소스 코드를 간단한 검사기로 거치지만, 기본적으로 인터프리터로 감, 그건 기계 내부에 있는 것으로 명령의 각 하나를 거치는 흐름을 제어함, 그리고 출력을 보여줌. 즉 런타임때 우리의 코드를 바로 간단하게 연산함
          - 장점: 디버깅이나 코드 그대로이기 때문에 이해하기 쉽다
          - 단점: 느리다
        - 컴파일된 언어 -> 소스코드가 있으면, 검사기(컴파일러) 를 거쳐 오브젝트 코드를 만듦, 버그를 잡고, 실제로 런하기 전에 명령의 더 효과적인 방법으로 변환
          - 장점: 빠르다
          - 단점: 디버깅, 이해하기 어렵다
    - Python
      - 파이썬은 어떤 언어냐?
        - High
        - General
        - Interpreted
      - Syntax (문법)
        - What are legal expressions (합법적인 표현인 것)
        - ex. SyntaxError
      - Static semantics (고정된 의미)
        - What programs are meaningful (의미가 있는 것)
        - ex. TypeError
      - Semantics
        - What does program mean, what happens (어떤 의미를 가지는가? 어떤 일이 일어나느가)
        - 이 부분은 누구도 동와줄 수 없음
        - 온전히 설계자가 의도한 대로 돌아가는지에 대한 부분임
        - Style 을 길러야 함
    - Python 기본 요소들
      - Values
        - Numbers
          - 3 - integers
          - 3.14 - floating point
        - Strings
          - 'abc' - string
      - Operations
        - +, *, -, /
      - Variables
        - myString = 'eric'