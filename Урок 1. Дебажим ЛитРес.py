from books_sdk import get_book_by_id, get_author

print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)))

# Гипотеза 1: Неправильные скобки
# Способ проверки: методом клика пройтись по какой скобке
# Установленный факт: Все скобки на месте
# Вывод: Проблема не в этом...

# Гипотеза 2: Ошибка во вложенной функции
# Способ проверки: Запустить вложенную функцию отдельно от внешней
# Код для проверки: print(get_author(get_book_by_id(1, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
#                   print(get_author(get_book_by_id()))
#                   print(get_author())
#
# Установленный факт: Каждая из функций имеет нужные аргументы
# Вывод: Проблема не в этом...

# Гипотеза 3: Проблема в типе данных, '1' должно быть числом
# Способ проверки: Создать переменную с типом данных int
# Код для проверки: а = 1
#                   print(get_author(get_book_by_id(а, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: Тип данных в данном случе не играет роли
# Вывод: Проблема не в этом...

# Гипотеза 4: Книги с номером 1 не существует
# Способ проверки: Подставить другой номер книги
# Код для проверки: print(get_author(get_book_by_id(34, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
#                   print(get_author(get_book_by_id(52, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
#                   print(get_author(get_book_by_id(48, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
#                   print(get_author(get_book_by_id(18, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: Номер книги в данном случает не играет роли
# Вывод: Проблема не в этом...

# Гипотеза 5: Не правильный порядок аргументов
# Способ проверки: Поменять аргументы функции сетами
# Код для проверки: print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)))
# Установленный факт: Неправильный порядок аргументов в функции и был причиной ошибки
# Вывод: Проблема решена!
