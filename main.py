import re


# Задание 1
def get_domain_from_link(link: str):
    """Извлечение домена из URL-адреса"""

    return re.findall(r'[a-z-]+(?=\.[a-z/]+$)', link)[0]


link_1 = 'http://github.com/carbonfive/raygun'
link_2 = 'http://www.zombie-bites.com'
link_3 = 'https://www.cnet.com'

print(get_domain_from_link(link_1))
print(get_domain_from_link(link_2))
print(get_domain_from_link(link_3))


# Задание 2
def moving_zeros(numbers_list: list):
    """Перемещение нулей в конец массива"""

    no_zeros_list = []
    zeros_list = []

    for number in numbers_list:
        if number != 0:
            no_zeros_list.append(number)
        else:
            zeros_list.append(number)

    moving_zeros_list = no_zeros_list + zeros_list

    return moving_zeros_list


massif = [1, 0, 1, 2, 0, 1, 3]

print(moving_zeros(massif))


# Задание 3
def get_hashtag_from_string(input_string: str):
    """Генератор хэштегов"""

    if input_string != ' ':
        words_list = input_string.split(' ')
        hashtag_string = ['#']

        for word in words_list:
            hashtag_string.append(word.title())

        hashtag_string = ''.join(hashtag_string)

        if len(hashtag_string) > 140 or len(hashtag_string) == 0:
            return False
        else:
            return hashtag_string
    else:
        return False


print(get_hashtag_from_string(' Hello there thanks for trying my Kata'))
print(get_hashtag_from_string(' Hello World '))
print(get_hashtag_from_string(' '))
