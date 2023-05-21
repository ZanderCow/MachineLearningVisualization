import re

def parse_polynomial(function_string):
    terms = re.findall(r'([+-]?\s*\d*\.?\d*\s*x\^\d+|[+-]?\s*\d*\.?\d*\s*x|[+-]?\s*\d+\.?\d*)', function_string)
    coefficients = []
    powers = []

    for term in terms:
        term = term.replace(' ', '')
        if 'x' in term:
            if '^' in term:
                coef, power = term.split('x^')
                coef = '1' if coef in ['', '+'] else '-1' if coef == '-' else coef
                coefficients.append(float(coef))
                powers.append(int(power))
            else:
                coef = term.split('x')[0]
                coef = '1' if coef in ['', '+'] else '-1' if coef == '-' else coef
                coefficients.append(float(coef))
                powers.append(1)
        else:
            coefficients.append(float(term))
            powers.append(0)

    return coefficients, powers


print(parse_polynomial("x^3 -4x^2 +5"))