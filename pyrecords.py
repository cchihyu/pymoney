import sys
from pycategories import*
import datetime as dt

class Record:
    """Represent a record."""
    def __init__(self,category,item,amount):
        self._category = category
        self._item = item
        self._amount = amount
    category = property(lambda self : self._category)
    item = property(lambda self : self._item)
    amount = property(lambda self : self._amount)
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        try:
            fh = open('record','r')# 1 error examination (does the file exist?)
            i = 1
            flag1 = True
            fh.seek(0)
            records = fh.readlines()
            for items in records:                                               # 2 error examination (any of the other lines cannot be interpreted as a record )
                if i != 1:
                    if len(items.split()) != 3:
                        raise IndexError
                    elif categories.is_category_valid(items.split()[0]) == False:
                        raise TypeError
                    items.split()[2] = int(items.split()[2])
                i += 1
        except (IndexError,ValueError,TypeError):
            print('Invalid format in record. Deleting the contents.')
            fh = open('record','w')
        except OSError:
            print('the file does not exist but we have created a new file')
            fh = open('record','w')
        fh = open('record','r')
        records = fh.readlines()
        if records == []:
            flag1 = False
            Total = input('How much money do you have? ')
            try:                                                                # 3 error examination(can the input be converted to interger )
                Total = int(Total)
            except ValueError:
                print('Invalid value for money. Set to 0 by default.')
                Total = 0
            records.append(str(Total)+'\n')
        else:
            print('Welcome back!')
        self._initial_money = records[0]
        self._records = records[1:]

    def view(self):    # 4.function
        """View the records."""
        print("Here's your expense and income records:\nCategory        Description          Amount")
        print('='*15 + ' ' + '='*20 + ' ' + '='*6)
        i = 1
        Sum = int(self._initial_money)
        for line in self._records:
            line = line.split()
            line[2] = int(line[2])
            print(f'{i}.{line[0]:<15s}{line[1]:<20s}{line[2]:<6d}')                           # use f-string to print each data
            Sum += line[2]
            i += 1
        print('='*43)
        print(f"Now you have {Sum} dollars.")

    def delete(self,x):                # 3.function
        """delete the record you want of the records"""
        try:                                                                    # 6 error examination (the user inputs in an invalid format in respect of your design)
            x = int(x)
        except ValueError:
            print('Invalid format. Fail to delete a record.')
            return records
        else:
            self._records = self._records[:x-1] + self._records[x:]

    def add(self,Amount,categories):
        """add a record like this meal breakfast -50"""
        try:                                                                    # 4 error examination(does the user input a string that can be split into a list of two strings)
            if len(Amount.split()) != 3:
                raise IndexError                                                    
            elif categories.is_category_valid(Amount.split()[0]) == False:
                raise TypeError
            else:
                Amount.split()[2] = int(Amount.split()[2])                      # 5 error examination ( can the second string after splitting be converted to integer.)
        except ValueError:
            print('Invalid value for money.')
            print('Fail to add a record.')
        except IndexError:
            print('The format of a record should be like this: meal breakfast -50.')
            print('Fail to add a record.')
        except TypeError:
            print('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.')
        else:
            self._records.append(Amount.split()[0] +' ' + Amount.split()[1] + ' ' + Amount.split()[2] + '\n')        # extend the list

    def find(self,target_category):
        """find the record with the category you want."""
        if target_category != False:
            result = filter(lambda n : n.split()[0] in target_category,self._records)
            print(f'Here\'s your expense and income records under category "{category}":')
            print('Category        Description          Amount')
            print('='*15 + ' ' + '='*20 + ' ' + '='*6)
            i = 1
            Sum = 0
            for line in result:
                line = line.split()
                line[2] = int(line[2])
                print(f'{i}.{line[0]:<15s}{line[1]:<20s}{line[2]:<6d}')                           # use f-string to print each data
                Sum += line[2]
                i += 1
            print('='*43)
            print(f"Now you have {Sum} dollars.")
        else:
            print('The specified category is not in the category list.\nYou can check the category list by command "view categories".')

    def save(self):    # 5.function
        """save the records to the file record"""
        with open('record','w') as fh:
            fh.write(self._initial_money)
            fh.writelines(self._records)