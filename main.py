""" Slovar morza """
morza_kirilica = {
    'а':' .- ',
    'б':' -... ',
    'в':' .--' ,
    'г':' --.' ,
    'д':' -..' ,
    'е':' . ' ,
    'ж':' ...-' ,
    'з':' --..' ,
    'и':' ..' ,
    'й':' .---' ,
    'к':' -.-' ,
    'л':' .-..' ,
    'м':' -- ' ,
    'н':' -. ' ,
    'о':' --- ',
    'п':' .--. ',
    'р':' .-. ',
    'с':' ... ',
    'т':' - ',
    'у':' ..- ',
    'ф':' ..-. ',
    'х':' .... ',
    'ц':' -.-. ',
    'ч':' ---. ',
    'ш':' ---- ',
    'щ':' --.- ',
    'ъ':' .--.-. ',
    'ы':' .-.. ',
    'ь':' -..- ',
    'э':' ...-... ',
    'ю':' ..-- ',
    'я':' .-.- ',
}

c = input('Русский - Морза: \nНапишите на русском\n')
res = []
for i in c.lower(): 
    res.append(morza_kirilica[i] + ' ')
result ="".join(res)
print(result)
print('Hello baby,My name is Sanjik,I am a bad boy,I have a big gone in my pants')

def gay_test(person):
    if person == 'gaayy'
        return True
    return False
