def csv_reader(csv_path: str) -> list:
    """
    Считывает и возвращает таблицу в виде 2-мерного списка

    Args:
        csv_path (str): Путь к csv-файлу

    Returns:
        list: 2-мерный список с таблицей
    """
    req_columns = [
        "ФИО полностью",
        "Департамент",
        "Отдел",
        "Должность",
        "Оценка",
        "Оклад",
    ]

    try:
        with open(csv_path, "r", newline="") as csvfile:
            csvfile = list(csvfile)
    except FileNotFoundError:
        print("Не удалось открыть файл, введите корректный путь файла")
        return None

    for i in range(len(csvfile)):
        csvfile[i] = csvfile[i].replace("\r", "").replace("\n", "")
        csvfile[i] = csvfile[i].split(";")

    if csvfile[0] != req_columns:
        print("В файле нет требуемых колонок, проверьте входной файл")
        return None

    return csvfile[1:]


def print_hierarchy(table: list) -> None:
    """
    Выводит на экран иерархию департаментов-команд

    Args:
        table (list): Таблица в виде 2-мерного списка
    """
    deps_nm = list(set([item[1] for item in table]))
    deps = {k: set() for k in deps_nm}

    for item in table:
        deps[item[:][1]].add(item[2])

    for dep in deps_nm:
        print("{}:".format(dep))
        for item in deps[dep]:
            print("\t{}".format(item))


def create_report(table: list, mode: str) -> None:
    """
    Создает сводный отчет по департаментам

    Args:
        table (list): Таблица в виде 2-мерного списка
        mode (str): Режим работы:
                        'print' – вывод на экран
                        'save' – сохранить в csv
    """
    deps_nm = list(set([item[1] for item in table]))
    deps_info = {
        k: {"size": 0, "min_sal": -1, "max_sal": -1, "sum_sal": 0}
        for k in deps_nm
    }

    for item in table:
        # увеличиваем size на 1
        deps_info[item[1]]["size"] += 1
        # берем min(cur_min, salary)
        if deps_info[item[1]]["min_sal"] == -1:
            deps_info[item[1]]["min_sal"] = float(item[5])
        else:
            deps_info[item[1]]["min_sal"] = min(
                deps_info[item[1]]["min_sal"], float(item[5])
            )
        # берем max(cur_min, salary)
        deps_info[item[1]]["max_sal"] = max(
            deps_info[item[1]]["max_sal"], float(item[5])
        )
        # добавляем текущую зп к суммарной зп по департаменту
        deps_info[item[1]]["sum_sal"] += float(item[5])

    if mode == "print":
        for dep in deps_nm:
            avg_sal = deps_info[dep]["sum_sal"] / deps_info[dep]["size"]

            print("{}:".format(dep))
            print("\tnum of employees: {}".format(deps_info[dep]["size"]))
            print(
                "\tsalary range: {:,} – {:,}".format(
                    int(round(deps_info[dep]["min_sal"], 0)),
                    int(round(deps_info[dep]["max_sal"], 0)),
                ).replace(",", " ")
            )
            print("\tavg salary: {}".format(int(round(avg_sal, 0))))
    elif mode == "save":
        table_columns = ["department", "num of employees",
                         "salary range", "avg salary"]
        # записываем в файл
        with open("report.csv", "w", newline="") as csvfile:
            csvfile.write(";".join(table_columns) + "\n")
            for dep in deps_nm:
                avg_sal = deps_info[dep]["sum_sal"] / deps_info[dep]["size"]

                line = [
                    dep,
                    str(deps_info[dep]["size"]),
                    "{:,} – {:,}".format(
                        int(round(deps_info[dep]["min_sal"], 0)),
                        int(round(deps_info[dep]["max_sal"], 0)),
                    ).replace(",", " "),
                    str(int(round(avg_sal, 0))),
                ]
                csvfile.write(";".join(line) + "\n")
        print("Отчет успешно сохранен в report.csv")


if __name__ == "__main__":
    table = None
    while table is None:
        csv_nm = input("Введите путь к csv-файлу: ")
        table = csv_reader(csv_nm)

    option_text = (
        "\nДопустимые значения команд:\n"
        "\t1 - вывести иерархию команд\n"
        "\t2 - вывести сводный отчёт по департаментам\n"
        "\t3 - сохранить сводный отчёт по департаментам в csv\n"
        "\tend – завершить работу\n"
        "Введите команду: "
    )

    while True:
        option = input(option_text)

        if option == "1":
            print_hierarchy(table)
        elif option == "2":
            create_report(table, "print")
        elif option == "3":
            create_report(table, "save")
        elif option == "end":
            break
        else:
            print("Такой команды не существует, введите другую")
