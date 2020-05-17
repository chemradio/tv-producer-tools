from time import strftime, gmtime
from pprint import pprint
import re
srtin = 'Это были все новости, 349 которых мы хотели вам рассказать.Смотрите нас в социальных сетях, в эфире своих национальных телеканалов и в прямом эфире круглосуточного канала Настоящее время в Ютубе (24 часа в сутки, 7 дней в неделю). Мы встретимся с вами завтра в это же время. Всего доброго. До встречи в эфире.'


def calc_readtime(text, wpm=160):
    words = re.findall(r'[а-яА-Яa-zA-Z]+', text)
    # pprint(f'{words}, {len(words)}')
    digits = re.findall(r'[1-9]', text)
    # print(f'{digits}, {len(digits)}')
    word_count = len(words) + len(digits)
    seconds = word_count / wpm * 60
    time = strftime("%M:%S", gmtime(seconds))
    return time

# print(calc_readtime(srtin))