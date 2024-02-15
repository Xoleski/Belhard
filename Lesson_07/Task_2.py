# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError


class Category:
    categories = []

    @classmethod
    def add(cls, name: str):
        try:
            if name in cls.categories:
                raise ValueError("ValueError")
            else:
                cls.categories.append(name)
                return print(cls.categories.index(name))
        except ValueError as exp:
            print(exp, "Уже есть такая категория")

    @classmethod
    def get(cls, index: int):
        if index < len(cls.categories):
            return cls.categories[index]
        else:
            return "Нет такого индекса в списке"

    @classmethod
    def delete(cls, index: int):
        try:
            del (cls.categories[index])
        except IndexError:
            print("IndexError", "Нет такого индекса")

    @classmethod
    def update(cls, index: int, new_name: str):
        try:
            if new_name not in cls.categories:
                if index >= len(cls.categories):
                    cls.categories.append(new_name)
                else:
                    cls.categories[index] = new_name
            else:
                raise ValueError("ValueError")
        except ValueError as exp:
            print(exp, "Уже есть такая категория")


Category().add("low")

Category().add("high")

# Category().delete(2)

Category().update(2, "medium")

Category().get(2)
Category().update(2, "medium")
# Category().update(3, "medium")

Category().add('high')

Category().get(3)
Category().delete(6)





# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError


class CategoryList:
    categories = []
    name_c = ""
    is_published = bool

    @classmethod
    def add(cls, name: dict[name_c: str, is_published: bool]):
        try:
            if name in cls.categories:
                raise ValueError("ValueError")
            else:
                cls.categories.append(name)
                return print(cls.categories.index(name))
        except ValueError as exp:
            print(exp, "Уже есть такая категория")

    @classmethod
    def get(cls, index: int):
        if index < len(cls.categories):
            return cls.categories[index]
        else:
            return "Нет такого индекса в списке"

    @classmethod
    def delete(cls, index: int):
        try:
            del (cls.categories[index])
        except IndexError:
            print("IndexError", "Нет такого индекса")

    @classmethod
    def update(cls, index: int, new_name: dict[name_c: str, is_published: bool]):
        try:
            if new_name.keys() not in [i.keys() for i in cls.categories]:
                if index >= len(cls.categories):
                    cls.categories.append(new_name)
                    return print(cls.categories.index(new_name))
                else:
                    cls.categories[index] = new_name
                    return print(cls.categories.index(new_name))
            else:
                raise ValueError("ValueError")
        except ValueError as exp:
            print(exp, "Уже есть такая категория")

    @classmethod
    def make_published(cls, index: int):
        try:
            k = cls.categories[index]
            itm = [i for i in k][0]
            k.update({itm: True})
            return k
        except IndexError:
            print("IndexError", "Нет такого индекса")

    @classmethod
    def make_unpublished(cls, index: int):
        try:
            k = cls.categories[index]
            itm = [i for i in k][0]
            k.update({itm: False})
            return k
        except IndexError:
            print("IndexError", "Нет такого индекса")


CategoryList().add({"low": False})

print(CategoryList().get(0))
CategoryList().add({"medium": False})

print(CategoryList().get(1))
CategoryList().add({"high": False})

print(CategoryList().get(2))
CategoryList().delete(1)
print(CategoryList().get(1))
CategoryList().update(1, {"mix": False})
print(CategoryList().get(1))
CategoryList().update(4, {"max": False})
print(CategoryList().get(2))
# CategoryList().update(2, {"max": False})
# print(CategoryList().get(1))
CategoryList().make_published(3)
print(CategoryList().get(2))
CategoryList().make_unpublished(6)
print(CategoryList().get(2))
CategoryList().update(4, {"max": False})
print(CategoryList().get(6))

CategoryList().add({"nice": False})
print(CategoryList().get(3))
CategoryList().add({"nice": False})
