target = "atgacatgcacaagtatgcat"
key = "atgc"


def countSubStringMatch(target, key):
    count = 0
    start = 0
    while target.find(key, start) != -1:
        count += 1
        start = target.find(key, start) + 1
        print("where key start:", start)
    return count


def countSubStringMatchRecursive(target, key, indent=" "):
    """
        Recursive 구조를 쉽게 이해하는 방법 -> nested box 가 여러개 존재!
        
        count  <-- base case 에 도달하기 전까지 = resursive step 에서는 count 변수가 placeholder 로 존재
          └ 1 + box1
                  └ 1 + box2
                          └ 0  <-- base case 에 도달해서야 count 변수에 value assign 되어, 최종 값으로 수렴한다
    """
    count = 0
    print(indent, "Current target string:", target)
    if target.find(key) == -1:
        print(indent, "Current count:", count)
        return count
    else:
        count = 1 + countSubStringMatchRecursive(target[target.find(key)+1:], key, indent+indent)
        print(indent, "Current count:", count)
        return count



print("countSubStringMatch:", countSubStringMatch(target, key), "\n")
print("countSubStringMatchRecursive:", countSubStringMatchRecursive(target, key))