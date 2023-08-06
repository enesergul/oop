class Calculator(object):
    
    def __init__(self,a,b):
        "initialize"
        self.value_1 = a
        self.value_2 = b 
    
    def add(self):
        "addition a+b"
        return self.value_1 + self.value_2
    
    def multiply(self):
        "multiplication a*b"
        return self.value_1 * self.value_2
    
c1 = Calculator(5,12)
add_result = c1.add()
multiply_result = c1.multiply()

print("add : {} multiply : {}".format(add_result,multiply_result))