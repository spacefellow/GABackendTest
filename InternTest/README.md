### Задачи для стажера в Гринатом
#### Какие шаги следует предпринять, если бы пользователь сказал, что API возвращает ему ошибку 500?
[Ответ](https://github.com/spacefellow/InternGATest/blob/master/task1.md)
#### Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить? Исправь ошибку и перепиши код ниже с использованием типизации.
```
def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()
```
[Ответ](https://github.com/spacefellow/InternGATest/blob/master/task2.py)
#### Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы выше.
[Ответ](https://github.com/spacefellow/InternGATest/blob/master/task3.py)

#### Напиши функцию на Python, которая возвращает текущий публичный IP-адрес компьютера (например, с использованием сервиса ifconfig.me).
[Ответ](https://github.com/spacefellow/InternGATest/blob/master/task4.py)
#### Напиши функцию на Python, выполняющую сравнение версий по условиям ниже.
```
- Return -1 if version A is older than version B
- Return 0 if versions A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.
```
[Ответ](https://github.com/spacefellow/InternGATest/blob/master/task5.py)
