import os
# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telegram
import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Подключаем модуль для SQLite
import sqlite3
# Подключаем модуль для работы с датой/веременем
from datetime import datetime

# Указываем токен
API_TOKEN = '5619714418:AAFnmD40Ejmonq3v9FCZi7mU_TV1qr6RyoM'
bot = telebot.TeleBot(API_TOKEN)
# Текст приглашения
welcome_message = "Тестовая версия\nДобро пожаловать!\nБот предназначен для поиска вакансий на рынке труда"
# Справочная информация
#help_message = "Помощь"

# Создание базы данных, заполнение ее данными 
def init_db():
    try:
        # Подключение к SQLite 
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                             
        conn = sqlite3.connect('genealogy.db')
        print("База данных SQLite подключена")
        # Объект cursor, позволяет взаимодействовать с базой данных             
        cursor = conn.cursor()

        # Проверка наличия таблицы 
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='juz'")
        result = cursor.fetchall()
        if len(result) > 0:
            print("Таблица juz уже существует")        
        else:
            print("Создается таблица juz")  
            create_table_query = '''CREATE TABLE juz (
                                id INTEGER PRIMARY KEY,                                
                                title TEXT NOT NULL UNIQUE);'''
            # Выполнение команды: это создает новую таблицу
            cursor.execute(create_table_query)
            conn.commit()
            print("Таблица juz создана")        
        # Заполнение таблицы (один раз)
        sql = "SELECT id FROM juz"
        # С помощью метода execute объекта cursor можно выполнить запрос в базу данных из Python.
        # Он принимает SQL-запрос в качестве параметра и возвращает resultSet (строки базы данных):
        cursor.execute(sql)
        # Получить результат запроса из resultSet можно с помощью методов, например, fetchAll()
        row = cursor.fetchone()
        # Если таблица пустая - заполнить ее
        if row is None:
            cursor.execute("INSERT INTO juz (id, title) VALUES (Null, 'Ұлы жүз')")
            cursor.execute("INSERT INTO juz (id, title) VALUES (Null, 'Орта жүз')")
            cursor.execute("INSERT INTO juz (id, title) VALUES (Null, 'Кіші жүз')")
            conn.commit()
            print("Таблицы juz заполнена")

        # Проверка наличия таблицы 
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tribe'")
        result = cursor.fetchall()
        if len(result) > 0:
            print("Таблица tribe уже существует")        
        else:
            print("Создается таблица tribe")  
            create_table_query = '''CREATE TABLE tribe (
                                id INTEGER PRIMARY KEY,                                
                                juz_id INTEGER NOT NULL,                                
                                title TEXT NOT NULL UNIQUE);'''
            # Выполнение команды: это создает новую таблицу
            cursor.execute(create_table_query)
            conn.commit()
            print("Таблица tribe создана")        
        # Заполнение таблицы (один раз)
        sql = "SELECT id FROM tribe"
        # С помощью метода execute объекта cursor можно выполнить запрос в базу данных из Python.
        # Он принимает SQL-запрос в качестве параметра и возвращает resultSet (строки базы данных):
        cursor.execute(sql)
        # Получить результат запроса из resultSet можно с помощью методов, например, fetchAll()
        row = cursor.fetchone()
        # Если таблица пустая - заполнить ее
        if row is None:
            # Ұлы жүз
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Канглы')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Жалайыры')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Шанышкылы')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Сары Уйсун')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Шапрашты')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Ысты')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Ошакты')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Албаны')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Суаны')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Дулаты')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 1, 'Сиргели')")
            # Орта жүз
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 2, 'Аргыны')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 2, 'Кыпшак')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 2, 'Найманы')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 2, 'Коныраты')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 2, 'Кереи')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 2, 'Уаки')")
            # Кіші жүз
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 3, 'Байулы')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 3, 'Алимулы')")
            cursor.execute("INSERT INTO tribe (id, juz_id, title) VALUES (Null, 3, 'Жетыру')")
            conn.commit()
            print("Таблицы tribe заполнена")

         # Проверка наличия таблицы 
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clan'")
        result = cursor.fetchall()
        if len(result) > 0:
            print("Таблица clan уже существует")        
        else:
            print("Создается таблица clan")  
            create_table_query = '''CREATE TABLE clan (
                                id INTEGER PRIMARY KEY,                                
                                tribe_id INTEGER NOT NULL,                                
                                title TEXT NOT NULL);'''
            # Выполнение команды: это создает новую таблицу
            cursor.execute(create_table_query)
            conn.commit()
            print("Таблица clan создана")        
        # Заполнение таблицы (один раз)
        sql = "SELECT id FROM clan"
        # С помощью метода execute объекта cursor можно выполнить запрос в базу данных из Python.
        # Он принимает SQL-запрос в качестве параметра и возвращает resultSet (строки базы данных):
        cursor.execute(sql)
        # Получить результат запроса из resultSet можно с помощью методов, например, fetchAll()
        row = cursor.fetchone()
        # Если таблица пустая - заполнить ее
        if row is None:
            # Ұлы жүз
            # Канглы            
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 1, 'Кара-Канлы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 1, 'Кызыл-Канлы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 1, 'Капсан-Канлы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 1, 'Сары-Канлы')")
            # Жалайыры
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Сырманак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Арыктыным')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Байчигир')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Балгалы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Кайшылы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Кушук')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Шуманак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Кальпе')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Карашапал')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Мырза')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Оракты')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Сыпатай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 2, 'Бирманак')")
            # Шанышкылы
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Курбака')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Дархан')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Кырыксадак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Бектау')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Арапшы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Сырдым')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Жойсын')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 3, 'Багыс')")              
            # Сары Уйсун
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 4, 'Калша')")              
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 4, 'Джакып')")               
            # Шапрашты
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 5, 'Айкым')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 5, 'Асыл')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 5, 'Екей')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 5, 'Емил')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 5, 'Кебенек')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 5, 'Шыбыл')")            
            # Ысты
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 6, 'Ойык')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 6, 'Тилик')")
            # Ошакты
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 7, 'Аталык')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 7, 'Байлы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 7, 'Коныр')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 7, 'Тасжурек')")
            # Албаны
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 8, 'Сары')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 8, 'Шыбыл')")
            # Суаны
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 9, 'Байтюгей')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 9, 'Токарстан')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 9, 'Багыс')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 9, 'Сартай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 9, 'Нартай')")
            # Дулаты
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 10, 'Ботпай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 10, 'Жаныс')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 10, 'Сикым')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 10, 'Шымыр')")
            # Сиргели
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 11, 'Байулы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 11, 'Уштанбалы')")
            
            # Орта жүз
            #Аргыны
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Мейрам')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Куандык')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Суйиндык')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Бегендык')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Шегендык')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Каракесек')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Момын')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Атыгай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Басентийин')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Канжыгалы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Карауыл')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Тобыкты')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Джогары-Щекты')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Томенги-Щекты')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Жиен')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 12, 'Таракты')")
            #Кыпшак
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Кыпшак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Кулан Кыпшак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Сары Кыпшак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Кытай Кыпшак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Кара Кыпшак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Карабалык')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Колденен')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Бултын')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Узун')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 13, 'Торы')")
            #Найманы
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Саржомарт')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Бура')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Каратай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Кокджарлы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Толегетай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Матай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Каракерей')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Садыр')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Торгул')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Терстамгалы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Баганалы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 14, 'Балталы')")
            #Коныраты
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Котенши')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Сангыл')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Боджбан')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Джетимдер')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Мангытай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Аманбай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Джаманбай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Коктинулы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Байлар')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Жандар')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Оразкелди')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Карасирак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Токболат')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Кулшыгаш')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 15, 'Алги')")
            #Кереи
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Абак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Джантекей')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Джадик')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Шимойын')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Шубарайгыр')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Меркит')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Шеруши')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Сарбас')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Молкы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Ители')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Каракас (Сыйдалы)')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Консадак')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Джастабан')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Итимген')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Ашамайлы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Балта')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Кошебе')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Тарышы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 16, 'Сыйбан')")
            #Уаки
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Сарман')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Шога')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Байназар')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Еренши')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Бидалы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Барджакы')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Жансары')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 17, 'Шайкоз')")

            # Кіші жүз
            #Байулы
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Шеркеш')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Адай')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Алаша')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Алтын')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Байбакты')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Берш')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Есентемир')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Жаппас')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Кызылкурт')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Маскар')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Таз')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Тана')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 18, 'Ысык')")
            #Алимулы
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 19, 'Шекты')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 19, 'Каракесек')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 19, 'Карасакал')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 19, 'Кете')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 19, 'Торткара')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 19, 'Шомекей')")
            #Жетыру
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 20, 'Тама')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 20, 'Табын')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 20, 'Кердеры')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 20, 'Кереит')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 20, 'Тлеу')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 20, 'Рамадан')")
            cursor.execute("INSERT INTO clan (id, tribe_id, title) VALUES (Null, 20, 'Жагалбайлы')")

            conn.commit()
            print("Таблицы clan заполнена")

        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        print("База данных SQLite отключена")        
    except Exception as error:
        print(error)

# Список жузов
def get_juz(message):
    #print("get_juz")
    if message.text=="На главную":
        send_welcome(message)
    else:
        juz_list = []
        conn = sqlite3.connect('genealogy.db')
        print("База данных SQLite подключена")
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "SELECT title FROM juz"
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            juz_list.append(row[0])        
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        print("База данных SQLite отключена")    
        return juz_list

# Список племен
def get_tribe(message):
    #print("get_tribe")
    if message.text=="На главную":
        send_welcome(message)
    else:
        tribe_list = []
        conn = sqlite3.connect('genealogy.db')
        print("База данных SQLite подключена")
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "SELECT juz.title AS jus, tribe.title AS tribe FROM tribe INNER JOIN juz ON tribe.juz_id = juz.id WHERE juz.title = '" + message.text + "'"
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            tribe_list.append(row[1])        
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        print("База данных SQLite отключена")   
        return tribe_list

# Список родов
def get_clan(message):
    #print("get_clan")
    if message.text=="На главную":
        send_welcome(message)
    else:
        clan_list = []
        conn = sqlite3.connect('genealogy.db')
        print("База данных SQLite подключена")
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "SELECT juz.title AS jus, tribe.title AS tribe, clan.title AS clan FROM tribe INNER JOIN juz ON tribe.juz_id = juz.id  INNER JOIN clan ON clan.tribe_id = tribe.id WHERE  tribe.title = '" + message.text + "'"
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            clan_list.append(row[2])        
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        print("База данных SQLite отключена")   
        return clan_list

# Жуз
class Juz:
    def __init__(self, id, title):
        self.id = id
        self.title = title

# Племя
class Tribe:
    def __init__(self, id, juz_id, title):
        self.id = id
        self.juz_id = juz_id
        self.title = title

# Род
class Clan:
    def __init__(self, id, tribe_id, title):
        self.id = id
        self.tribe_id = tribe_id
        self.title = title

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    try:
        # Список жузов
        juz_list = get_juz(message)
        # Подключаем клавиатуру
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        # Указываем название кнопок, добавляем клавиатуру
        for i in range(0, len(juz_list)):
            markup.add(juz_list[i])
        # Стартовое сообщение
        msg = bot.reply_to(message, 'Қош келдіңіз\nтаңдаңыз', reply_markup=markup)
        #Выбор действия 
        bot.register_next_step_handler(msg, process_menu1)
    except Exception as e:
        print(str(e))
        bot.reply_to(message, 'упс')

def process_menu1(message):
    try:
        #print(message.text)
        if message.text=="Басына":
            send_welcome(message)
        else:    
            # Список племен для данного Жуза
            tribe_list = get_tribe(message)
            # Подключаем клавиатуру
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            # Указываем название кнопок, добавляем клавиатуру
            for i in range(0, len(tribe_list)):
                markup.add(tribe_list[i])
            # Кнопка в начало (На главную)
            markup.add("Басына")            
            # Сообщение
            msg = bot.reply_to(message, """Таңдаңыз""", reply_markup=markup)
            bot.register_next_step_handler(msg, process_menu2)
    except Exception as e:
        print(str(e))
        bot.reply_to(message, 'упс')

def process_menu2(message):
    try:
        #print(message.text)
        # Список племен для данного Жуза
        if message.text=="Басына":
            send_welcome(message)
        else:    
            clan_list = get_clan(message)
            # Подключаем клавиатуру
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            # Указываем название кнопок, добавляем клавиатуру
            for i in range(0, len(clan_list)):
                markup.add(clan_list[i])
            # Кнопка в начало (На главную)
            markup.add("Басына")            
            # Сообщение
            msg = bot.reply_to(message, """Таңдаңыз""", reply_markup=markup)
            bot.register_next_step_handler(msg, process_menu3)
    except Exception as e:
        print(str(e))
        bot.reply_to(message, 'упс')

def process_menu3(message):
    try:
        print(message.text)
        # Список племен для данного Жуза
        if (message.text=="Мейрам"):
            # Орта жүз, Арғын, Мейрам, Қуандық, Қарпық , Тінәлі, Үсейін, Құттыбай, Тілеумет, Құрмантай, Мәмбетей, Құлжан, Балықпай, Малтабар, Алдонғор, Өміртай, Ғабдулманап(Мантай), Әсет, Ескендір
            bot.send_message(message.chat.id,  "<b>Орта жүз</b> " +
                             "\n<b>Арғын</b> " + 
                             "\n<b>Мейрам</b> " + 
                             "\n<b>Қуандық</b> " + 
                             "\n<b>Қарпық</b> " + 
                             "\n<b>Тінәлі</b> " + 
                             "\n<b>Үсейін</b> " + 
                             "\n<b>Құттыбай</b> " + 
                             "\n<b>Тілеумет</b> " + 
                             "\n<b>Құрмантай</b> " + 
                             "\n<b>Мәмбетей</b> " + 
                             "\n<b>Құлжан</b> " + 
                             "\n<b>Балықпай</b> " + 
                             "\n<b>Малтабар</b> " + 
                             "\n<b>Алдонғор</b> " + 
                             "\n<b>Өміртай</b> " + 
                             "\n<b>Ғабдулманап(Мантай)</b> " + 
                             "\n<b>Әсет</b> " + 
                             "\n<b>Ескендір</b> ", parse_mode=telegram.ParseMode.HTML )                
            send_welcome(message)
        else:
            #msg = bot.reply_to(message, """Таңдаңыз""")
            #bot.register_next_step_handler(msg, send_welcome)
            send_welcome(message)
    except Exception as e:
        print('process_menu3', str(e))
        bot.reply_to(message, 'упс')

# Создание базы данных, заполнение ее данными 
init_db()
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)
# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
# Запускаем постоянный опрос бота в Телеграме 
bot.polling(none_stop=True, interval=0)
