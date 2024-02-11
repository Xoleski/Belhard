# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

def sort_list(list1: list):
    return list(filter(lambda x: isinstance(x, str), list1))


ls1 = ["ghf", 7, {4, "dfkj"}, "", None, False, 9, "world", ]
print(sort_list(ls1))

