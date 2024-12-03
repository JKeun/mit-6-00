### Lecture 3: Common code patterns: iterative programs



What we did?

- 프로그래밍의 기본 요소들의 개요를 잡음

- 3가지 요소
  - Data
    - 근본적으로 우리가 이동하길 원하는 정보를 나타내는 방법
      - Number
      - Strings
      - Booleans
  - Operations
    - 초기 데이터 관련하여 데이터를 가져오고 새로운 데이터를 만들거나 데이터의 버전을 만드는 방법
      - +, *, ...
      - and, or, ...
  - **Commands**
    - **assignment**
      - **값에 이름을 바인딩하는 대입**
    - **input/output**
    - **conditionals**
      - **명령문들의 순서를 통해 제어의 흐름을 바꾸는 브랜칭**
    - **loop mechanisms**
      - **while**
    - **위 4가지 명령문 세트는 꽤 강력하고, 어떻게 코드 패턴을 작성할지를 할 수 있음**
- 좋은 코드 스타일이란
  - 코멘트
  - 타입 지시
    - 연산자들을 적용하기전에 피연산자의 타입을 검사해야 함
  - 좋은 변수 이름
  - 가능한 브랜치들을 테스트하는 생각



Iterative programs

- choose variable that "count"
- initialize outside the loop
- setup and test (include variable)
- construct block
  - change variable
- what to do when done



Flowchart

- 제곱근을 찾는 예제의 플로우 차트

  - ![lec3-1](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec3-1.png)

  - X의 사이즈에 따라 명령문 수행 횟수 결정

  - 시간의 수는 입력 수에 달렸음

  - 입력을 바꿀 때 코드의 복잡성도 바뀜

  - 선형 프로세스, Linear Process

    - 루프를 도는 시간의 수는 인수의 크기와 같음
    - 인수를 2배 늘리면 복잡성도 2배 늘어남

  - ```python
    # find the square root of a perfect square
    x = 16
    ans = 0
    while ans*ans <= x:
    	ans = ans + 1
    print ans
    ```

- 짝수/홀수 찾는 플로우 차트

  - ![lec3-2](/Users/jkeun/dev/cs-study/mit-6-00/lecture-notes/lec3-2.png)
  - X의 사이즈는 상관 없음
  - 명령문의 갯수만큼 수행 횟수 결정




SImulate code

- 간단한 값을 고르고 어떻게 돌아가는지 확인하기 (손으로)
  - 버그 -> 올바른 위치에서 멈추지 못함
  - 어떤 x 값이 루프를 끝내나?
    - x 가 양수이다 -> 코드가 언젠가 끝남
    - X가 음수이다 -> 코드가 첫 단계에서 끝남 -> print 0



Better code -> Defensive programming

- 모든 가능한 경로들을 살펴보는 것

  - 유저는 개발자가 원한대로 입력하지 않는다

  - 개발자는 멍청하다 (실수를 꼭 한다)

- 코드 설명

  - 첫 블락 -> 입력한 값이 음수인지 체크 -> 음수면 블락 밖으로 빠짐
  - while -> 기본적인 연산 -> 중간 ans 상태를 출력 -> 각 단계를 확인 가능
  - while 끝에 -> if 문 만남 -> 완벽한 제곱근인지 아닌지 확인 -> 결과 출력

- ```py
  if x <= 0:
  	while ans * ans < x:
  		ans = ans + 1
  		print("ans =", ans)
  	if ans * ans != x:
  		print(x, "is not a perfect sqaure")
  	else:
  		print(x)
  else: print(x, "is a negative number")
  ```



Exhaustive enumeration (철저한 계산)

- 어떤 인자, 계산의 어떤 요소의 모든 가능한 값들을 살펴 보는 것

- Try all "reasonable" values until you find solution

- 모든 약수를 구하는 예제

  - ```python
    x = 10
    i = 1
    while i < x:
    	if x % i == 0:
    		print("divisor ", i)
    	i = i + 1
    ```

  - 변화를 주고 싶은 것을 고르고, 그것을 루프 밖에서 초기화

  - 내가 볼 수 있는 테스트를 가짐

  - 루프 안에서 매번 하는 명령문 세트를 가짐

  - 모든 일이 끝났을때 어떤 것도 리턴하지 않음



For loop

- 데이터의 컬렉션이 주어 졌을때 루프 매커니즘을 수행, 더 일반적인 방법

- ```
  for <var> in <some collection>
  	block of code
  ```

- 장점 - > 깔끔함

  - 초기화 하는 것 필요 없음
  - 변수를 업데이트 하는 코드를 작성하지 않아도 됨

- ```python
  x = 10
  for i in range(1, x):
  	if x % i == 0:
  		print("divisor ", i)
  ```



Tuple

- ordered sequence of elements (immutable: 변경할 수 없음)

- ```python
  foo = (1, 2, 3, 4)
  ```

- selection

  - `foo[0]`

- slicing

  - `foo[1:3]`

- ```python
  x = 100
  divisors = ()
  for i in range(1, x):
  	if x % i == 0:
  		divisors = divisors + (i,)
  ```



Strings also support

- 문자열도 정렬된 컬렉션처럼 행동한다

- `s1 = 'abcdefg'`
- selection
  - `s1[0]`
- slicing
  - `s1[:5]`

- ```python
  sumDigits = 0
  for c in str(1952):
  	sumDigits += int(c)
  print(sumDigits)
  ```

  - 어떤 수를 가져와서 -> 문자열로 변환
  - 루프는 그 문자를 가져와 다시 정수로 변환하고 -> 더함
