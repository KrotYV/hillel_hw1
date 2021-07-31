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
