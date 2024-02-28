from loguru import logger


# Even odd

number = int(input('please enter the number to check : '))

if number%2 ==0:
    logger.info('The number is even')
elif number % 2 != 0:
    logger.info('The number is odd')
else:
    logger.info('The input is invaid')