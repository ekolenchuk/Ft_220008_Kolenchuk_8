def name_the_number(number):
    result = ''

    if number > 999:
        f = 2
        num = number // 1000
    else:
        f = 1
        num = number

    while f != 0:
        ones = num % 10
        tens = (num % 100) // 10 * 10
        if tens == 10:
            tens += ones
            ones = 0
        hundreds = (num % 1000) // 100 * 100

        match hundreds:
            case 100:
                result += 'сто '
            case 200:
                result += 'двести '
            case 300:
                result += 'триста '
            case 400:
                result += 'четеыреста '
            case 500:
                result += 'пятьсот '
            case 600:
                result += 'шестьсот '
            case 700:
                result += 'семьсот '
            case 800:
                result += 'восемьсот '
            case 900:
                result += 'девятьсот '
            case _:
                pass

        match tens:
            case 10:
                result += 'десять '
            case 11:
                result += 'одиннадцать '
            case 12:
                result += 'двенадцать '
            case 13:
                result += 'тринадцать '
            case 14:
                result += 'четырнадцать '
            case 15:
                result += 'пятнадцать '
            case 16:
                result += 'шестнадцать '
            case 17:
                result += 'семнадцать '
            case 18:
                result += 'восемнадцать '
            case 19:
                result += 'девятнадцать '
            case 20:
                result += 'двадцать '
            case 30:
                result += 'тридцать '
            case 40:
                result += 'сорок '
            case 50:
                result += 'пятьдесят '
            case 60:
                result += 'шестьдесят '
            case 70:
                result += 'семьдесят '
            case 80:
                result += 'восемьдесят '
            case 90:
                result += 'девяносто '
            case _:
                pass

        match ones:
            case 1:
                if f == 2:
                    result += 'одна тысяча '
                else:
                    result += 'один рубль '
            case 2:
                if f == 2:
                    result += 'две тысячи '
                else:
                    result += 'два рубля '
            case 3:
                if f == 2:
                    result += 'три тысячи '
                else:
                    result += 'три рубля '
            case 4:
                if f == 2:
                    result += 'четыре тысячи '
                else:
                    result += 'четыре рубля '
            case 5:
                result += 'пять '
            case 6:
                result += 'шесть '
            case 7:
                result += 'семь '
            case 8:
                result += 'восемь '
            case 9:
                result += 'девять '
            case _:
                pass

        if f == 2:
            if ones != 1 and ones != 2 and ones != 3 and ones != 4:
                result += 'тысяч '
        if f == 1:
            if ones != 1 and ones != 2 and ones != 3 and ones != 4:
                result += 'рублей '
        f -= 1
        num = number % 1000

    return result
