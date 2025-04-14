from loguru import logger

labour = ['Ramesh', 'Suresh', 'Bunty', 'Sonty']
new_labour = ['lovly', 'Shayam']


#use of extend(to add two list ) note - '+' can be also used
labour.extend(new_labour)

logger.info(f"the exteded list is {labour}")

#fetching list using ':'
print("Actual list",labour)
print("to get seconf to fourth labours: ",labour[1:5])
print("to reverse the list ",labour[::-1])

#insert method
labour.insert(4,'Kite')
print("After appling insert 'method':",labour)

#.pop() method -
# '''it is used to delete valued.it is used in stack and queue if empty
#then last element will be deleted.also return the deleted element.
#if index is given then that item will be deleted

labour.pop(4)
print("After using '.pop() method'",labour)

#.remove()
# to deleted specific value in the list
labour.remove('Suresh')
print("After using '.remove() method'",labour)


# .split() method ***
api_endpoint = "https://azureportal/trueypz/controls/databricks/inside/yzpi"
api_address_list = api_endpoint.split("/")
logger.info(f"the splited api_endpoint form in list is : {api_address_list}")