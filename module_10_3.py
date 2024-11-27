import time
import threading
from random import randint


class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            randomvalue = randint(50, 500)
            self.balance += randomvalue
            print(f'Пополнение: {randomvalue}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            randomvalue = randint(50, 500)
            print(f'Запрос на {randomvalue}.')
            if randomvalue <= self.balance:
                self.balance -= randomvalue
                print(f'Снятие: {randomvalue}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
