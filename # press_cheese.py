def press_cheese(weight_kg, pressure_psi, duration_minutes):
    """
    Симуляция процесса прессования сыра.
    
    :param weight_kg: Вес сырной массы в кг.
    :param pressure_psi: Давление пресса в PSI.
    :param duration_minutes: Продолжительность прессования в минутах.
    """
    print(f"Прессование сыра весом {weight_kg} кг под давлением {pressure_psi} PSI...")
    for minute in range(duration_minutes):
        print(f"Минута {minute + 1}: Прессование продолжается.")
        time.sleep(60)  # Пауза на 1 минуту
    print("Прессование завершено.")

if __name__ == "__main__":
    weight = float(input("Введите вес сырной массы (кг): "))
    pressure = float(input("Введите давление пресса (PSI): "))
    duration = int(input("Введите продолжительность прессования (минуты): "))
    press_cheese(weight, pressure, duration)
