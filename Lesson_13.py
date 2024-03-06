# Конкурентное выполнение кода
# Ассинхронное
# Использование потоков
#     программные потоки
#     каждую функцию в своем потоке
#     паралелльно
#     Жертвуем ресурсами, выигрываем в скорости
# GIL - нельзя два и более потоков не могут обратиться к одному и тому же файлу одновременно

from threading import *
from time import sleep

from queue import Queue, LifoQueue

# логику и интерфейс на два отдельных потока

def ping():
    for _ in range(10):
        print("ping")
        sleep(1)


def pong():
    for _ in range(10):
        print("pong")
        sleep(1)

# ping()
# pong()

treads = [Thread]
Thread().start()
Thread().join()

# Синхронизация потоков

# Замок

l = Lock()


# Деде лок - когда поток заблокировал замок, но до его разблокировки попытался заблокировать его еще раз

rl = RLock()

s = Semaphore(3)

# Похож на кассы в магазине 3 шт
# Не более чем указанное количество потоков
# Ограничение пропускной способности

b = Barrier(3)
# Барьер. Принимает число. Нет контекстного менеджера. Есть Wait()
# Как маршрутка ждет указанное количество пассажиров

# Иногда нужно прокидывать между потоками флаг
# Для этого - ивенты

e = Event() # булевый флаг

l = local() # локальные области видимости



# ПРОЦЕССЫ

from multiprocessing import Process, Lock, RLock, Semaphore

# тоже, только не средс а процесс

#  внутри процессов можно запускать потоки

# кратное потребление ресурсов, но более безопасно чем потоки

# процессы можно запустить только из точки входа bли из функции

if __name__ == "__main__":
    ...

# АСИНХРОННОЕ ПРОГРАММИРОВАНИЕ
# Один процесс - один поток
# на самом деле это конкурентное выполнение
# цикл событий - задача выполнять таски по очереди
# чем то похожее на генераторы
# pip install asyncio - ноо он уже встроен

# корутина = это ассинхр. функция


async def foo():
    print("asy")


# async def bar(): # нужно вызывать корутину так
#     await foo()


# но корутину можно вызвать только из другой корутины
# поэтому первую корутину нужно превратить в задачу
# и поставить ее в цикл событий
# но нужно и бар запучтит  но тоже в задачу

from asyncio import create_task, run, current_task
async def bar():
    f = create_task(foo(test="g"))
    await f

run(bar())

# конкурентность начинает работать только тогда когда корутину превращают в задау
# но не всегда нужна задача, потому что иногда нужно получить результат здесь и сейчас





