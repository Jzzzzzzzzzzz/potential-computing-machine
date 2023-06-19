'''english_dict={
    "Яблоко":"Apple",
    "Молоко":"Milk",
    "Кот":"Cat"
}
if word in english_dict:
    word = input("Введите слово:")
    print(word, "на анг будет;:", english_dict[word])
else:
    print("Такого слова нет")'''



'''film_dict={
    "Начало":"Леонардо Ди Каприо",
    "Пираты Карибского моря":"Джонни Депп",
    "Острые Козырьки":"Томас Шелби"
}
film=input("Какой фильм вы собираетесь посмотреть?:")
f_actor="Леонардо Ди Каприо"
if film in film_dict:
    actor = film_dict.get[film]
    if actor == f_actor:
        print("Этот фильм стоит посмотреть!")
    else:
        print("я бы не стал тратить время!")
else:
    print("В словаре такого нету(")'''





questions=[
    {
        'question':'Кто из героев Marvel начал знакомство с Землей,попав под грузовик?',
        'answers':['Фил Колсон','Халк','Капитан Америка','правильного ответа нету'],
        'right_answers':4
    },
    {
        'question':'Как звучит полное имя брата Тора?',
        'answers':['Локи Одинсон','Локки Эриксон','Локки Лафейсон','правильного ответа нету'],
        'right_answers':3
    },
    {
        'question':'Какой злодей отличился тем,что за короткое время собрал в ангаре сотни управляемых дронов для армии США?',
        'answers':['Иван Ванко','Альтрон','Танос','правильного ответа нету'],
        'right answers':1
    }
]
name=input("Введите имя:")
score=0
for question_ in questions:
    print(question_.get('question'))
    answer_num = 0
    for answer in question_.get('answers'):
        answer_num += 1
        print(answer_num, '-', answer)
    user_answer = int(input("Введите ответ:"))
    if user_answer == question_.get('right answers'):
        print("Верно")
        score+=1
    else:
        print("Не верно")
print(score)
if score==3:
    print(f"{name},ты победил")
else:
    print(f"{name} ,ты Проиграл")














'''songs={
    "World in My Eyes":4.86,
    "Christmas song":10.0,
     "Halo":4.9
}
a=int(input("Сколько песен выбрать?:"))
for i in range(a):
    b=input(f"{i+1}-трек:")
a=input("Вы хотите узнать время звучания песен?")
if a=="Да":
    #что тут делать?????? разбирался долгое время,могу сделать так:

songs = {
     "World in My Eyes": 4.86,
     "Christmas song": 10.0,
     "Halo": 4.9
}
a=int(input("Сколько песен выбрать?:"))
if a ==1:
    b=input("1 Трек:")
    print(songs[b])
if a==2:
    a=input("1 Трек:")
    b=input("2 Трек:")
    print(songs[b]+songs[a])
if a==3:
    a=input("1 Трек:")
    b=input("2 Трек:")
    c=input("3 Трек:")
    print("Общее время звучания:",songs[b] + songs[a]+songs[c] ,sep="")'''


goods={
    "Лампа":"123456",
    "Стол":"23456",
    "Диван":"34567",
    "Стул":"45678"
}
store={
    "123456":[
        {"quan":27,"price":42}
    ],
    "23456":[
        {"quan":22,"price":510},
        {"quan":32,"price":520},
    ],
    "34567":[
        {"quan":2,"price":1200},
        {"quan":1,"price":1150},
    ],
    "45678":[
        {"quan":50,"price":100},
        {"quan":12,"price":95},
        {"quan":43,"price":97}
    ]
}
lamp_code = goods['Лампа']
table_code = goods['Стол']
sofa_code = goods['Диван']
chair_code = goods['Стул']

for i in range(4):
    a = input("лампа,стол,стул или диван?")
    b=a.lower()
    if a=="Лампа":
        lamp_code = goods['Лампа']
        lamps_item = store[lamp_code][0]
        lamps_quan = lamps_item['quan']
        lamps_price = lamps_item['price']
        lamps_cost = lamps_quan * lamps_price
        print('Лампа -', lamps_quan, 'шт, стоимость', lamps_cost, 'руб')
    if a=="Cтол":
        table_code = goods['Стол']
        table_item = store[table_code][0]
        table_item = store[table_code][1]
        table_quan = table_item['quant']
        table_quan = table_item['quant']
        sum(table_quan)
        table_price = table_item['price']
        table_cost1 = table_quan * table_price
        print('Стол -', table_quan, 'шт, стоимость', table_cost1, 'руб')
    if a=="Стул":
        hair_code = goods['Стул']
        chair_item = store[chair_code][0]
        chair_quan = chair_item['quan']
        chair_price = chair_item['price']
        chair_cost = chair_quan * chair_price
        print('Стул -', chair_quan, 'шт, стоимость', chair_cost, 'руб')
    if a=="Диван":
        sofa_code = goods['Диван']
        sofa_item = store[sofa_code][0]
        sofa_quan = sofa_item['quan']
        sofa_price = sofa_item['price']
        sofa_cost = sofa_quan * sofa_price
        print('Диван -', sofa_quan, 'шт, стоимость', sofa_cost, 'руб')






























