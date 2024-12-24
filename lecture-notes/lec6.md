### Lecture 6: Bisection methods, Newton/Raphson, introduction to lists 



테스트 함수를 만드는 이유

- 테스트 예시를 타이핑 하는 대신 함수를 쓰는게 나음

- 함수로 만듦으로써 만약 버그를 찾고 프로그램을 바꾼다면 단지 함수를 재사용하는 것으로 테스트 할 수 있음

- regression testings

- ```python
  def squareRootBi(x, epsilon):
  	assert x >= 0, "x must be non-negative , not" + str(x)
  	assert epsilon > 0, "epsilon must be positive, not" + str(epsilon)
  	low = 0
  	high = x
  	guess = (low + high) / 2.0
  	ctr = 1
  	while abs(guess**2 - x) > epsilon and ctr <= 100:
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
  	
  def testBi():
    print("squreRoot(4, 0.0001)")
    squreRoot(4, 0.0001)
    print("squreRoot(9, 0.0001)")
    squreRoot(9, 0.0001)
    print("squreRoot(0.25, 0.0001)")
    squreRoot(0.25, 0.0001)
  ```

- ```
  squareRootBi(4, 0.0001)
  Bi method. Num. Iterations: 1 Estimate: 2.0
  squareRootBi(9, 0.0001)
  Bi method. Num. Iterations: 18 Estimate: 2.999988555908203
  squareRootBi(0.25, 0.0001)
  Traceback (most recent call last):
    File "/Users/jkeun/dev/cs-study/mit-6-00/assignments/tmp.py", line 28, in <module>
      testBi()
    File "/Users/jkeun/dev/cs-study/mit-6-00/assignments/tmp.py", line 26, in testBi
      squareRootBi(0.25, 0.0001)
    File "/Users/jkeun/dev/cs-study/mit-6-00/assignments/tmp.py", line 16, in squareRootBi
      assert ctr <= 100, "Iteration count exceeded"
             ^^^^^^^^^^
  AssertionError: Iteration count exceeded
  ```

  - 이분법을 할 떄 lower bound ~ upper bound 사이에 있음
  - 그런데 우리가 처음에 lower bound 를 0으로 셋팅했고, guess 를 처음 X의 절반으로 셋팅했기 때문에, 절반에서 X사이의 값을 서치하지 못함
  - 그런데 실제 답은 upper bound 보다 더 위에 있음 --> `sqaure root(1/4) == 1/2 > 1/4`

- upper bound 를 수정

  - `high = max(x, 1)`
    - 만약 1보다 작은 어떤 값의 루트를 찾는 거라면 내 지역에 있음
  - 반복법은 고정된 것이 아니라는 점

- speed of conversion (수렴속도)

  - 이분법은 17세기까진 잘 사용하던 방법
  - 아이작 뉴턴, 조샙 랩슨의 미분 함수
  - sqrt(x)
    - 아래 방정식을 푸는 것
      - `F(guess) = guess**2 - x`
      - `F(guess) = 0`
    - `guess**2 - 16` 그래프를 보면 y 축의 0을 지나는 x를 구하는 것
    - 만약 첫 추측을 3이라 하면 3의 탄젠트 값을 구함
    - 다음 추측은 x축을 지나는 탄젠트 값임 -> 반으로 나누는 대신 다른 방법을 씀
    - 그러나 추측이 0이라면 탄젠트 값이 없음 -> 함정이 존재
  - 뉴턴 방법
    - 추측값의 지점에서 첫번째 f함수의 파생물이 탄젠트(기울기) 값임 -> `dy/dx`
    - 우리가 찾을 추측은 파생물이고, i'th 추측 값은 f' 의 i'th 추측 값의 2배와 같다
      - `f'(guess_i) = 2*guess_i`
    - i+1 의 추측은 i 추측에 1을 뺴는 것임
      - `guess_i+1 = guess_i - f(guess_i)/2*guess_i`
    - 실험
      - `f(3) = 9 - 16 = 7`
      - `guess_i+1 = 3 - (-7 / 2*3) = 4.1666`

- ```python
  def squreRootNR(x, epsilon):
      assert x >= 0, "x must be non-negative , not" + str(x)
      assert epsilon > 0, "epsilon must be positive, not" + str(epsilon)
      x = float(x)
      guess = x/2.0
      # guess = 0.001
      diff = guess**2 - x
      ctr = 1
      while abs(diff) > epsilon and ctr <= 100:
          # print("error:", diff, "guess:", guess)
          guess = guess - diff/(2.0*guess)
          diff = guess**2 - x
          ctr += 1
      assert ctr <= 100, "Iteration count exceeded"
      print("NR method. Num. Iterations:", ctr, "Estimate:", guess)
      return guess
  
  def compareMethods():
      print("SquareRoot(2, 0.01)")
      squareRootBi(2, 0.01)
      squreRootNR(2, 0.01)
      input()
      print("SquareRoot(2, 0.0001)")
      squareRootBi(2, 0.0001)
      squreRootNR(2, 0.0001)
      input()
      print("SquareRoot(2, 0.0000001)")
      squareRootBi(2, 0.0000001)
      squreRootNR(2, 0.0000001)
      input()
      print("SquareRoot(123456789, 0.0001)")
      squareRootBi(123456789, 0.0001)
      squreRootNR(123456789, 0.0001)
      input()
      print("SquareRoot(123456789, 0.000001)")
      squareRootBi(123456789, 0.000001)
      squreRootNR(123456789, 0.000001)
  ```

- ```
  SquareRoot(2, 0.01)
  Bi method. Num. Iterations: 8 Estimate: 1.4140625
  NR method. Num. Iterations: 3 Estimate: 1.4166666666666667
  
  SquareRoot(2, 0.0001)
  Bi method. Num. Iterations: 14 Estimate: 1.4141845703125
  NR method. Num. Iterations: 4 Estimate: 1.4142156862745099
  
  SquareRoot(2, 0.0000001)
  Bi method. Num. Iterations: 24 Estimate: 1.4142135381698608
  NR method. Num. Iterations: 5 Estimate: 1.4142135623746899
  
  SquareRoot(123456789, 0.0001)
  Bi method. Num. Iterations: 53 Estimate: 35136.4182864  # 강의 영상에서는 이렇게 출력되었음
  NR method. Num. Iterations: 18 Estimate: 35136.4182864  # 강의 영상에서는 이렇게 출력되었음
  
  SquareRoot(123456789, 0.000001)
  Bi method. Num. Iterations: 59 Estimate: 11111.111060555599
  NR method. Num. Iterations: 18 Estimate: 11111.111060555555
  ```

  - 첫번쨰
    - 이분법은 8번의 반복, 뉴턴랩슨은 3번의 반 -> 조금더 효율
    - 살짝 다른 답을 갖지만 둘다 e 오차 안에 있음
    - 다른 답이 나와도 모두 같은 스펙을 만족시킴
  - 두번쨰, 세번째
    - 더 정확한 답을 요구할떄(e 가 더 작을떄) -> 뉴턴랩슨은 오직 1,2번의 반복만 추가되서 답을 찾음
    - 더 어려운 문제에 더 낫지 않을까 생각함
    - 문제의 어려움을 확대시킴에 따라 좋은 방법과 안좋은 방법의 차이는 점점 더 커짐
    - 컴퓨터의 복잡도에 대한 개념임
  - 네번쨰, 다섯번쨰
    - 두 시도의 결과 숫자가 값자기 튐, 너무 다름 (ex. 35136)
    - Answer can be wrong
      - 컴퓨터의 말을 신처럼 믿지 말라, 믿을 이유가 없음
      - 오버플로우, 언더플로우, 부동소수점에 대해서 나중에 배울 것임



Non-scalar

- Immutable

  - Tuples

  - Strings

- Mutable

  - List
    - List 가 String 과 다른 두가지
      - 리스트는 변경할 수 있음
      - 밸류가 캐릭터일 필요가 없음
        - 숫자, 캐릭터, 또는 다른 리스트가 될 수 있음
  - `Techs = ["MIT", "Cal Tech"]` -- Object
    - Techs -> | "MIT" | "Cal Tech" |
  - `Ivy = ["Harvard", "Yale", "Brown"]`
    - Ivy -> | "Harvard" | "Yale" | "Brown" |
  - `Univs = []`
    - Univs -> |       |
  - `Univs.append(Techs)`
    - Univs -> || "MIT" | "Cal Tech" ||
    - 왜 리스트 안에 리스트로 존재하냐
      - Techs 객체 전체를 Univs 객체 안에 다시 넣은 것
    - 파이써닉 한 문법
      - Methods
      - 메소드는 다른 문법을 가진 함수에 대해 매우 복잡한 단어임
      - 만약 두 인자를 가지는 함수로 생각해보면
        - univs, techs 두 인자를 가짐
      - 그리고 메서드는 그 함수 호출을 쓰는 단지 다른 문법임
      - 강의 나중에 왜 우리가 이 문법을 사용해야 하는지 그리고 그것이 왜 완전히 파이썬 설계자에 의한 임의의 말도 안되는 결정인지 알게 될 것
  - `Univs.append(Ivy)`
    - Univs -> || "MIT" | "Cal Tech" |,  | "Harvard" | "Yale" | "Brown" ||
  - `for e in Univs:`
    - `print(e)`
    - `for c in e: print c`
      - | "MIT" | "Cal Tech" |
      - MIT
      - Cal Tech
      - | "Harvard" | "Yale" | "Brown" |
      - Harvard
      - Yale
      - Brown
    - 아주 강력한 개념임
      - 이 리스트들로 많은 것들을 할 수 있음
  - Flatten
    - `Univs = Techs + Ivy`
      - | "MIT" | "Cal Tech" | "Harvard" | "Yale" | "Brown" |
  - Remove
    - `Ivy.remove("Harvard")`
      - Ivy -> | "Yale" | "Brown" |
      - Ivy[0] -> "Yale"