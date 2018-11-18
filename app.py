""" Цель - сгенерировать все возможные комбинации кода посылки, зная только последние 11 символов
    
    Первые две латинские буквы (XX) обозначают тип почтового отправления:

    RA-RZ — регистрируемое отправление письменной корреспонденции (заказная карточка, письмо, бандероль, мелкий пакет (до 2 кг), мешок М);
    LA-LZ — отслеживаемое письмо, несколько подтипов; использование LZ требует двустороннего соглашения
    VA-VZ — письмо с объявленной ценностью;
    CA-CZ — международная посылка (более 2 кг);
    EA-EZ — экспресс-отправления (EMS);
    UA-UZ — нерегистрируемые и неотслеживаемые отправления, но которые обязаны проходить таможенные процедуры;
    ZA-ZZ — SRM-отправление (от simplified registered mail), простой регистрируемый пакет.
"""
first_letters = ['R', 'L', 'V', 'C', 'E', 'U', 'Z']
known_second_letters = ['U', 'H', 'J', 'N', 'M', 'W', 'Y', 'V']
input_string = '790684075UA'

count_of_first_letters = len(first_letters)
count_of_second_letters = len(known_second_letters)
print(count_of_first_letters, count_of_second_letters)
counter = 0

output_file = open("output.txt", "w")

for x in range(count_of_first_letters):
    for y in range(count_of_second_letters):
        first_block = first_letters[x]+known_second_letters[y]
        print(first_block)
        counter = counter + 1
        if (counter % 30) == 0:
            output_file.write('\n')
        output_file.write(first_block + input_string + '\n')



#def generator(input_string, known_second_letters):
