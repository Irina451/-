class CheeseProductionLog:
    def __init__(self):
        self.log = []

    def add_entry(self, cheese_type, quantity_kg, date):
        entry = {
            "type": cheese_type,
            "quantity_kg": quantity_kg,
            "date": date
        }
        self.log.append(entry)
        print(f"Добавлена запись: {entry}")

    def show_log(self):
        if not self.log:
            print("Журнал пуст.")
        else:
            print("Журнал производства сыра:")
            for entry in self.log:
                print(f"- Тип: {entry['type']}, Количество: {entry['quantity_kg']} кг, Дата: {entry['date']}")

if __name__ == "__main__":
    log = CheeseProductionLog()
    while True:
        print("\n1. Добавить запись\n2. Просмотр журнала\n3. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            cheese_type = input("Введите тип сыра: ")
            quantity = float(input("Введите количество (кг): "))
            date = input("Введите дату (ГГГГ-ММ-ДД): ")
            log.add_entry(cheese_type, quantity, date)
        elif choice == "2":
            log.show_log()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")
