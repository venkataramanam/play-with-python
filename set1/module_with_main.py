def calculator(operator, left_operand, right_operand):
    '''
    The calulator coded here is a generic binary operator
    which accepts a operator function callback and invokes it
    '''
    return operator(left_operand, right_operand)

def add_operator(left_operand, right_operand):
    return left_operand + right_operand

def multiply_operator(left_operand, right_operand):
    return left_operand * right_operand

# The variable __name__ is a dunder variable which resolves to
# __main__ string if the module is run as a script using python
# interpreter. Otherwise, if module is imported into some other
# module, the __name__ resolves to the module name
# In a way this helps mimic adding main functions for testing
# modules, which is quite useful
if (__name__ == '__main__'):
    sum_4_5 = calculator(add_operator, 5, 4)
    print('Sum of 4 and 5 is {}'.format(sum_4_5))

    product_3_4 = calculator(multiply_operator, 3, 4)
    print('Product of 3 and 4 is ' + str(product_3_4))
