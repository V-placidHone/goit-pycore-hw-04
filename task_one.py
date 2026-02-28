#task1
"""Завдання 1
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
Наприклад:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

Вимоги до завдання:
Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

Рекомендації для виконання:
Використовуйте менеджер контексту with для читання файлів.
Пам'ятайте про встановлення кодування при відкриті файлів
Для розділення даних у кожному рядку можна застосувати метод split(',').
Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.

Критерії оцінювання:
Функція повинна точно обчислювати загальну та середню суми.
Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

Очікуваний результат:
Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000"""

import re


 
def total_salary(path):
    total = 0
    count_employes = 0

    #need to parse the file and get every salary + average
    with open(path) as fl_name:
        #обробка випадку, коли файл відсутній
        if not fl_name:
            print("File not found".upper())
            return
        
        else:
            salary_employes = []
            #iterate through the file and get every line, split it by comma and get the salary, add it to total and count the number of employees
            for ln in fl_name:

                ln = ln.strip()
                if not ln:
                    continue
                count_employes +=1
                
                employee_data = ln.strip().split(",") 
                if len(employee_data) != 2:
                    print(f"There is incorrect data in the file, please check the file and try again. Line: {ln}")
                    return



                #adding fields validation: Name -> only letters and spaces, Salary -> exist + only numbers
                # Validate name
                if not re.fullmatch(r"[a-zA-Z\s]+", employee_data[0].strip()):
                    print(f"Invalid employee name. Line: {ln}")
                    return

                # Validate salary
                if not re.fullmatch(r"\d+", employee_data[1].strip()):
                    print(f"Invalid salary. Line: {ln}")
                    return



                empl = ln.split(",")
                salary_employes.append(empl[1])
                
                
                
        
        total = sum(int(salary) for salary in salary_employes)
        average = total / count_employes if count_employes > 0 else 0
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {int(average)}") 
    


if __name__ == "__main__":
    path = "salary_file.txt"
    total_salary(path)