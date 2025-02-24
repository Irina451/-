import time

def monitor_aging(temperature, humidity, duration_minutes):
    """
    Мониторинг условий созревания сыра.
    
    :param temperature: Температура в градусах Цельсия.
    :param humidity: Влажность в процентах.
    :param duration_minutes: Продолжительность мониторинга в минутах.
    """
    print(f"Начало мониторинга созревания при T={temperature}°C и влажности {humidity}%")
    for minute in range(duration_minutes):
        print(f"Минута {minute + 1}: Текущие условия - T={temperature}°C, Вл={humidity}%")
        time.sleep(60)  # Пауза на 1 минуту
    print("Мониторинг завершен.")

if __name__ == "__main__":
    temp = float(input("Введите желаемую температуру (°C): "))
    humid = float(input("Введите желаемую влажность (%): "))
    duration = int(input("Введите продолжительность мониторинга (минуты): "))
    monitor_aging(temp, humid, duration)
