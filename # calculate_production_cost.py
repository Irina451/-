def calculate_cost(milk_cost_per_liter, rennet_cost_per_ml, salt_cost_per_kg, milk_volume, rennet_amount, salt_amount):
    """
    Рассчитывает общие затраты на производство сыра.
    
    :param milk_cost_per_liter: Стоимость молока за литр.
    :param rennet_cost_per_ml: Стоимость реннета за мл.
    :param salt_cost_per_kg: Стоимость соли за кг.
    :param milk_volume: Объем используемого молока в литрах.
    :param rennet_amount: Количество используемого реннета в мл.
    :param salt_amount: Количество используемой соли в кг.
    :return: Общая стоимость производства.
    """
    milk_cost = milk_volume * milk_cost_per_liter
    rennet_cost = rennet_amount * rennet_cost_per_ml
    salt_cost = salt_amount * salt_cost_per_kg
    total_cost = milk_cost + rennet_cost + salt_cost
    return total_cost

if __name__ == "__main__":
    milk_cost = float(input("Введите стоимость молока за литр: "))
    rennet_cost = float(input("Введите стоимость реннета за мл: "))
    salt_cost = float(input("Введите стоимость соли за кг: "))
    milk_volume = float(input("Введите объем молока (литры): "))
    rennet_amount = float(input("Введите количество реннета (мл): "))
    salt_amount = float(input("Введите количество соли (кг): "))
    total_cost = calculate_cost(milk_cost, rennet_cost, salt_cost, milk_volume, rennet_amount, salt_amount)
    print(f"Общая стоимость производства: {total_cost:.2f} руб.")
