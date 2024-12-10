### Lecture 5: Floating point numbers, successive refinement, finding roots



Number

- int

  - Arbitrary precision

  - Type=L -> Long

    - ```
      a = 2 ** 1000
      a -> 10715.....776L
      
      b = 2 ** 999
      b -> 5357...688L
      
      a/b -> 2L
      ```

    - why 2L not 2?

      - 한번 긴정수(L) 을 얻으면, L의 형태를 이룸

- Float

  - floating point -- real

    - ```
      x = 0.1
      x -> 0.10000000000000001  (총 소숫점 17자리까지 표현)
      
      ```

    - 모든 현대 프로그래밍 언어처럼 파이썬은 IEEE 754 floatings point

    - Scientific notation

    - mantissa, exponent

      - 컴퓨터는 float 를 가수와 지수 쌍으로 표현한다
      - 가수는 1 <= mantissa < 2
      - 지수는 -1022 : 1023
      - 이것은 컴퓨터가 전형적으로 그 안에 워드들을 가지고 있다는 것과 워드가 64 Bits 로 표현된다는 점
        - 1 BIt sign (+/-)
        - 11 exponent
        - 52 mantissa
      - 17 decimal digits (17진법) 까지 표현할 수 있다

- 분수

  - 1/8 = 0.125

    - Base 10: `1.25 * 10^-1`
    - Base 2: `1.0 *2^-3 = 0.001`

  - 1/10 = 0.1

    - Base 1-: `1 * 10^1`
    - Base 2: `? -> 00011001100....`
      - 대부분의 컴퓨터에서 이진 근사치의 십진수 값을 프린트하려면 대부분 잘 프린트해준다

  - `repr()`

    - 파이썬은 무엇을 나타내려할 때 마다 repr 내장함수를 사용한다

    - int의 경우 문자로 바꿔주고, 스크린에 보여준다

    - float형의 경우 17자리의 수로 반올림 되고, 스크린에 보여준다

      - 그래서 0.1 이 0.10000000000000001 로 보여지는 것
      - 이 표현에 함축된 것이 무엇인가?

    - ```
      s = 0.0
      for i in range(10): s += 0.1
      
      s --> 0.99999999999999989
      print(s) --> 1.0
      ```

      - 마지막 두 숫자가 8 과 9 이다.
      - 에러가 축적됨, 시작할떈 작은 에러였고, loop 가 반복되면서 에러가 중첩되어 커졌다
      - print(s) 가 1.0 으로 표현된건, repr 함수가 17자리의 수로 반올림 하여 출력했기 때문이다.
        - 좋기도 하고 나쁘기도 하다.
        - 디버깅할때 혼란스러울 수 있음, 주의해야함

- Worry about `==` on floats

  - ```
    import math
    a = mat.sqrt(2)
    a -> 1.4142......51
    
    a*a == 2
    False
    
    a*a -> 2.0000000000004
    ```

    - a *a 는 컴퓨터내에서 근사치이기 때문이다.
    - 따라서 소수점을 비교할 떄 `==` 을 테스트하는건 굉장히 위험하다

  - ```
    abs(a*a-2.0) < epsilon
    ```

    - 위 두 식의 차가 입실론 내에 있다면 통과하는 것
    - 근사치에 대한 테스트의 올바른 방법

  - `==` = near!!!!!

    - float 비교는 같다가 아니라 근사치라는 것을 항상 인지해야 한다

- Might not be an exact answer

- can't enumerate all guesses

  - reals -> uncountable

- 숫자의 모든 state space 를 검증하기란 어렵다

- Guess, check, and improve 방법

  - 각 추측이 이전 추측보다 좋다는 가정을 갖고 계산하는 방법을 찾음

- Successive approximation

  - 구조

    - guess = initial guess
    - For iter in range(n):
      - if f(gess) close enough: return guess
      - else: guess = better guess
    - Error (n 번 수행하고도 좋은 답을 찾지 못할 경우)

  - 예제: Bisection method

    - 일직선상에 내가 찾고자 하는 답이 있다면 처음 추측보다 큰지/작은지 확인하고, 다음 게스로 넘어감

    - 계속 큰지/작은지 두 방향으로 정답의 범위를 좁혀나감

    - ```python
      def squareRootBi(x, epsilon):
      	assert x >= 0, "x must be non-negative , not" + str(x)
      	assert epsilon > 0, "epsilon must be positive, not" + str(epsilon)
      	low = 0
      	high = x
      	guess = (low + high) / 2.0
      	ctr = 1
      	while abs(quess**2 - x) > epsilon and ctr <= 100:
      		# print("low:", low, "hight:", hight, "guess:", guess)  # for debug
      		if guess**2 < x:
      			low = guess
      		else:
      			high = guess
      		guess = (low + high)/2.0
      		ctr += 1
      	assert ctr <= 100, "Iteration count exceeded"
      	print("Bi method. Num. Iterations:", ctr, "Estimate:", guess)
      	return guess
      ```

    - 