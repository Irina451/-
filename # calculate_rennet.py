def calculate_rennet(milk_volume, rennet_concentration):
    """
    Рассчитывает количество реннета для свертывания молока.
    
    :param milk_volume: Объем молока в литрах.
    :param rennet_concentration: Концентрация реннета (мл на 1 л молока).
    :return: Требуемое количество реннета в мл.
    """
    return milk_volume * rennet_concentration

if __name__ == "__main__":
    milk_volume = float(input("Введите объем молока (в литрах): "))
    rennet_concentration = float(input("Введите концентрацию реннета (мл/л): "))
    required_rennet = calculate_rennet(milk_volume, rennet_concentration)
    print(f"Требуется {required_rennet:.2f} мл реннета.")
