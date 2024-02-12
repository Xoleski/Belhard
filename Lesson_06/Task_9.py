# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)


def no_data(users: list, key: str):
    users_without_email = []
    for item in users.keys():
        if not key in users[item]:
            users_without_email.append(item)
        elif not users[item][key]:
            users_without_email.append(item)
    return users_without_email


users = {
    "id_01": {
        "name": "name_01",
        "last_name": "last_name_01",
        "phone_number": "phone_number_01",
        "email": "email_01"
    },
    "id_02": {
        "name": "name_02",
        "last_name": "last_name_02",
        "phone_number": "phone_number_02",
        "email": ""
    },
    "id_03": {
        "name": "name_03",
        "last_name": "last_name_03",
        "phone_number": "phone_number_03",
    },
    "id_04": {
        "name": "name_04",
        "phone_number": "phone_number_04",
        "email": "email_04"
    },
    "id_05": {
        "name": "name_05",
        "last_name": "last_name_05",
        "phone_number": "phone_number_05",
        "email": ""
    },
    "id_06": {
        "name": "name_06",
        "last_name": "last_name_06",
        "phone_number": "phone_number_06",
        "email": "email_06"
    },
    "id_07": {
        "name": "name_07",
        "last_name": "",
        "phone_number": "phone_number_07",
    }
}


key = "email"
print(no_data(users, key))
