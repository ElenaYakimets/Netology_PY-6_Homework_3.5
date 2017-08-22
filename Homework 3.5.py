import osa


def convert_temp(path):
    """
    Конвертиртация температуры
    :param path: путь к файлу с температурами
    :return: температура в градусах Цельсия
    """
    with open(path) as f:
        for line in f:
            temp = line.split()
            if temp[1] == 'F':
                temp[1] = 'degreeFahrenheit'
            client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
            print(client.service.ConvertTemp(
                Temperature=float(temp[0]),
                FromUnit=temp[1],
                ToUnit='degreeCelsius'
            ))
print('Температуры:')
convert_temp('temps.txt')


def convert_money(path):
    """
    Конвертация валюты
    :param path: путь к файлу с валютами
    :return: округленная сумма в рублях
    """
    total_cost = 0
    with open(path) as f:
        for line in f:
            money_amount, money_currency = line.split()[1:]
            client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
            total_cost += client.service.ConvertToNum(
                fromCurrency=money_currency,
                toCurrency='RUB',
                amount=money_amount,
                rounding=True
            )
    print(round(total_cost))
print('--------------------\nСуммарная стоимость:')
convert_money('currencies.txt')


def convert_distance(path):
    """
    Конвертация длинны
    :param path: путь к файлу с длиннами путей
    :return: сумма путей в километрах, округленная до сотых
    """
    total_length = 0
    with open(path) as f:
        for line in f:
            length = line.split()[1:]
            if length[1] == 'mi':
                length[1] = 'Miles'
            client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
            total_length += client.service.ChangeLengthUnit(
                LengthValue=float(length[0].replace(',','')),
                fromLengthUnit=length[1],
                toLengthUnit='Kilometers',
            )
    print(round(total_length, 2))
print('--------------------\nСуммарный путь:')
convert_distance('travel.txt')
