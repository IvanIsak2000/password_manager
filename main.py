print("Программа для сохранения паролей!")

import json
from pathlib import Path

move = ""
while move !="-":
    
    move = input("Добавить сайт и пароль:(1)/Удалить пароль у сайта:(2)/Изменить пароль у сайте:(3)/Посмотреть(4): ")
    if move == "1":#add data
        site = input("Введите название сайта: ")
        pasw = input("Введите пароль: ")
        file = Path('data.json')
        data = json.loads(file.read_text(encoding='utf-8'))
        data['data'].append({site:pasw})
        file.write_text(json.dumps(data), encoding='utf-8')
        print("ДАННЫЕ ДОБАВЛЕННЫ!")



    if move == "2":#delete data NO WORK


            
        site = input("Введите название сайта, данные от которого надо удалить: ")
        import json

        with open ("data.json","r") as file:
            f = json.load(file)
        f = f["data"]
        print(f)
        for(name) in f:
            if str(name) ==site:
                print("Сайт существует!")
        
        
        
    if move == "3":#NO WORK
        data = {}
        site = input("Введите сайт,у которого хотите изменить пароль: ")
        pasw = input("Введите новый пароль: ")
        file = Path('data.json')
        data = json.loads(file.read_text(encoding='utf-8'))
        data['data'].append({site:pasw})
        file.write_text(json.dumps(data), encoding='utf-8')


    if move =="4":#VIEW DATA
        file = Path('data.json')
        data = json.loads(file.read_text(encoding='utf-8'))
        for dic in data["data"]:
            print(dic)
