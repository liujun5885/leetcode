def solution(input) -> int:
    stack = []

    stripped_input = []
    for i in input:
        if i.strip():
            stripped_input += i

    i = 0
    while i < len(stripped_input):
        if stripped_input[i] == "*":
            middle_result = stack.pop()
            middle_result *= int(stripped_input[i + 1])
            stack.append(middle_result)
            i += 1
        elif stripped_input[i] == "/":
            middle_result = stack.pop()
            middle_result //= int(stripped_input[i + 1])
            stack.append(middle_result)
            i += 1
        elif stripped_input[i] == '+':
            stack.append(int(stripped_input[i + 1]))
            i += 1
        elif stripped_input[i] == '-':
            stack.append(-1 * int(stripped_input[i + 1]))
            i += 1
        else:
            stack.append(int(stripped_input[i]))
        i += 1

    ans = 0
    for i in stack:
        ans += i
    return ans


def test_solution_01():
    input = "3+2 * 2"
    acutual = solution(input)
    expected = 7
    assert expected == acutual


def test_solution_02():
    input = "3+5/2*2-4"
    acutual = solution(input)
    print(acutual)
    expected = 3
    assert expected == acutual
