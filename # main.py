
from milk_preparation import prepare_milk
from curdling import curdle_milk
from pressing import press_cheese
from aging import age_cheese
from packaging import package_cheese

def main():
    print("Начало производства сыра...")
    
    # Этап 1: Подготовка молока
    milk = prepare_milk()
    print(f"Молоко готово: {milk}")
    
    # Этап 2: Свертывание молока
    curd = curdle_milk(milk)
    print(f"Сычужный сгусток создан: {curd}")
    
    # Этап 3: Прессование сыра
    cheese = press_cheese(curd)
    print(f"Сыр прессован: {cheese}")
    
    # Этап 4: Созревание сыра
    aged_cheese = age_cheese(cheese)
    print(f"Сыр созрел: {aged_cheese}")
    
    # Этап 5: Упаковка сыра
    packaged_cheese = package_cheese(aged_cheese)
    print(f"Сыр упакован: {packaged_cheese}")

if __name__ == "__main__":
    main()
