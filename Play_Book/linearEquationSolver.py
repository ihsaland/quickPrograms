def solve_linear(equation,var='x'):
    expression = equation.replace("=","-(")+")"
    grouped = eval(expression.replace(var,'1j'))
    return -grouped.real/grouped.imag

if __name__ == '__main__':
    print(solve_linear(input("Enter equation:")))