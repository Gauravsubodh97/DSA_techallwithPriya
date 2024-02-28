def fizzbuzz():
    for i in range(100):
        print(i)
        if i / 3 == 0:
          print('FIZZ')
        if i / 5 == 0:
          print('Buzz')


result =fizzbuzz()
print(result)