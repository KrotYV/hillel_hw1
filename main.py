import re

def parse(query: str) -> dict:

    list_2 = re.split('\?|&', query)

    # for el in query.split('?'):
    #     list_2 = el.split('&')

    dict_res = dict()
    for el in list_2:
        if el.find('=') != -1:
            list_param = el.split('=')
            if list_param[0] != '':
                dict_res[list_param[0]] = list_param[1]
    return dict_res

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('://example.com/http') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://example.com/path/to/page?name=ferret&color=&&color1=purple') == {'name': 'ferret', 'color': '', 'color1': 'purple'}
    assert parse('https://e?name=ferret&=&&color1=purple') == {'name': 'ferret', 'color1': 'purple'}
    assert parse('https://e?name=ferret&=purple') == {'name': 'ferret'}
    assert parse('https://rozetka.com.ua/console/sc80020?producer=playstation&seller=rozetka&') == {'producer': 'playstation', 'seller': 'rozetka'}
    assert parse('https://rozetka.com/??producer=playstation&&&&&seller=rozetka&') == {'producer': 'playstation', 'seller': 'rozetka'}
    assert parse('https://e?name======ferret&color=purple') == {'name': '', 'color': 'purple'}
    assert parse('http://example.com/&') == {}
    assert parse('http://example.com/?name={r\"}') == {'name': '{r"}'}
    assert parse('http://example.com/?=') == {}
    assert parse('=http://example.com/?') == {}

def parse_cookie(query: str) -> dict:
    dict_res = dict()
    for el in query.split(';'):
        index_1 = el.find('=')
        if index_1 != -1 and index_1 != 0:
            dict_res[el[:index_1]] = el[index_1 + 1:]

    return dict_res


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('=Dima') == {}
    assert parse_cookie('name==Dima;') == {'name': '=Dima'}
    assert parse_cookie('name=Dima=Userage=28;') == {'name': 'Dima=Userage=28'}
    assert parse_cookie('name=Dima=User;age=28;weight=76;;;city=Kharkov;school=hillel') == {'name': 'Dima=User', 'age': '28', 'weight': '76', 'city': 'Kharkov', 'school': 'hillel'}
    assert parse_cookie('=;?*=;') == {'?*': ''}
    assert parse_cookie('name=Dima;;;;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;color=blue;season=spring;day=monday') == {'name': 'Dima', 'age': '28', 'color': 'blue', 'season': 'spring', 'day': 'monday'}
    assert parse_cookie('name=') == {'name': ''}
    assert parse_cookie('=') == {}
    assert parse_cookie('name=Alex;age=44;user_name=aleXx;school=hillel') == {'name': 'Alex', 'age': '44', 'user_name': 'aleXx', 'school': 'hillel'}



