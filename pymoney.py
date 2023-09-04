import sys
import pyrecords
import pycategories

categories = Categories()
records = Records() 
while True:
    command = input('What do you want to do (add / view / delete / view categories / find / exit)? ')
    if command == 'add':
        record = input('Add an expense or income record with category, description, and amount (separate by spaces):\n')
        records.add(record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view()
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')
