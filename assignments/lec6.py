def squareRootBi(x, epsilon):
	assert x >= 0, "x must be non-negative , not" + str(x)
	assert epsilon > 0, "epsilon must be positive, not" + str(epsilon)
	low = 0
	high = max(x, 1.0)
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
  print("squareRootBi(4, 0.0001)")
  squareRootBi(4, 0.0001)
  print("squareRootBi(9, 0.0001)")
  squareRootBi(9, 0.0001)
  print("squareRootBi(0.25, 0.0001)")
  squareRootBi(0.25, 0.0001)

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
    
compareMethods()