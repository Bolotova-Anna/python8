def show (file, a):
    with open(file, 'r', encoding='utf-8') as an:
     if a == 1:
         print(an.read())
def add (file, a,):
    with open(file, 'a', encoding='utf-8') as an:
        if a==2:
            name = input("введите имя: ")
            fam = input("введите фамилию: ")
            surname = input("введите отчество: ")
            phon = (input("введите телефон: "))
            an.write(name+','+fam+','+surname+','+phon)
def find (file,a):
    with open(file, 'r', encoding='utf-8') as an:
        if a == 3:
            array =[]
            for line in file:
                b = an.readline().upper().strip()
                array.append(b)
            name = input("введите имя для поиска записи: ").upper()
            for j in array:
                if name in j:
                    print(j)
def delete (file,a):
    with open(file, 'r', encoding='utf-8') as an:
        if a == 4:
            array =[]
            for line in file:
                b = an.readline().upper().strip()
                array.append(b)
            print(array)
            name = input("напишите имя контакта, который хотите удалить: ").upper()
            i =0
            for k in array:
                if name in k:
                    array.pop(i)  
                i+=1 
            print(array) 
            str_array = '\n'.join(array)
            print(str_array)
    with open(file, 'w', encoding='utf-8') as an:
        an.write(str_array)
def change (file,a):
    with open(file, 'r', encoding='utf-8') as an:
        if a == 5:
            array = []
            for line in file:
                 b = an.readline().upper().strip()
                 array.append(b)
            print(array)
            num =int(input("введите 1 если хотите поменять имя, введите 2 если хотите поменять фамилию, введите 3 если хотите поменять отчество, введите 4 если хотите поменять номер: "))
            d = input('введите старые данные, которые хотите поменять: ')
            oro = input("введите новые данные: ")
            for k in array:
                for n in k:
                    if num ==1 and d == n:
                        n = oro  
                    elif num ==2 and d == n:
                        n = oro
                    elif num ==3 and d == n:
                        n = oro
                    elif num ==4 and d == n:
                        n = oro
            print(array)
            str_array = '\n'.join(array)
            print(str_array)
    with open(file, 'w', encoding='utf-8') as an:
        an.write(str_array)
a = int(input("введите 1 если хотите вывести все данные, введите 2 если хотите добавить человека в справочник,введите 3 если хотите найти информацию из справочника по имени, введите 4 если хотите удалить какой-то контакт:, введите 5 если хотите внести измнения в список контактов "))
work_file = 'справочник.txt'
show(work_file, a)
add(work_file,a)
find(work_file, a)
delete(work_file, a)
change(work_file, a)