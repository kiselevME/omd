def csv_reader(csv_nm: str) -> list:
    """
    Считывает и возвращает таблицу в виде 2-мерного списка

    Args:
        csv_nm (str): Путь к csv-файлу

    Returns:
        list: 2-мерный список с таблицей
    """
    req_columns = ['ФИО полностью', 'Департамент', 'Отдел',
                   'Должность', 'Оценка', 'Оклад']

    with open(csv_nm, 'r', newline='') as csvfile:
        csvfile = list(csvfile)
    for i in range(len(csvfile)):
        csvfile[i] = csvfile[i].replace('\r', '').replace('\n', '')
        csvfile[i] = csvfile[i].split(';')

    if csvfile[0] != req_columns:
        raise Exception('Check the columns in input file')

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
        print(f'{dep}:')
        for item in deps[dep]:
            print(f'\t{item}')


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
    deps_info = {k: {'size': 0,
                     'min_sal': -1,
                     'max_sal': -1,
                     'sum_sal': 0}
                 for k in deps_nm}

    for item in table:
        # увеличиваем size на 1
        deps_info[item[1]]['size'] += 1
        # берем min(cur_min, salary)
        if deps_info[item[1]]['min_sal'] == -1:
            deps_info[item[1]]['min_sal'] = float(item[5])
        else:
            deps_info[item[1]]['min_sal'] = min(deps_info[item[1]]['min_sal'],
                                                float(item[5]))
        # берем max(cur_min, salary)
        deps_info[item[1]]['max_sal'] = max(deps_info[item[1]]['max_sal'],
                                            float(item[5]))
        # добавляем текущую зп к суммарной зп по департаменту
        deps_info[item[1]]['sum_sal'] += float(item[5])

    if mode == 'print':
        for dep in deps_nm:
            avg_sal = deps_info[dep]["sum_sal"]/deps_info[dep]["size"]

            print(f'{dep}:')
            print(f'\tnum of employees: {deps_info[dep]["size"]}')
            print(f'\tsalary range: {deps_info[dep]["min_sal"]}–'
                  f'{deps_info[dep]["max_sal"]}')
            print(f'\tavg salary: {avg_sal}')
    elif mode == 'save':
        table_columns = ['department', 'num of employees',
                         'salary range', 'avg salary']
        # cоздаем файл (если он не существует)
        with open('report.csv', 'a', newline='') as csvfile:
            pass
        # записываем в файл
        with open('report.csv', 'w', newline='') as csvfile:
            csvfile.write(';'.join(table_columns)+'\n')
            for dep in deps_nm:
                line = [dep,
                        str(deps_info[dep]['size']),
                        f'{deps_info[dep]["min_sal"]}–'
                        f'{deps_info[dep]["max_sal"]}',
                        str(deps_info[dep]['sum_sal']/deps_info[dep]['size'])]
                csvfile.write(';'.join(line)+'\n')


if __name__ == '__main__':
    csv_nm = input('Введите путь к csv-файлу: ')
    table = csv_reader(csv_nm)

    option_text = 'Допустимые значения команд:\n'\
                  '\t1 - вывести иерархию команд\n'\
                  '\t2 - вывести сводный отчёт по департаментам\n'\
                  '\t3 - сохранить сводный отчёт по департаментам в csv\n'\
                  'Введите команду: '
    option = input(option_text)

    if option == '1':
        print_hierarchy(table)
    elif option == '2':
        create_report(table, 'print')
    elif option == '3':
        create_report(table, 'save')
    else:
        raise Exception('Input command is not supported')
