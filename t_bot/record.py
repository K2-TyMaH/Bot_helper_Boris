from fields_for_record import Name, Birthday, Phone, Email, Note, Tag
from datetime import datetime
from copy import copy


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.emails = []
        self.tag = None
        self.note = None
        self.notes =[]


    def add_phone(self, phone) -> str:
        '''Додає телефону до списку телефонів контакту.'''
        added_phone = Phone(phone)
        self.phones.append(added_phone)
        return f'The phone < {added_phone.value} > was added to the < {self.name.value.title()} >.'

    def change_phone(self, new_phone) -> str:
        '''Міняє існуючий телефон контакту.'''
        
        if self.phones:
            new_phone = Phone(new_phone)
            phones = [phone.value for phone in self.phones]
            showing = dict(enumerate(phones, 1))
            while True:
                try:
                    print(f"What phone you want to change? {showing}")
                    choosing = input("Choose № of this phone (skip it if you don't want)>>> ")
                    if not choosing:
                        return f"You didn't change any phone of < {self.name.value.title()} >"
                    choosing = int(choosing)
                    if choosing > 0:
                        self.phones[choosing-1] = new_phone
                        return f"Phone < {showing[choosing]} > of < {self.name.value.title()} > changed to the < {new_phone.value} >"
                    else:
                        raise KeyError
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Phones list of < {self.name.value.title()} > is empty")

   
    def delete_phone(self) -> str:
        '''Видаляє існуючий телефон.'''
        
        if self.phones:
            phones = [phone.value for phone in self.phones]
            showing = dict(enumerate(phones, 1))
            while True:
                try:
                    print(f"What phone you want to remove? {showing}")
                    choosing = input("Choose № of this phone (skip it if you don't want)>>> ")
                    if not choosing:
                        return f"You didn't remove any phone of < {self.name.value.title()} >"
                    choosing = int(choosing)
                    if choosing > 0:
                        self.phones.pop(choosing-1)
                        return f"Phone < {showing[choosing]} > of < {self.name.value.title()} > removed"
                    else:
                        raise KeyError
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Phones list of < {self.name.value.title()} > is empty")

    def add_mail(self, mail) -> str:
        '''Додає мейл до контакту.'''
        added_email = Email(mail)
        self.emails.append(added_email)
        return f'The email < {added_email.value} > was added to the < {self.name.value.title()} >.'

    def change_mail(self, new_mail) -> str:
        '''Міняє існуючий мейл.'''
        if self.emails:
            new_mail = Email(new_mail)
            emails = [email.value for email in self.emails]
            showing = dict(enumerate(emails, 1))
            while True:
                try:
                    print(f"What email you want to change? {showing}")
                    choosing = input("Choose № of this email (skip it if you don't want)>>> ")
                    if not choosing:
                        return f"You didn't change any email of < {self.name.value.title()} >"
                    choosing = int(choosing)
                    if choosing > 0:
                        self.emails[choosing-1] = new_mail
                        return f"Email < {showing[choosing]} > of < {self.name.value.title()} > changed to the < {new_mail.value} >"
                    else:
                        raise KeyError
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Emails list of < {self.name.value.title()} > is empty")

    def delete_mail(self) -> str:
        '''Видаляє існуючий мейл.'''
        if self.emails:
            emails = [email.value for email in self.emails]
            showing = dict(enumerate(emails, 1))
            while True:
                try:
                    print(f"What email you want to remove? {showing}")
                    choosing = input("Choose № of this email (skip it if you don't want)>>> ")
                    if not choosing:
                        return f"You didn't remove any email of < {self.name.value.title()} >"
                    choosing = int(choosing)
                    if choosing > 0:
                        self.emails.pop(choosing-1)
                        return f"Email < {showing[choosing]} > of < {self.name.value.title()} > removed."
                    else:
                        raise KeyError
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Emails list of < {self.name.value.title()} > is empty")

    def add_note(self, list_note) -> str:
        '''Додає нотатку. Один раз'''
        if not self.note:
            note = ""
            for item in list_note:
                note += f"{item} "
            self.note = Note(note)
        else:
            return f'Note is existed. Cannot be added'

        return f"The note < {note[:-1]} > was added to the contact < {self.name.value.title()} >."

    def change_note(self, list_new_note) -> str:
        '''Міняє нотатку.'''
        new_note = ""
        for item in list_new_note:
            new_note += f"{item} "
        old_note = self.note.value
        note = old_note + new_note   
        self.note = Note(note)

        return f"The note < {new_note[:-1]} > was added to the contact < {self.name.value.title()} >."

    def delete_note(self) -> str:
        '''Видаляє нотатку.'''
        deleted_note = self.note.value
        self.note = None
        return f'The note < {deleted_note} > of contact < {self.name.value} > was deleted.'

    def add_tag(self, list_tag) -> str:
        '''Створює теги. Один Раз при виклику та кожного разу післі Delete tags '''
        if not list_tag:
            return f'Tag is not input, please type again'
        elif not self.tag:
            tag_list2 = []
            for tag in list_tag:
                tag_list2.append(tag)
            #tags_list = tag[0].split(',') # [#one,#two]
            self.tag = Tag(tag_list2)
            return f"The tag < {tag_list2} > was added to the contact < {self.name.value} >."
        else:
            return f'Tag is existed. Cannot be added'

    def change_tag(self, new_tag_list):
        '''Додає теги до існуючиго списку тегів.'''
        old_tag = self.tag
        if self.tag:
            self.tag = Tag(old_tag.value + new_tag_list)
            print(f'The new tag {new_tag_list} has been added to old one {old_tag.value}')
        else:
            print(f'The tag has been added yet for this contact. Add first')

    def delete_tags(self) -> str:
        '''Видаляє всі тег.'''
        deleted_tag = self.tag
        self.tag = None
        return f"The tag < {deleted_tag.value} > of contact < {self.name.value} > was deleted"

    def del_tag(self):
        '''Видаляє існуючий тег зі списку.'''
        if self.tag:
            old_tags =copy(self.tag.value)
            tags = [tag for tag in self.tag.value]
            showing = dict(enumerate(tags, 1))
            while True:
                try:
                    print(f"What tag do you want to remove? {showing}")
                    choosing = input("Choose № of this tags (skip it if you  want press enter)>>> ")
                    if not choosing:
                        print( f"You didn't remove any tags of < {self.tag.value} >")
                    choosing = int(choosing)
                    self.tag.value.pop(choosing - 1)
                    print( f"Tag < {showing[choosing]} > from < {old_tags} > was removed")
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")
        else:
            return f' Tag {self.tag} is empty '


    def add_birthday(self, birthday) -> str:
        '''Додає день народження.'''
        self.birthday = Birthday(birthday)
        return f'Birthday was successfully added'

    def change_birthday(self, new_birthday) -> str:
        '''Міняє день народження.'''
        if self.birthday:
            self.birthday = Birthday(new_birthday)
            return f'Birthday has been successfully changed'
        else:
            return f'The birthday hasn`t been added yet for this contact. Add first'

    def days_to_birthdays(self):
        '''Повертає кількість днів, яка залишилась до ДН конкретної людини.'''
        if self.birthday:
            current_year = datetime.now().year
            current_day = datetime.now()
            this_year_birthday = datetime(year=current_year, month=self.birthday.value.month, day=self.birthday.value.day)
            if (this_year_birthday - current_day).days >= 0:
                next_birth = this_year_birthday - current_day
                return next_birth.days
            else:
                next_birth = datetime(year=current_year + 1, month=self.birthday.value.month, day=self.birthday.value.day)
                return (next_birth - current_day).days
        else:
            return f'The birthday hasn`t been added yet for this contact'
    
    def delete_birthday(self):
        self.birthday = None
        return f"The birhdays was deleted successfully."

