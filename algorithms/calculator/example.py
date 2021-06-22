"""
Programming for linguists

An example of using ReversePolishNotationConverter and ReversePolishNotationCalculator
"""
from algorithms.calculator.converter import ReversePolishNotationConverter
from algorithms.calculator.calculator import ReversePolishNotationCalculator

# Testing the Converter
rpn_coverter = ReversePolishNotationConverter()
example_1 = rpn_coverter.convert("7-2.5*3")  # 7 2.5 3 * -
example_2 = rpn_coverter.convert("(10-15)*3")  # 10 15 - 3 *
example_3 = rpn_coverter.convert("(1+2)*4+3")  # 1 2 + 4 * 3 +
example_4 = rpn_coverter.convert("3+4*2/(1-5)^2")  # 3 4 2 * 1 5 - 2 ^ / +

print(example_1, example_2, example_3, example_4, sep="\n")

# Testing the Calculator
rpn_calculator = ReversePolishNotationCalculator()
print(rpn_calculator.calculate(example_1))
print(rpn_calculator.calculate(example_2))
print(rpn_calculator.calculate(example_3))
print(rpn_calculator.calculate(example_4))
