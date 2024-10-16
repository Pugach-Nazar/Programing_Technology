
data_list = {
    1:{
    'ціна':500,
    'назва' : 'годинник'
    },
    2:{
    'ціна': 300,
    'назва' : 'телефон'
    },
    3:{
    'ціна': 300,
    'назва' : 'телефон'
    },
     4:{
    'ціна': 300,
    'назва' : 'телефон'
    },
    5:{
    'ціна': 300,
    'назва' : 'телефон'
    }
    }

def get_last_id(data_list: dict[int, dict]) -> int:
    """функція повертає останнє id в словнику"""
    last_id = list(data_list.keys())
    return last_id[-1]


def add_item(data_list: dict[int, dict], item: dict) -> int:
    """функція додає новий пункт до словника\n
    повертає його id"""
    id = get_last_id(data_list) + 1
    data_list[id] = item
    return id

def update_item(data_list: dict[int, dict], id: int, item:dict) -> dict:
    """функція змінює значення в слонику на основі id \n
    повертає пункт словника по id \n
    повертає KeyError якщо такого id немає"""
    if id in data_list:
        data_list[id] = item
        return data_list[id]
    else:
        raise KeyError(f'Key {id} not found in the dictionary.')
    

def get_item(data_list:dict[int, dict], id:int) -> dict:
    """функція повертає пункт словника за id\n
    повертиає повертає KeyError якщо такого id немає"""
    return data_list[id]

def delete_item(data_list:dict[int, dict], id: int) -> dict:
    """функція видаляє пункт з словника по id \n
    повертає значення видаленого пункту \n
    повертає KeyError якщо такого id немає """
    if id in data_list:
        return(data_list.pop(id))
    else:
        raise KeyError(f'Key {id} not found in the dictionary.')
    
def show_items(data_list:dict[int, dict]) -> int:
    """функція виводить на екран всі пункти словника \n
    повертає кількість пунктів в словнику \n """
    for i in data_list:
        print(data_list[i], 'id = ', i)
    return len(data_list)

def show_menu():
    print("\n--- Меню ---")
    print("1. Показати всі товари")
    print("2. Додати товар")
    print("3. Оновити товар")
    print("4. Видалити товар")
    print("5. Переглянути товар за ID")
    print("6. Вийти")

def handle_show_items():
    print("\n--- Список товарів ---")
    count = show_items(data_list)
    print(f"\nЗагальна кількість товарів: {count}")

def handle_add_item():
    print("\n--- Додати новий товар ---")
    назва = input("Введіть назву товару: ")
    ціна = float(input("Введіть ціну товару: "))
    new_item = {'ціна': ціна, 'назва': назва}
    new_id = add_item(data_list, new_item)
    print(f"Товар успішно доданий з ID: {new_id}")

def handle_update_item():
    print("\n--- Оновити товар ---")
    id = int(input("Введіть ID товару: "))
    try:
        назва = input("Введіть нову назву товару: ")
        ціна = float(input("Введіть нову ціну товару: "))
        updated_item = {'ціна': ціна, 'назва': назва}
        update_item(data_list, id, updated_item)
        print(f"Товар з ID {id} успішно оновлено.")
    except KeyError:
        print(f"Товар з ID {id} не знайдено.")

def handle_delete_item():
    print("\n--- Видалити товар ---")
    id = int(input("Введіть ID товару: "))
    try:
        deleted_item = delete_item(data_list, id)
        print(f"Товар {deleted_item} успішно видалено.")
    except KeyError:
        print(f"Товар з ID {id} не знайдено.")

def handle_get_item():
    print("\n--- Переглянути товар за ID ---")
    id = int(input("Введіть ID товару: "))
    try:
        item = get_item(data_list, id)
        print(f"Товар з ID {id}: {item}")
    except KeyError:
        print(f"Товар з ID {id} не знайдено.")

def main():
    while True:
        show_menu()
        choice = input("\nВиберіть опцію: ")
        
        if choice == "1":
            handle_show_items()
        elif choice == "2":
            handle_add_item()
        elif choice == "3":
            handle_update_item()
        elif choice == "4":
            handle_delete_item()
        elif choice == "5":
            handle_get_item()
        elif choice == "6":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
