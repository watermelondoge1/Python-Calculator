import operator

Repeat = True
prompts = {
    0: "Enter First Number or Stop to Stop\n",
    1: "Enter Second Number or Stop to Stop\n",
    2: "Enter Operation (+, -, *, /\n)",
}


def Get(A, func):
    A = A.strip()
    if A.lower() in ["stop", "s"]:
        global Repeat
        Repeat = False
        return "Escape"
    return func(A)


def Get_or_Go(A):
    try:
        return int(A)
    except ValueError:
        return None


def Get_Operator(B):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    B = B.strip()
    return operators.get(B)


while Repeat:
    escape = False
    result = {}
    for i in prompts:
        inp = input(prompts[i])
        if i == 2:
            result[i] = Get(inp, Get_Operator)
        else:
            result[i] = Get(inp, Get_or_Go)
        if result[i] == "Escape":
            escape = True
            break
        elif result[i] is None:
            escape = True
            break
        if escape:
            continue
    Answer = result[2](result[1], result[0])
    print(Answer)
