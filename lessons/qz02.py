


def main() -> None: 
    factorials: dict[int,int] = {}
    factorials[3] = factorial(3)
    factorials[4] = factorial(4)
    print(factorials)

def factorial(input: int) -> int:
    answer: int = 1
    for i in range(1, input+1):
        answer *= i
    return answer

if __name__ == "__main__":
    main()

def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for keys in inp:
        if inp[keys] % 2 == 0:
            inp[keys] += n
        if inp[keys] % 2 != 0:
            inp[keys] -= n
    return inp


def mystery(n: int) -> int:
    if n == 0:
        return 1
    else:
        return 2 * mystery(n-1)
    

    # base case: n = 0
    # mystery (n) = 1
    # recursive step: n>0
    # mystery (n) = 2 * mystery (n-1)