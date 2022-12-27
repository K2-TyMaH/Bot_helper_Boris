from record import Record
from sort import sort_files
import os
from address_book import address_book

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact doesn't exist, please try again."
        except ValueError as exception:
            ex_text = exception.args[0]
            if "not enough values to unpack" in ex_text:
                return "Wrong format. Must be '{command} {name} {new_value}'."
            elif "invalid literal for int" in ex_text:
                return "You must enter an integer number."
            return ex_text    #"Incorrect data"
        except IndexError:
            return "Wrong format. Must be '{command} {name} {value}'."
        except TypeError:
            return "Unknown command or parameters, please try again."
        except AttributeError:
            return "Can't find information about this contact or the data is incorrect."
        except StopIteration:
            return "There are no other numbers in the book."

    return inner


@input_error
def add_func(args: list) -> str:
    record = Record(args[0])
    if record.name.value not in address_book.keys():
        return address_book.add_record(record)
    else:
        return f"The contact with the name {args[0].title()} already exists in the AB."

@input_error
def edit_contact_name_func(args: list) -> str:
    existing_name = args[0]
    corrected_name = args[1]
    if not address_book:
        return f"'{existing_name.title()}' wasn't found in you address book."
    for value in address_book.values():
        if existing_name in address_book.keys():
            value.name.value = corrected_name
            address_book[corrected_name] = address_book.pop(existing_name)
            return f"'{existing_name.title()}' was changed to '{corrected_name.title()}'."
        else:
            return f"'{existing_name.title()}' wasn't found in you address book."

@input_error
def delete_record_func(args: list) -> str:
    contact_name = args[0]
    if contact_name in address_book.keys():
        return address_book.delete_record(contact_name)
    return f"Name '{contact_name}' doesn't exist in your book."

@input_error
def add_phone_func(args: list) -> str:
    contact_name = args[0]
    phone = args[1]
    if contact_name in address_book.keys() and phone not in [p.value for p in address_book[contact_name].phones]:
        return address_book[contact_name].add_phone(phone)
    else:
        return f"There is no '{contact_name}' in your AB or the '{phone}' already exists in the list."

@input_error
def change_phone_func(args: list) -> str:
    '''Змінює номер телефону контакту {name}'''
    
    name, new_phone = args   # Розпаковуємо аргументи
    record = address_book.data.get(name)   # Знаходимо {record} контакту {name}

    return record.change_phone(new_phone)
   

@input_error
def phone_func(args: list) -> str:
    name = args[0]
    record = address_book.data.get(name)
    if record:
        phones_list = [phone.value for phone in record.phones]
        return f"{record.name.value.title()} has this phones {phones_list}"
    return f"I didn't find any < {name} > in your Address Book."

@input_error
def del_phone_func(args: list) -> str:
    '''Видаляє існуючий номер телефону'''

    name = args[0]    
    record = address_book.data.get(name)
    
    return record.delete_phone()

@input_error
def add_mail_func(args: list) -> str:
    
    contact_name = args[0]
    email = args[1]
    
    if contact_name in address_book.keys() and email not in [e.value for e in address_book[contact_name].emails]:
        return address_book[contact_name].add_mail(email)
    else:
        return f"There is no '{contact_name}' in your AB or the '{email}' already exists in the list."

@input_error
def change_mail_func(args: list) -> str:

    name, new_mail = args
    record = address_book.data.get(name)

    return record.change_mail(new_mail)

@input_error
def delete_mail_func(args: list) -> str:

    name = args[0]
    record = address_book.data.get(name)

    return record.delete_mail()


@input_error
def show_all_func(*_) -> str:
    return address_book


@input_error
def add_birth_func(args: list) -> str:
    record = address_book[args[0]]
    if not record.birthday:
        return record.add_birthday(args[1])
    else:
        return f'The name {args[0].title()} is not exist or this guy already has a birthday.'


@input_error
def change_birth_func(args: list) -> str:
    record = address_book[args[0]]
    if record.birthday:
        return record.change_birthday(args[1])
    else:
        return f'The name {args[0].title()} is not exist. Please add first'

@input_error
def del_birth_func(args: list) -> str:
    record = address_book[args[0]]
    if record.birthday:
        return record.delete_birthday()
    else:
        return f"The name {args[0].title()} isn't in AB or there is no birthday to delete."

@input_error
def days_to_birth_func(args: list) -> str:
    record = address_book[args]
    if record.birthday != None:
        return f"{args.title()}'s birthday will be in '{record.days_to_birthdays()}' days."
    else:
        return f"'{args.title()}' doesn't have a birthday"


@input_error
def all_birth_func(args) -> str:
    days = int(args[0])
    result = "\n"
    bdays = address_book.all_birthdays(days)
    if not bdays:
        return f"No one from your book will have a birthday in '{days}' days."
    for data in bdays:
        result += " - ".join(data)
        result += "\n"
    result = result[0:-1]
    return result

@input_error
def add_note_func(args: list) -> str:
    record = address_book[args[0]]
    return record.add_note(args[1:])

@input_error
def change_note_func(args: list) -> str:
    name, *new_note = args 
    record = address_book.data.get(name)
    return record.change_note(new_note)

@input_error
def del_note_func(args: list) -> str:
    name=args[0]
    record = address_book.data.get(name)
    return record.delete_note()

@input_error
def add_tag_func(args: list) -> str:
    '''Функція створює один раз теги'''
    record = address_book[args[0]]
    
    return record.add_tag(args[1:])

@input_error
def edit_tag_func(args: list) -> str:
    '''Функція редагує існуючи теги'''
    record = address_book[args[0]]
    if record.tag:
        while True:
            print(f'The current list of tags is {record.tag.value}')
            act = int(input('Please choose the way to edit tags: 1)remove any tag; 2)add any tag; 3)exit >>>'))
            if act == 1:
                record.del_tag()
                continue
            elif act == 2:
                new_line_tag = input('Please type new tags, with # and separated by \'space\'>>>')
                new_list_tag = new_line_tag.split(' ')
                record.change_tag(new_list_tag)
                continue
            elif act == 3:
                return f''
            else:
                print('You enter a wrong number. Please try again')
                continue
    else:
        return f'Please verify your command or Tag are empty, please fill it'

@input_error
def delete_tags_func(args: list) -> str:
    '''Функція видаляє всі теги'''
    record = address_book.data.get(args[0])
    return record.delete_tags()

@input_error
def find_func(args) -> str:
    return address_book.search_in_contact_book(args)

@input_error
def sort_func(*_) -> str:
    user_input = input(
        'Enter "1" if you want to sort files in the current folder.\n'
        'Enter "2" if you want to choose another folder.\n'
    )
    if user_input == '1':
        return sort_files(os.getcwd())
    elif user_input == '2':
        user_path = input('Enter a path: ')
        return sort_files(user_path)
    else:
        return f'You have to enter "1" or "2".'

@input_error
def exit_func(*_)-> str:
    """The function close bot."""
    return exit("\nGood bye! \n\nSee you later!  ͡° ͜ʖ ͡° \n")


