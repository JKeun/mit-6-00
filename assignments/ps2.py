print("a b c n step")

step_range = range(1, 5)
for step in step_range:
    n_range = range(30+6*(step-1), 30+6*step)
    for n in n_range:
        a_max = n // 6
        b_max = n // 9
        c_max = n // 20
        
        for c in range(0, c_max+1):
            for b in range(0, b_max+1):
                for a in range(0, a_max+1):
                    expected = 6 * a + 9 * b + 20 * c
                    if expected == n:
                        print(a, b, c, n, step)
                        
 
