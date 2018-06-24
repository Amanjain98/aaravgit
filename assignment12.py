try:
    a = 3
    if a<4:
         b = a//a-3
         if(a-3 ==0):
             raise ArithmeticError()
except ArithmeticError:
    print("Division by Zero Error")
else:
    print("Success")
