from time import strftime, gmtime
import re
srtin = 'Это были все новости, которых мы хотели вам рассказать. Смотрите нас в социальных сетях, в эфире своих национальных телеканалов и в прямом эфире круглосуточного канала Настоящее время в Ютубе (24 часа в сутки, 7 дней в неделю). Мы встретимся с вами завтра в это же время. Всего доброго. До встречи в эфире.'


def calc_readtime(text, wpm=160):
    words = re.split('; |, |\*|\n | ', text)
    word_count = len(words)
    seconds = word_count / wpm * 60
    time = strftime("%M:%S", gmtime(seconds))
    return time