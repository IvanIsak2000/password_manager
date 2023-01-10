import time
import os
from pathlib import Path
import json
print("ПРОГРАММА МЕНЕДЖЕР ПАРОЛЕЙ!")
a = int(input("Включить программу? Да(1)/Нет(2) "))


def e():
    z = input("Нажмите любую клавишу для выхода...")
    exit()


def clea():
    time.sleep(2)
    os.system("cls||clear")


if a == 1:
    print("Программа запущена!!!")
    clea()
else:
    e()


move = ""
while move != "-":

    move = input(
        "Добавить сайт и пароль:(1)/Удалить пароль у сайта:(2)/Посмотреть(3):/Выключить программу:(-) ")
    if move == "1":  # add data
        site = input("Введите название сайта: ")
        pasw = input("Введите пароль: ")
        file = Path('data.json')
        data = json.loads(file.read_text(encoding='utf-8'))
        print(f"Сайт с именем {site} и паролем {pasw}")
        answer = int(input("Продолжить? (1/2)"))
        if answer == 1:
            data['data'].append({site: pasw})
            file.write_text(json.dumps(data), encoding='utf-8')
            print("ДАННЫЕ ДОБАВЛЕННЫ!")
            clea()

        else:
            print("ДОБАВЛЕНИЕ ОТМЕНЕНО!")

    if move == "2":  # delete data
        site = str(
            input("Введите название сайта, данные от которого надо удалить: \n"))
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        minimal = 0

        for txt in data['data']:
            try:
                if txt[site]:
                    data["data"].pop(minimal)
                    print("ДАННЫЕ УДАЛЕНЫ!")
                    clea()
            except BaseException:
                print(f"САЙТА  {site} НЕ СУЩЕСТВУЕТ!")
        minimal = minimal + 1

        with open('data.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

    if move == "3":  # VIEW DATA
        file = Path('data.json')
        data = json.loads(file.read_text(encoding='utf-8'))

        for dic in data["data"]:
            if dic == " ":
                print("ДАННЫЕ НЕ ЗАПОЛНЕНЫ!")
            else:
                print(dic)

    if move == "-":
        e()
