### Lecture 2: Operators and operands; statements; branching, conditionals, and iteration



TODO

- operators: 연산자
- operands: 피연산자
- statement: 프로그램의 간단한 셋트
- branching: 조건문, 선언문



Primitive data - numbers & strings

- value & type

Combine in expressions - operands & operators

- interpreter - eval & print
- inside script - no print unless explicit

Type conversion

- ex. 3 + 'ab' -> TypeError

  - Not Syntax error but Static error

  - 문법은 맞음, 피연산자와 연산자 관점에서 문법적으로 맞음

  - 의미 문제를 발생하는데 연산자가 특정한 구조를 기대하고 있기 때문

- ex. str(3) + 'ab' -> '3ab'

Type checking

- 파이썬은 타입 검사를 하고 있고, 이것은 에러를 잡음
- 피연산자의 타입을 검사하고 나는 멈출꺼야 하고 말함
- 이는 computation 결과를 다른 블록으로 전달하기 전에 잘못된 부분을 미리 감지하고 멈추는 장점
- week vs strong typing
- 예
  - 'a' < 3 -> False
  - 4 < '3' -> True
  - '4' < '3' -> False

Type discipline (타입 지시)

- 코드 작성할 떄 연산자와 프로시저를 검사하는 습관에 빠짐
- 연산자에 적용하는 인수나 피연산자의 타입이 무엇인지에 대해 지시 받고 싶어짐
- 종종 명확하게 타입 지시하지 않으면 혼란에 빠질 가능성 높음
- 연산자는 계산하기 전에 타입을 먼저 본다
  - 9/5 -> 1 : 정수이기 때문
  - 3+4*5 -> 연산자 프로세스가 있다
    - Operator procedure

Variables & values Assignment

- x = 3 * 5
- y = 15
  - 바인딩
  - x, y 라는 변수를 기계 어딘가의 공간에 그 값으로 포인터를 만듬 (값의 링크)
- z = x
  - 링크 x 를 가져와서 ㅋ에게 같은 곳에 포인터를 줌, 값에 줌 not x

Type of variable - gets from values

- x -> integer

- python -> Dynamic types

  - 현재 값이 무엇인지에 따라 바뀐다, 즉 내가 현재 x = 'abc' 로 바꾸면 int -> string 으로 타입이 바뀐다
  - very bad

  - **don't change types arbitrarily (임의로 타입을 변경하지 말라)**

Variable used any place it's legal to use value

- 값을 사용하길 원하는 어디서나 변수를 사용하는 것은 허용 된다

Statement -> legal commands that Python can interpret

- print, assignment

Variable names - important to document

- keywords excluded

Straight line program

Branching program - can change the order of instructions based on some test (test usually value of variables)

- 어떤 세트에 기반하여 명령문의 순서를 바꿀 수 있는 것

Conditional

- : is important
- identifies a block
  - : start
  - carriage is end
- == 를 같다는 operator 로 쓰는 이유
  - 이미 = 는 binding (assingment) 로 사용되는 문법이기 때문

```
if <some test>:
	BLock of instructions
else:
	Block of instructions


```

Boolean combination - True, False

- and, or, not

브랜칭 프로그램

- 어떤 코드나 다른 것을 실행할지 결정하는 것 뿐인 간단함
  - 실행하는데 각 하나를 순서대로 하기 때문에 (직선 프로그램)
  - 간단한 브랜칭 코드는 각 명령문을 하나씩 실행할 것임
  - 그러므로 간단한 브랜칭 프로그램은 코드의 복잡성은 정수이다. 
  - 기껏해야 명령문들의 실제 수의 길이임

평균 나이 구하는 것에 대하여

- 나이를 모으고 다 더하고 나눔
- 레시피 관점에서
  - 언제까지 그걸 계속해? 어떤 조건이 충족될때까지 계속해

Iteration or Loop

- 테스트를 포함해야 한다
- 코드 내부의 값을 어떻게 변화 시킬지 알아야 가능
- 테스트는 변하고 있는 어떤 루프 변수를 포함해야 한다는 것, 무한 루프에서 피함

