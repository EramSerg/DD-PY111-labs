"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self.queue_ = []  # инициализировать список
        #self.start_queue = self.queue_[0]
        #self.end_queue = self.queue_[-1]

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.queue_.append(elem)  # реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self.queue_:     # реализовать метод dequeue
            raise IndexError('Очередь пуста!')

        return self.queue_.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):  # реализовать метод peek
            raise TypeError('Индекс должен быть целым числом!')

        if ind > (len(self.queue_) - 1):
            raise IndexError('Индекс элемента вне диапазона очереди!')

        return self.queue_[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        self.queue_.clear()  # реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self.queue_)     # реализовать метод __len__


if __name__ == '__main__':
    MyQueue = Queue()
    MyQueue.enqueue('p')
    MyQueue.enqueue('y')
    MyQueue.enqueue('t')
    MyQueue.enqueue('h')
    MyQueue.enqueue('o')
    MyQueue.enqueue('n')
    print(MyQueue.__len__())
    print(MyQueue.queue_)
    print(MyQueue.peek(1))
    print(MyQueue.peek(4))
    MyQueue.dequeue()
    print(MyQueue.__len__())
    print(MyQueue.queue_)
    MyQueue.dequeue()
    print(MyQueue.__len__())
    print(MyQueue.queue_)