from loguru import logger

labour = ['Ramesh', 'Suresh', 'Bunty', 'Sonty']
new_labour = ['lovly', 'Shayam']

# to just simply add to list
total_labours = labour + new_labour
logger.info(f"adding to list {total_labours}")

# append
labour.append("Ram")
logger.info(f"the updated labour value after append method {labour} ")

#extend(to add new list to exsisting list
labour.extend(new_labour)
logger.info(f'The updated value after using extend method{labour}')

#insert
labour.insert(0,'Sohan')
logger.info(f'the updated value after using insert method{labour}')

#multidimensional list
labour_with_cost =[['Mahesh',700],['ramesh',400],['sohan',300],['ankit',400]]

logger.info(f"the cost of ramesh is {labour_with_cost[1][1]}",)
logger.info(f"the cost of mahesh is {labour_with_cost[0]}")
