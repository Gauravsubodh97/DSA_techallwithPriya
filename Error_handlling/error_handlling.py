# try :-  Try test the block of code.
# except :- except block handdle the code and acording to error give output.
# finally :- finally block let you execute the code regardless of of the result of try - except block.

'''
try:
  it test the block that might give exception
except:
  code to handle the exception
else:
  if no exception then this block will execute its optional
finally:
  it will execute anyhow not dependent on try-except block
'''

# try:
#     print(x) # x is not defined so it will throw the error.
# except:
#     print('variable is not defined')


# ZeroDivisionError

# try:
#     n = 0
#     x =100
#     div = x/n
# except ZeroDivisionError as e:
#     print('Cant divide by Zero')
# else:
#     print(div)
# finally:
#     print('execution complete')

try:
    x = ['10','Twenty',30]
    total = sum(x[0],x[1])
except ArithmeticError as e:
    print('Arithmetic error',e)
except ValueError as e:
    print('Invalid value',e)
except TypeError as e:
    print('Invalid type ',e)
else:
    print('total sum is:-'+ total)
finally:
    print('finally block executed')

# hannling all exception in one code
try:
    # Code that might raise an exception
    # For example:
    x = ['10', 'Twenty', 30]
    total = sum(x[0], x[1])
    
    result = 10 / 0

except Exception as e:
    # This will catch any exception and print it
    print(f"handling all exception in one base code :{e}")
