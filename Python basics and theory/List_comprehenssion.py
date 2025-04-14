from loguru import logger

lst = [i for i in range(1, 31) if i % 2 == 0]
logger.info(f'the out of lst is {lst}')

even_odd = [f'{i} even' if i % 2 == 0 else f'{i} odd' for i in range(1, 11)]
logger.info(f'the result of even odd program is {even_odd}')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a_fruit = [i for i in fruits if 'a' in i]
print(a_fruit)

cap_fruit = [x.upper() for x in fruits if x in fruits]
logger.info(f'The fruits in capitol letters {cap_fruit}')
