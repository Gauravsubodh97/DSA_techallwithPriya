from loguru import logger

labour = ['Ramesh','Suresh','Bunty','Sonty']
new_labour =['ram','Shayam']

# to just simply add to list
total_labours = labour + new_labour
print(total_labours)

#append
labour=labour.append("Ram")
logger.info("the updated labour value is ",labour)