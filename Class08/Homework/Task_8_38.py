from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")

def input_firstname(): 
    first = input("Введите имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# last name 
def input_lastname(): 
    last = input("Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname

def Add_a_record():
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input("Введите номер телефона: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + "]\n") 
    myfile = open(file_base, "a") 
    myfile.write(contactDetails) 
    print("Следующие контактные данные:\n " + contactDetails + "\nhas been stored successfully!")

def searchcontact(): 
    searchname = input("Введите имя для поиска контактной записи: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(file_base, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print("Ваша необходимая контактная информация: ", end = " ") 
            print(line) 
            found = True 
            break 
    if found == False: 
        print("Искомый контакт недоступен в телефонной книге", searchname)

def change_phone_number():
    contact_list = read_records()
    number_to_change = searchcontact(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_base, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact():
    contact_list = read_records()
    number_to_change = searchcontact(contact_list)
    contact_list.remove(number_to_change)
    with open(file_base, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
 
path_to_db = 'db.txt'
def export_txt():
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open('Export_contact.txt', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                    data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    
def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                Add_a_record()
            case "3":
                searchcontact()
            case "4":
                change_phone_number()
            case "5":
                delete_contact
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()