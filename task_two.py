#task2
"""авдання 2
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

Вимоги до завдання:
Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

Рекомендації для виконання:
Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.

Критерії оцінювання:
Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)


Очікуваний результат:
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]"""
#path = "cats.txt"


import re

def get_cats_info(path):


    
    with open(path) as fl:

        #обробка випадку, коли файл відсутній
        if not fl:
            print("File not found".upper())
            return
        
        else:
    
            indiv_cat_list = []

            for cat_line in fl:
                cat_line = cat_line.strip()
                if not cat_line:
                    continue


                cat_dict = {}
                data = cat_line.split(",")
               
                id, name, age = data
                
                 #component validation: name should be a string, age should be a number, id should be string and no special characters

                if not re.match(r'^[a-zA-Z0-9]+$', id):
                    print(f"Invalid id: {id}. Id should contain only letters and numbers.")
                    continue

                if not re.match(r'^[a-zA-Z]+$', name):
                    print(f"Invalid name: {name}. Name should contain only letters.")
                    continue
                if not age.isdigit() or int(age) < 0 or int(age) > 30:
                    print(f"Invalid age: {age}. Age should be a number between 0 and 30.")
                    continue


                
                cat_dict["id"] = id
                cat_dict["name"] = name 
                cat_dict["age"] = age
                

               



                indiv_cat_list.append(cat_dict)
            
            print("\nCats info successfully retrieved\n")
            print(indiv_cat_list)
            
        
if __name__ == "__main__":
    path = "cats.txt"
    get_cats_info(path)