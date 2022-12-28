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
                    print(color(f"\nThe contact '{new_contact_name.title()}' successfully added {SMILE_LIST[1]}", "g"))
                    print(color(f"\nDo you wanna add information about '{new_contact_name.title()}' ? {SMILE_LIST[8]}", "b"))
                    new_contact_name = new_contact_name.lower()
                    againer(add_main_atributes, new_contact_name, new_record)
                    boris()
                else:
                    print(color(f"\nThe contact with the name '{new_contact_name.title()}' already exists in the AB {SMILE_LIST[2]}", "rb"))
            else:
                boris()
                
        elif choosing == "2":
            print(checker())
        
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
            print(color(all_birth_func([input_days]), "rb"))

        elif choosing == "6":
            print('')
            print(color(sort_func(), "rb"))
        
        elif choosing == "7":
            exit_func()
        
        else:
            print('')
            print(color(f"What is it '{choosing}' ??? {SMILE_LIST[3]}?", "rb"))


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
            print(color(days_to_birth_func(name), "rb"))
            break

        elif choosing == "6":
            print(color(address_book.delete_record(name), "rb"))
            boris()

        elif choosing == "7":
            break
        
        else:
            print(color(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?", "r"))
    
    print(color(f"\nDo you wanna CHECK something else in the '{name.title()}' ? {SMILE_LIST[8]}", "gb"))
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
                print(color(add_phone_func([name, value]), "rb"))
                break
            else:
                break
        
        elif choosing == "2":
            value = input(f"Write birthday for '{name.title()}' ('year.month.day') >>> ")
            print('')
            if value:
                print(color(add_birth_func([name, value]), "rb"))
                break
            else:
                break
        
        elif choosing == "3":
            value = input(f"Write email for '{name.title()}' >>> ")
            print('')
            if value:
                print(color(add_mail_func([name, value]), "rb"))
                break
            else:
                break

        elif choosing == "4":
            value = input(f"Write one #tag or #tags (separatet by ' ') for '{name.title()}' >>> ")
            print('')
            if value:
                value = value.split(' ')
                print(color(search_entry.add_tag(value), "rb"))
                break
            else:
                break

        elif choosing == "5":
            value = input(f"Write note for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.note:
                    print(color(add_note_func([name, value]), "rb"))
                    break
                else:
                    old_note = search_entry.note.value
                    note = old_note + " " + value   
                    search_entry.note = Note(note)
                    print(color(f"The note '{value}' was added to the contact '{name.title()}'.", "rb"))
                    break
            else:
                break
        
        elif choosing == "6":
            break

        else:
            print(color(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?", "r"))

    print(color(f"\nDo you wanna ADD something else to the '{name.title()}' ? {SMILE_LIST[8]}", "gb"))
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
            print(color(edit_contact_name_func([name, new_name.lower()]), "rb"))
            boris()

        elif choosing == "2":
            value = input(f"Write new phone for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.phones:
                    print(color(add_phone_func([name, value]), "rb"))
                    break
                else:
                    print(color(change_phone_func([name, value]), "rb"))
                    break
            else:
                break
        
        elif choosing == "3":
            value = input(f"Write new birthday for '{name.title()}' ('year.month.day') >>> ")
            print('')
            if value:
                if not search_entry.birthday:
                    print(color(add_birth_func([name, value]), "rb"))
                    break
                else:
                    print(color(change_birth_func([name, value]), "rb"))
                    break
            else:
                break
        
        elif choosing == "4":
            value = input(f"Write new email for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.emails:
                    print(color(add_mail_func([name, value]), "rb"))
                    break
                else:
                    print(color(change_mail_func([name, value]), "rb"))
                    break
            else:
                break

        elif choosing == "5":
            value = input(f"Write one #tag or #tags (separatet by ' ') for '{name.title()}' >>> ")
            print('')
            if value:
                value = value.split(' ')
                print(color(search_entry.add_tag(value), "rb"))
                break
            else:
                break

        elif choosing == "6":
            value = input(f"Write note for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.note:
                    print(color(add_note_func([name, value]), "rb"))
                    break
                else:
                    old_note = search_entry.note.value
                    note = old_note + " " + value   
                    search_entry.note = Note(note)
                    print(color(f"The note '{value}' was added to the contact '{name.title()}'.", "rb"))
                    break
            else:
                break
        
        elif choosing == "7":
            break

        else:
            print(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?")
    
    print(color(f"\nDo you wanna Change something else in the '{name.title()}' ? {SMILE_LIST[8]}", "gb"))
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
            print(color(del_phone_func([name]), "rb"))
            break
        
        elif choosing == "2":
            print(color(del_birth_func([name]), "rb"))
            break
        
        elif choosing == "3":
            print(color(delete_mail_func([name]), "rb"))
            break

        elif choosing == "4":
            print(color(f"\nDo you want to remove one or ALL! tags from the '{name.title()}' ? {SMILE_LIST[8]}", "b"))
            print(color("\n1 : Remove only one tag ", "g"))
            print(color("2 : !!! Delete all tags !!! ", "g"))
            print(color("3 : I changed my mind, I don't want to delete anything", "g"))
            while True:     
                choosing_t = input("\nChoose № >>> ")
                print('') 
                if not choosing_t:
                    break  
                elif choosing_t == "1":
                    print(color(search_entry.del_tag(), "r"))
                    break           
                elif choosing_t == "2":
                    print(color(search_entry.delete_tags(), "rb"))
                    break
                elif choosing_t == "3":
                    break
                else:
                    print(color(f"\nWhat is it '{choosing_t}' ??? {SMILE_LIST[3]}?", "r"))
            break            

        elif choosing == "5":
            if search_entry and search_entry.note.value:
                deleted_note = search_entry.note.value
                search_entry.note = Note('')
                print(color(f"The note '{deleted_note}' of contact '{name.title()}' was deleted.", "rb"))
                break
            else:
                print(color(f"Note list of '{name.title()}' is already empty.", "rb"))
                break
        
        elif choosing == "6":
            break

        else:
            print(color(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?", "r"))
    
    print(color(f"\nDo you want to DELETE something else in '{name.title()}' ? {SMILE_LIST[8]}", "gb"))
    againer(del_main_atributes, name, search_entry)




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

def show_contact(c_info):
    contact_info = AddressBook()
    contact_info.add_record(c_info)
    return contact_info

def dobriy_den():
    f1 = color("Dobriy den, everybody!", "bb")
    f2 = color("Boris Jonson", "yb")
    print(f"\n\n{f1} I'm {f2} from London {SMILE_LIST[4]}")
    print(f"\nOh, sorry, I'm joking {SMILE_LIST[5]} I'm just a cool bot from Ukraine {SMILE_LIST[6]} ")

def slava_ukraine():
    slava = color("♥♥♥♥♥♥♥ SLAVA UKRAINI ♥♥♥♥♥♥♥", "rb")
    print(f"\n{slava}")
    line = "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    sky = color(line, 'b')
    wheat_field = color(line, 'y')
    print(f"{sky}\n" * 4 + f"{wheat_field}\n" * 4)
    
def smile_list_funk():
    SMILE_LIST = ["(⌐■_■)", "♥", "(-_-)", "(o_O)", "♥ (ʘ‿ʘ) ♥", "^▿^", "(◕‿◕)", "(° ͜ʖ°)", "(•¿•)"]
    new_SMILE_LIST = []
    for smile in SMILE_LIST:
        smile = color(smile, "p")
        new_SMILE_LIST.append(smile)
    return new_SMILE_LIST
SMILE_LIST = smile_list_funk()
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
    print(color("1", "b") + " : " + color("Yes", "g"))
    print(color("2", "b") + " : " + color("No", "r"))
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
            print(color(f"\nWhat is it '{choosing}' ??? ", "rb") + color(f"{SMILE_LIST[3]}?"))

@input_error
def checker():
    
    print(color("1", "b") + " : " + color("I want to enter the desired name myself.", "g"))
    print(color("2", "b") + " : " + color("Select a name from the list: ", "g"))
    print(color("3", "b") + " : " + color("Return to preavious menu", "g"))
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
                print(color(f"\nWhat would you like to do with contact '{name.title()}' {SMILE_LIST[8]}\n", "bb"))
                main_comands(name, search_entry)
            else:
                for n, v in address_book.items():

                    if (name in n.split() or
                            name.title() in n.split()):
                        search_entry = v
                        print(color(f"What would you like to do with contact '{name.title()}' {SMILE_LIST[8]}\n", "bb"))
                        main_comands(n, search_entry)

                return color(f"\nI didn't find any contact with name '{name.title()}' "
                                     f"in AB {SMILE_LIST[2]}", "rb")
            break
        
        elif choosing == "2":
            all_names_list = all_names()
            if all_names_list:
                name, search_entry = all_names_list
                print(color(f"What would you like to do with contact '{name.title()}' {SMILE_LIST[8]}\n", "bb"))
                main_comands(name, search_entry)
                break
            else:
                break

        if choosing == "3":
            break

        else:
            print(color(f"\nWhat is it '{choosing}' ??? {SMILE_LIST[3]}?", "r"))

def show_comander(showing):
    for k, v in showing.items():
            k = color(k, "b")
            v = color(v, "g")
            print(f"{k} : {v}")

