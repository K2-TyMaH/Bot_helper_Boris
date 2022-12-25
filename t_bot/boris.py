from user_funcs import *
from fields_for_record import Note

FUNC_1_LIST = ("Add new contact", "Check contact", \
    "Find information in the book", "Show all book", "Show upcoming birthdays", \
        "Sort the garbage in my folder", "Exit")
FUNC_2_LIST = ("Add information", "Change information", "Delete information", \
    "Check how many days to birthday", "Remove contact from book", "Return to the previous menu")
ATTRIBUTES_LIST = ("Phone", "Birthday", "Email", "Tag", "Note", "Return to the previous menu")

@input_error
def boris():
    def fast_adding(new_contact_name, new_record):
            print(f"\nDo you wanna add information about '{new_contact_name.title()}' ? (•¿•)")
            print("1 : Yes")
            print("2 : No")
            new_contact_name = new_contact_name.lower()
            while True:    
                choosing_a = input("\nChoose № >>> ") 
                if not choosing_a:
                    break
                elif choosing_a == "1":
                    add_main_atributes(new_contact_name, new_record)
                    break
                elif choosing_a == "2":
                    break
                else:
                    print(f"\nWhat is it '{choosing_a}' ??? (o_O)?")

    f1 = blue_color("Dobriy den everybody")
    f2 = blue_color("Boris Jonson")
    print(f"\n\n{f1}, I'm {f2} from London ♥ (ʘ‿ʘ) ♥")
    print("\nOh, sorry, I'm joking ^▿^ I'm just a cool bot (◕‿◕) ")
    while True:
        f3 = blue_color("How can I help you? •௰•")
        print(f"\n{f3}")
        print("P.S. You always can skip any comand if you want to exit (⌐■_■)\n")
        
        showing = dict(enumerate(FUNC_1_LIST, 1))
        for k, v in showing.items():
            print(f"{k} : {v}")
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            exit_func()
        
        elif choosing == "1":
            new_contact_name = input("\nWrite name of your new contact >>> ")
            print('')
            new_record = Record(new_contact_name.lower())
            if new_record.name.value not in address_book.keys():
                print('')
                address_book.add_record(new_record)
                print(f"\nThe contact '{new_contact_name.title()}' successfully added ♥")
                fast_adding(new_contact_name, new_record)
            else:
                print(f"\nThe contact with the name '{new_contact_name.title()}' already exists in the AB (-_-)")
        
        elif choosing == "2":
            name = input("\nWhich contact would you like to check? >>> ")
            name = name.lower()
            search_entry = address_book.data.get(name)
            if search_entry:
                print(f"\nWhat would you like to do with contact '{name.title()}' (° ͜ʖ°)\n")
                main_comands(name, search_entry)
            else:
                print(f"\nI didn't find any contact with name '{name.title()}' in AB (-_-)")
        
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
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")


@input_error
def main_comands(name, search_entry):
    showing = dict(enumerate(FUNC_2_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            break
        
        elif choosing == "1":
            add_main_atributes(name, search_entry)
            break
        
        elif choosing == "2":
            change_main_atributes(name, search_entry)
            break
        
        elif choosing == "3":
            del_main_atributes(name, search_entry)
            break

        elif choosing == "4":
            print(days_to_birth_func(name))
            break

        elif choosing == "5":
            print(address_book.delete_record(name))
            break

        elif choosing == "6":
            break
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")

@input_error
def add_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
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
            value = input(f"Write birthday for '{name.title()}' >>> ")
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
                if not search_entry.tag:
                    print(add_tag_func([name, value]))
                    break
                else:
                    value = value.split(' ')
                    search_entry.change_tag(value)
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
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")

    print(f"\nDo you wanna add something else to the '{name.title()}' ? (•¿•)")
    print("1 : Yes")
    print("2 : No")
    while True:    
        
        choosing_2 = input("\nChoose № >>> ")
        
        if not choosing_2:
            break
        
        elif choosing_2 == "1":
            add_main_atributes(name, search_entry)
            break
        
        elif choosing_2 == "2":
            break

        else:
            print(f"\nWhat is it '{choosing_2}' ??? (o_O)?")

@input_error
def change_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        print('')
        
        if not choosing:
            break
        
        elif choosing == "1":
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
        
        elif choosing == "2":
            value = input(f"Write new birthday for '{name.title()}' >>> ")
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
        
        elif choosing == "3":
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

        elif choosing == "4":
            value = input(f"Write one #tag or #tags (separatet by ' ') for '{name.title()}' >>> ")
            print('')
            if value:
                if not search_entry.tag:
                    print(add_tag_func([name, value]))
                    break
                else:
                    value = value.split(' ')
                    search_entry.change_tag(value)
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
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")
    
    print(f"\nDo you wanna change something else to the '{name.title()}' ? (•¿•)")
    print("1 : Yes")
    print("2 : No")
    while True:    
        
        choosing_2 = input("\nChoose № >>> ")
        
        if not choosing_2:
            break
        
        elif choosing_2 == "1":
            change_main_atributes(name, search_entry)
            break
        
        elif choosing_2 == "2":
            break

        else:
            print(f"\nWhat is it '{choosing_2}' ??? (o_O)?")

@input_error
def del_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
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
            print(f"\nDo you want to remove one or ALL! tags from the '{name.title()}' ? (•¿•)")
            print("1 : Remove only one tag ")
            print("2 : !!! Delete all tags !!! ")
            print("3 : I changed my mind, I don't want to delete anything")
            while True:     
                choosing_t = input("\nChoose № >>> ")
                print('') 
                if not choosing_t:
                    break  
                elif choosing_t == "1":
                    search_entry.del_tag()
                    break           
                elif choosing_t == "2":
                    print(search_entry.delete_tags())
                    break
                elif choosing_t == "3":
                    break
                else:
                    print(f"\nWhat is it '{choosing_t}' ??? (o_O)?")
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
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")
    
    print(f"\nDo you want to delete something else in '{name.title()}' ? (•¿•)")
    print("1 : Yes")
    print("2 : No")
    while True:    
        
        choosing_3 = input("\nChoose № >>> ")
        
        if not choosing_3:
            break
        
        elif choosing_3 == "1":
            del_main_atributes(name, search_entry)
            break
        
        elif choosing_3 == "2":
            break

        else:
            print(f"\nWhat is it '{choosing_3}' ??? (o_O)?")

# address_book.load_address_book()
# try:
#     boris()
# finally:
#     address_book.save_address_book()

def blue_color(colorless_string): 
    painted_string = "\033[1m\033[34m{}\033[0m".format(colorless_string)
    return painted_string

    





