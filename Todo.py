from os import system
import colorama
from colorama import Fore, Back, Style
import sqlite3

# Database Connection

try:
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    # print(Fore.RED + "Database Created/Connected" + Style.RESET_ALL)
except ConnectionError as e:
    print(e)


def newTaskInput():
    # print('New Input')

    try:
        print()
        task_id = int(input(Fore.LIGHTMAGENTA_EX + 'Enter Task Number : '))
        topic = input('Enter Topic : ')
        comment = input('Enter Comment : ' + Style.RESET_ALL)
        print()
        tableInsertion = '''INSERT INTO TaskList
                            (TASK_ID, TOPIC, COMMENT)
                            VALUES(?, ?, ?)'''

        cursor.execute(tableInsertion, (task_id, topic, comment))
        # print('Data Inserted')
        conn.commit()
        # print('Database Commit')
        system('clear')

    except Exception as i:

        print(i)


def taskCompleted():
    # print('Completed')

    try:
        completed = input(Fore.LIGHTMAGENTA_EX + 'Enter Task ID : ' + Style.RESET_ALL)
        deleteData = '''DELETE FROM TaskList WHERE TASK_ID = ?'''
        cursor.execute(deleteData, ([completed]))
        conn.commit()

        system('clear')

    except Exception as i:
        print(i)


class this_is_win:
    colorama.init()

    while True:
        print(Fore.CYAN + '*' * 50 + Style.RESET_ALL)
        print(Back.GREEN + ' ' * 20 + ' TODOLIST ' + ' ' * 20 + Style.RESET_ALL)
        print(Fore.CYAN + '*' * 50 + Style.RESET_ALL)
        print()

        try:
            tableCreation = '''CREATE TABLE IF NOT EXISTS TaskList
                                (
                                    TASK_ID INTEGER PRIMARY KEY,
                                    TOPIC TEXT NOT NULL,
                                    COMMENT TEXT NOT NULL);'''

            cursor.execute(tableCreation)
            # print(Fore.RED + "Table is created!" + Style.RESET_ALL)

        except Exception as e:
            print(e)

        try:
            cursor.execute("SELECT * FROM TaskList")
            dataFetch = cursor.fetchall()
            print(Fore.LIGHTMAGENTA_EX + ' ' * 10 + 'Total tasks for today : ' + Style.RESET_ALL,
                  Fore.YELLOW + str(len(dataFetch)) + Style.RESET_ALL)
            print()
            for row in dataFetch:
                print(Fore.BLUE + 'ID : ' + Style.RESET_ALL, Fore.YELLOW + str(row[0]) + Style.RESET_ALL)
                print(Fore.BLUE + 'Topic : ' + Style.RESET_ALL, Fore.YELLOW + str(row[1]) + Style.RESET_ALL)
                print(Fore.BLUE + 'Comment : ' + Style.RESET_ALL, Fore.YELLOW + str(row[2]) + Style.RESET_ALL)
                print()
        except Exception as e:
            print(e)

        try:
            print(Fore.CYAN + '*' * 50 + Style.RESET_ALL)
            print(Fore.RED + '1. Add task' + ' ' * 7 + '2. Task completed' + ' ' * 7 + '3. Exit' + Style.RESET_ALL)
            print(Fore.CYAN + '*' * 50 + Style.RESET_ALL)
            choice = int(input(Fore.GREEN + 'Choice : ' + Style.RESET_ALL))

            if choice == 1:
                newTaskInput()
            elif choice == 2:
                taskCompleted()
            elif choice == 3:
                break
            else:
                print(Fore.RED + 'Enter valid choice please !' + Style.RESET_ALL)

        except Exception as e:
            print(e)


this_is_win()
