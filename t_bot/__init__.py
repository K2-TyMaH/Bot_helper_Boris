from user_funcs import *
from address_book import AddressBook

# a = {}
# b = address_book.keys()
# for i in b:
#     print(i)
#     print(address_book[i])

# if not b:
#     print('ye')
#address_book = AddressBook()
@input_error
def all_names():
    
        if address_book.keys():
            all_names = [name.title() for name in address_book.keys()]
            showing = dict(enumerate(all_names, 1))
            while True:
                try:
                    for k, v in showing.items():
                        print(f"{k} : {v}")
                    choosing = input("\nChoose № of this name (or skip it) >>> ")
                    print('')
                    if not choosing:
                        break
                    choosing = int(choosing)
                    needed_name = showing[choosing].lower()
                    needed_record = address_book[needed_name]
                    return needed_name, needed_record
                    
                    
                except ValueError:
                    print(f"'{choosing}' is not a number!")
                except KeyError:
                    print(f"'{choosing}' is out of range!")

        else:
            raise ValueError(f"Address book is empty")

a = all_names()

print(a)
