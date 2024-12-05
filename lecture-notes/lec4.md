### Lecture 4: Decomposition and abstraction through functions; introduction to recursion



We have:

- assignment
- conditionals
- I/O
- looping constructs (for, while)



위 4가지로 모든 프로그래밍을 짤 수 있지만, 쉽게 짜기 위해선 아직 부족하다



We don't have:

- Decomposition (분해)
  - 코드에 구조를 두는 방법, 코드를 모듈로 나누는 방법
  - 모듈: 프로세스의 성분들을 분리, 재사용
- Abstraction (추상적 개념)
  - 자세한 내용을 숨기는 방법, 블랙박스
  - 입력을 하고 구체적인 출력을 얻음
  - 그러나 그 내부는 알 필요가 없음



Functions

- 함수의 핵심은 위 두가지를 모두 제공함
  - break up into modules (모듈로 나눔)
  - suppress detail (디테일을 숨김)
  - create "new primitives"
- Syntax
  - `def` -- keyword
  - `nmae(x)` -- formal parameters (=placeholder)
  - `return` -- keyword
    - stop computation
  - `None` -- special value
    - no value when computation finished
- Invoke function by passing in values for the parameters
  - `sqrt(16)`
    - binds x to 16 -- local
- Local bindings do not affect global bindings
  - Interpreters -- global bindings
  - Call function -- local table
    - 함수가 끝나면 테이블은 사라지고, 다시 전역으로 돌아온다



Barnyard problem

- 20 heads, 56 legs
  - numP + numC = 20
  - 4 x numP + 2 x numC = 56
- enuerate & check -- brute force algorithm (주먹구구 알고리즘)
  - solve 모듈 -- 실제 계산 작업이 수행되는 함수
  - barnYard 모듈 -- solve 모듈을 사용
    - 자세한 내용은 숨겨짐, 값을 구하기 위해 어디서든 solve 함수를 computation 으로 사용할 수 있음
- loop 를 통해 가능한 모든 경우의 수를 찾고, 만약 찾지 못할 경우를 대비하여 solutionFound = False 내부 변수를 초기화하고, 찾을 경우 수정
  - 함수 내부에서 이러한 작업들은 정보의 반환과 디버깅에 많음 도움을 줌



Recursion

- 프로그램을 좋은 사이즈의 덩어리로 나누는 방법에 대해 생각하는 매우 유용한 방법

- 아이디어

  - 문제를 가지고 그것을 같은 프로그램의 더 간단한 버전 + 실행할 수 있는 단계로 나누는 것

- base case -- simplest possible solution

- inductive step or recursive step (귀납적 단계 or 순환적 단계)

  - 문제를 같은 프로그램의 더 간단한 버전과 다른 단계들로 나눔

- palindrome problem (회문 문제)

  - 앞에서 읽으나 뒤에서 읽으나 동일한 단어

  - 문자열이 그 안에 요소가 없으면, 또는 하나만 있으면 회문이다 -- base case

  - 문자열이 길면, 두 끝 점의 무나열이 같은지 테스트, 회문 중간에 있는 모든 것들을 테스트해야한다 -- inductive step

  - 더 작은 문자열의 모든 예를 푸는 코드를 쓸 수 있으면, 더 큰 크기의 것도 풀 수 있음 (순환적 관점)

  - ````python
    def isPalindrome(s):
    	if len(s) <= 1: return True
    	else: return s[0] == s[-1] and isPalindrome(s[1:-1])
    ````

    - s라는 문자열을 넘겨 지역적 바인드함
    - 문자열이 1보다 작으면 옳음
    - 그렇지 않으면 문자열의 첫번쨰와 마지막 요소가 같은지 확인하고, 다시 isPalindrome 함수를 첫번째와 마지막을 제거한 문자열을 입력하여 테스트
    - 훌륭한 순환적 정의임

  - ```python
    def isPalindrome1(s, indent):
    	print(indent, "isPalindrome1 called with", s)
      if len(s) <= 1:
        print(indent, "About to return True from base case")
        return True
      else:
        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent+indent)
        print(indent, "About to return", ans)
        return ans
    ```

    - computation 이 무엇을 하는지에 주목
      - 내가 base case 에 있는지 확인해라
      - 그렇지 않으면 이걸 더 작은 computation 으로 줄이고, 계속 줄어들어 결국엔 내가  base case 에 있는지까지 감
    - 인자는 줄어들 것 (문자열) -> 다른 단계로 넘어감 -> 문자열이 1이 되었을때 base case 에 진입-> 이제 계산을 풀 수 있 -> true 를 리턴 -> 이미 두 끝점을 체크한 것을 고려할 때 또 true -> true ...  -> 돌아가서 계산을 품
      - 베이스 케이스를 정하고 -> 귀납적 단계가 그것을 같은 문제의 더 작은 버전으로 줄이는  -> 코드는 수렴되어 나에게 답을 줌

- Fibonacci

  - 첫번쨰 두 수를 정함 -> 0, 1

  - 다음 피보나지 수는 이전 두 수 의 합 -> 반복

    - Pairs(0) = 1
    - Pairs(1) = 1
    - Pairs(n) = Pairs(n-1) + Pairs(n-2)

  - ```
    def fib(x):
    	if x == 0 or x == 1: return 1
    	else: return fib(x-1) + fib(x-2)
    ```

- Recursive 의 핵심이 무엇인가?

  - 순환적으로 생각할 수 있으니까, 이제 비슷하게 그것들을 같은 문제의 더 간단한 버전들로 나눌 수 있음

- 마지막으로 핵심은

  - 선천적으로 반복인 것으로 생각하는 프로그램을 쓰길 시작하는  -- 루프를 통해 런
  - 그것은 문제들에 대해 생각하는 일반적인 방법이다. 
  - 어떤 문제들은 자연스럽게 그 방법으로 다뤄질 것
  - 순환의 방법에서 더욱 더 자연스럽게 생각되는 다른 문제들도 있음 -- 훌륭한 예제가 바로 Palindrome
    - 그것은 순환적으로 생각하는 쉬운 것, 오히려 반복적으로 생각하는 것이 더 어려움
  - 결국 어떤 것이 사용하기 옳은 것인지 결정하는 습관으로 가길 바람

