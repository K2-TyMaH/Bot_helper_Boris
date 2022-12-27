from user_funcs import *
from fields_for_record import Note
from address_book import AddressBook

FUNC_1_LIST = ("Add new contact", "Check contact", \
    "Find information in the book", "Show all book", "Show upcoming birthdays", \
        "Sort the garbage in my folder", "Exit")
FUNC_2_LIST = ("Show information about this contact", "Add information", "Change information", \
    "Delete information", "Check how many days to birthday", \
        "Remove contact from book", "Return to the previous menu")
ATTRIBUTES_LIST = ("Phone", "Birthday", "Email", "Tag", "Note", "Return to the previous menu")


@input_error
def boris():
    
    while True:
        helper = color("How can I help you? •௰•", "bb")
        enter = color("press Enter", "yb")
        print(f"\n{helper}")
        print(f"P.S. You can always {enter} if you want to skip selection {SMILE_LIST[0]}\n")
        
        showing = dict(enumerate(FUNC_1_LIST, 1))
        show_comander(showing)
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            exit_func()
        
        elif choosing == "1":
            new_contact_name = input("\nWrite name of your new contact >>> ")
            print('')
            if new_contact_name:
                new_record = Record(new_contact_name.lower())
                if new_record.name.value not in address_book.keys():
                    print('')
                    address_book.add_record(new_record)
                    print(f"\nThe contact '{new_contact_name.title()}' successfully added {SMILE_LIST[1]}")
                    print(f"\nDo you wanna add information about '{new_contact_name.title()}' ? {SMILE_LIST[8]}")
                    new_contact_name = new_contact_name.lower()
                    againer(add_main_atributes, new_contact_name, new_record)
                else:
                    print(f"\nThe contact with the name '{new_contact_name.title()}' already exists in the AB {SMILE_LIST[2]}")
            else:
                boris()
                
        elif choosing == "2":
            checker()
        
        elif choosing == "3":
            information = input("\nWhat are you looking for? >>> ")
            print('')
            print(address_book.search_in_contact_book(information))
        
        elif choosing == "4":
            print('')
            print(address_book)

        elif choosing == "5":
            input_days = input("\nHow many days ahead should I look? >>> ")
            print('')
            print(all_birth_func([input_days]))

        elif choosing == "6":
            print('')
            print(sort_func())
        
        elif choosing == "7":
            exit_func()
        
        else:
            print('')
            print(f"What is it '{choosing}' ??? {SMILE_LIST[3]}?")


@input_error
def main_comands(name, search_entry):
    showing = dict(enumerate(FUNC_2_LIST, 1))
    show_comander(showing)
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            break
        
        elif choosing == "1":
            print(show_contact(search_entry))
            break

        elif choosing == "2":
            add_main_atributes(name, search_entry)
            break
        
        elif choosing == "3":
            change_main_atributes(name, search_entry)
            break
        
        elif choosing == "4":
            del_main_atributes(name, search_entry)
            break

        elif choosing == "5":
            print(days_to_birth_func(name))
            break

        elif choosing == "6":
            print(address_book.delete_record(name))
            break

        elif choosing == "7":
            break
        
        else:
            print(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?")
    
    print(f"\nDo you wanna CHECK something else in the '{name.title()}' ? {SMILE_LIST[8]}")
    againer(main_comands, name, search_entry)

@input_error
def add_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    show_comander(showing)
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            break
        
        elif choosing == "1":
            value = input(f"Write phone for '{name.title()}' >>> ")
            print('')
            if value:
                print(add_phone_func([name, value]))
                break
            else:
                break
        
        elif choosing == "2":
            value = input(f"Write birthday for '{name.title()}' ('year.month.day') >>> ")
            print('')
            if value:
                print(add_birth_func([name, value]))
                break
            else:
                break
        
        elif choosing == "3":
            value = input(f"Write email for '{name.title()}' >>> ")
            print('')
            if value:
                print(add_mail_func([name, value]))
                break
            else:
                break

        elif choosing == "4":
            value = input(f"Write one #tag or #tags (separatet by ' ') for '{name.title()}' >>> ")
            print('')
            if value:
                value = value.split(' ')
                print(search_entry.add_tag(value))
                break
            else:
                break

        elif choosing == "5":
            value = input(f"Write note for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.note:
                    print(add_note_func([name, value]))
                    break
                else:
                    old_note = search_entry.note.value
                    note = old_note + value   
                    search_entry.note = Note(note)
                    print(f"The note < {value} > was added to the contact < {name.title()} >.")
                    break
            else:
                break
        
        elif choosing == "6":
            break

        else:
            print(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?")

    print(f"\nDo you wanna add something else to the '{name.title()}' ? {SMILE_LIST[8]}")
    againer(add_main_atributes, name, search_entry)
    

@input_error
def change_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 2))
    print(color("1", "b") + " : " + color("Name", "g"))
    show_comander(showing)
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            break
        
        elif choosing == "1":
            new_name = input(f"Write NEW NAME for '{name.title()}' >>> ")
            print('')
            print(edit_contact_name_func([name, new_name.lower()]))
            boris()

        elif choosing == "2":
            value = input(f"Write new phone for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.phones:
                    print(add_phone_func([name, value]))
                    break
                else:
                    print(change_phone_func([name, value]))
                    break
            else:
                break
        
        elif choosing == "3":
            value = input(f"Write new birthday for '{name.title()}' ('year.month.day') >>> ")
            print('')
            if value:
                if not search_entry.birthday:
                    print(add_birth_func([name, value]))
                    break
                else:
                    print(change_birth_func([name, value]))
                    break
            else:
                break
        
        elif choosing == "4":
            value = input(f"Write new email for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.emails:
                    print(add_mail_func([name, value]))
                    break
                else:
                    print(change_mail_func([name, value]))
                    break
            else:
                break

        elif choosing == "5":
            value = input(f"Write one #tag or #tags (separatet by ' ') for '{name.title()}' >>> ")
            print('')
            if value:
                value = value.split(' ')
                print(search_entry.add_tag(value))
                break
            else:
                break

        elif choosing == "6":
            value = input(f"Write note for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.note:
                    print(add_note_func([name, value]))
                    break
                else:
                    old_note = search_entry.note.value
                    note = old_note + value   
                    search_entry.note = Note(note)
                    print(f"The note < {value} > was added to the contact < {name.title()} >.")
                    break
            else:
                break
        
        elif choosing == "7":
            break

        else:
            print(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?")
    
    print(f"\nDo you wanna change something else to the '{name.title()}' ? {SMILE_LIST[8]}")
    againer(change_main_atributes, name, search_entry)

@input_error
def del_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    show_comander(showing)
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            break
        
        elif choosing == "1":
            print(del_phone_func([name]))
            break
        
        elif choosing == "2":
            print(del_birth_func([name]))
            break
        
        elif choosing == "3":
            print(delete_mail_func([name]))
            break

        elif choosing == "4":
            print(f"\nDo you want to remove one or ALL! tags from the '{name.title()}' ? {SMILE_LIST[8]}")
            print("\n1 : Remove only one tag ")
            print("2 : !!! Delete all tags !!! ")
            print("3 : I changed my mind, I don't want to delete anything")
            while True:     
                choosing_t = input("\nChoose № >>> ")
                print('') 
                if not choosing_t:
                    break  
                elif choosing_t == "1":
                    print(search_entry.del_tag())
                    break           
                elif choosing_t == "2":
                    print(search_entry.delete_tags())
                    break
                elif choosing_t == "3":
                    break
                else:
                    print(f"\nWhat is it '{choosing_t}' ??? {SMILE_LIST[3]}?")
            break            

        elif choosing == "5":
            if search_entry:
                deleted_note = search_entry.note.value
                search_entry.note = Note('')
                print(f"The note '{deleted_note}' of contact '{name.title()}' was deleted.")
                break
            else:
                print(f"Note list of '{name.title()}' is already empty.")
                break
        
        elif choosing == "6":
            break

        else:
            print(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?")
    
    print(f"\nDo you want to delete something else in '{name.title()}' ? {SMILE_LIST[8]}")
    againer(del_main_atributes, name, search_entry)






def show_contact(c_info):
    contact_info = AddressBook()
    contact_info.add_record(c_info)
    return contact_info

def dobriy_den():
    f1 = color("Dobriy den everybody", "bb")
    f2 = color("Boris Jonson", "yb")
    print(f"\n\n{f1}, I'm {f2} from London {SMILE_LIST[4]}")
    print(f"\nOh, sorry, I'm joking {SMILE_LIST[5]} I'm just a cool bot {SMILE_LIST[6]} ")    

def slava_ukraine():
    slava = color("♥♥♥ SLAVA UKRAINI ♥♥♥", "rb")
    print(f"\n{slava}")
    line = "■■■■■■■■■■■■■■■■■■■■■■"
    sky = color(line, 'b')
    wheat_field = color(line, 'y')
    print(f"{sky}\n" * 4 + f"{wheat_field}\n" * 4)
    

@input_error
def all_names():
    
        if address_book.keys():
            all_names = [name.title() for name in address_book.keys()]
            showing = dict(enumerate(all_names, 1))
            while True:
                try:
                    show_comander(showing)
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

def againer(func, name, search_entry):
    print(color("1", "b") + " : " + color("Name", "g"))
    print("2 : No")
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            func(name, search_entry)
            break
        
        elif choosing == "2":
            break

        else:
            print(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?")

@input_error
def checker():
    
    print("1 : I want to enter the desired name myself.")
    print("2 : Select a name from the list: ")
    print("3 : Return to preavious menu")
    while True:    
        
        choosing = input("\nChoose № >>> ")
        print('')
        if not choosing:
            break
        
        elif choosing == "1":
            name = input("Which contact would you like to check? >>> ")
            name = name.lower()
            search_entry = address_book.data.get(name)
            if search_entry:
                print(f"\nWhat would you like to do with contact '{name.title()}' {SMILE_LIST[8]}\n")
                main_comands(name, search_entry)
            else:
                print(f"\nI didn't find any contact with name '{name.title()}' in AB {SMILE_LIST[2]}")
            break
        
        elif choosing == "2":
            all_names_list = all_names()
            if all_names_list:
                name, search_entry = all_names_list
                print(f"What would you like to do with contact '{name.title()}' {SMILE_LIST[8]}\n")
                main_comands(name, search_entry)
                break
            else:
                break

        if choosing == "3":
            break

        else:
            print(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?")

def color(message: str, color: str) -> str:
    '''bb - blue Bold, r - red, g - green, p - purple'''

    color_code = {
        "bb": "\033[1m\033[34m{}\033[0m",
        "b": "\033[34m{}\033[0m",
        "yb": "\033[1m\033[33m{}\033[0m",
        "y": "\033[33m{}\033[0m",
        "gb": "\033[1m\033[32m{}\033[0m",
        "g": "\033[32m{}\033[0m",
        "rb": "\033[1m\033[31m{}\033[0m",
        "r": "\033[31m{}\033[0m",
        "pb": "\033[1m\033[35m{}\033[0m",
        "p": "\033[35m{}\033[0m"
        }
    return color_code[color].format(message)  

def smile_list_funk():
    SMILE_LIST = ["(⌐■_■)", "♥", "(-_-)", "(o_O)", "♥ (ʘ‿ʘ) ♥", "^▿^", "(◕‿◕)", "(° ͜ʖ°)", "(•¿•)"]
    new_SMILE_LIST = []
    for smile in SMILE_LIST:
        smile = color(smile, "p")
        new_SMILE_LIST.append(smile)
    return new_SMILE_LIST
SMILE_LIST = smile_list_funk()

def show_comander(showing):
    for k, v in showing.items():
            k = color(k, "b")
            v = color(v, "g")
            print(f"{k} : {v}")

