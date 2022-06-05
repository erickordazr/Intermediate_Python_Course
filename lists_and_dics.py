def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Erick", "lastname": "Ordaz"}

    super_list = [
        {"firstname": "Erick", "lastname": "Ordaz"},
        {"firstname": "José", "lastname": "Martínez"},
        {"firstname": "Gerardo", "lastname": "Martínez"},
        {"firstname": "Fabián", "lastname": "Martínez"},
        {"firstname": "Antonio", "lastname": "Martínez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "float_nums": [-2.1, -1.2, 1.2, 2.1],
    }

    for key, value in super_dict.items():
        print(key, ">", value)

if __name__ == '__main__':
    run()
