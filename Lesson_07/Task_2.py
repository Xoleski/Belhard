
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
        if name in cls.categories:
            raise ValueError
        else:
            cls.categories.append(name)
            return cls.categories.index(name)

    @classmethod
    def get(cls, index: int):
        return cls.categories[index]

    @classmethod
    def delete(cls, index: int):
        try:
            del (cls.categories[index])
        except IndexError:
            pass

    @classmethod
    def update(cls, index: int, new_name: str):
        if index >= len(cls.categories):
            cls.categories.append(new_name)
        elif new_name not in cls.categories:
            cls.categories[index] = new_name
        else:
            raise ValueError




    # def __int__(self, categories):
    #     self.cat = categories


mn = ['low', 'high', 'medium']
kitkat = Category().add("low")
print(kitkat)
kitkat = Category().add("high")
print(kitkat)
# Category().delete(2)
# print(i := Category().get(0))
kitkat = Category().update(2, "medium")
print(kitkat)
print(i := Category().get(2))
Category().update(2, "medium")

# Category().add('high')
# print(kitkat)






























# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError




