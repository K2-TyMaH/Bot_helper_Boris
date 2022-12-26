import re
from datetime import datetime
from collections import UserDict


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        fixed_phone = self._sanitize_phone_number(value)
        if len(fixed_phone) < 10 or len(fixed_phone) > 12:
            raise ValueError('Wrong format of phone, must be 10 or 12 numbers')
        if not fixed_phone.isnumeric():
            raise ValueError("Wrong format of phone, must be only numbers")
        self._value = fixed_phone

    def _sanitize_phone_number(self, phone):
        new_phone = (
            phone.strip()
            .replace("+", "")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return new_phone


class Email(Field):

    @Field.value.setter
    def value(self, email: str):

        new_email = re.search(r'[a-zA-Z]+[\w.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', email)

        if not new_email:
            raise ValueError(f"Email '{email}' is not valid.")
        #if len(new_email) > 

        self._value = new_email.group()
        

class Notes(UserDict):
    # [["note1", ["tag1_1", "tag1_2"]], ["note2", ["#tag2_1", "tag2_2"]]]

    def __init__(self):
        self.notes = []   # буде складатися з класів Note

    def add_tags(self, tags):
        self.tags = tags
       
       
class Note(Field):
    pass


class Tag(Field):
    @Field.value.setter
    def value(self, value):
        for tag in value:
            if not isinstance(tag, str):
                raise ValueError(f'The tag shall be string')
            if not tag.startswith('#'):
                raise ValueError(f'The tag must start #')
        # value = " ".join(value)
        self._value = value



class Birthday(Field):
    ''' Класс Birthday створює дату народження.
    Робить перевірку на корректність введених данних
    '''
    @classmethod
    def range_control(cls, variable, left_range, right_range):
        if left_range <= variable <= right_range:
            return variable
        else:
            raise ValueError(f'Your data {variable} shall be in range from {left_range} up to {right_range}')

    @Field.value.setter
    def value(self, birthday_str):
        birth_list = birthday_str.split('.')
        if (len(birth_list) < 3) or (len(birth_list) > 3):
            raise ValueError("Please type birthday in format 'year.month.day'")
        year = [num for num in birth_list if len(num) == 4]
        year_index_in_list = birth_list.index(year[0])
        index_day = [2 if year_index_in_list == 0 else 0]

        year = self.range_control(int(year[0]), 1920, 2022)
        month = self.range_control(int(birth_list[1]), 1, 12)
        day = self.range_control(int((birth_list[index_day[0]])), 1, 31)

        self._value = datetime(year=year, month=month, day=day).date()



