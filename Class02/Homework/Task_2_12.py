# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа

sum = int(input('Введите сумму чисел S: '))
product = int(input('Введите произведение чисел P: '))
for x in range(sum):
    for y in range(product):
        if sum == x + y and product == x * y:
            print(x, y)
            break