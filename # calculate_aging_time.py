def calculate_aging_time(cheese_type):
    """
    Рассчитывает время созревания для разных видов сыра.
    
    :param cheese_type: Тип сыра (например, "cheddar", "mozzarella", "gouda").
    :return: Время созревания в днях.
    """
    aging_times = {
        "cheddar": 60,
        "mozzarella": 1,
        "gouda": 90,
        "brie": 30,
        "parmesan": 120
    }
    return aging_times.get(cheese_type.lower(), None)

if __name__ == "__main__":
    cheese_type = input("Введите тип сыра (cheddar, mozzarella, gouda, brie, parmesan): ")
    aging_time = calculate_aging_time(cheese_type)
    if aging_time:
        print(f"Сыр типа {cheese_type} должен созревать {aging_time} дней.")
    else:
        print("Неизвестный тип сыра.")
