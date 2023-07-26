from typing import Callable


def create_handlers(callback: Callable[[int], None]) -> list:
    """
    Функция создает список анонимных функций с аргументом callback.
    """
    handlers = []
    for step in  range(5):
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers: list) -> None:
    """
    Функция вызывает объекты(функции) из handlers.
    """
    for handler in handlers:
        handler()
