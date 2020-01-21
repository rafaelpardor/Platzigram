from datetime import date

users = [
    {
        'email':'rafael@platzi.com',
        'password':'125234',
        'first_name':'Rafael',
        'last_name':'Pardo Rodriguez',
        'is_admin': True,
        'bio':'Hola soy Rafael',
        'birth_date': date(1993,11,3)
    },{
        'email':'juan@gmail.com',
        'password':'y9834',
        'first_name':'Juan',
        'last_name':'Pardo Rodriguez',
        'bio':'Hola soy juan.'
    },{
        'email':'marmoz@hotmail.com',
        'password':'3785trj',
        'first_name':'Martha',
        'last_name':'Rodriguez Mozo',
        'is_admin':True,
        'bio':'Hola soy Martha'
    },{
        'email':'Alejandro@paper.com',
        'password':'khsd94',
        'first_name':'Alejandro',
        'last_name':'Pardo Chaves',
        'bio':'Holiwi'
    },{
        'email':'gordonfreeman@blackmesa.com',
        'password':'blackmesa1234',
        'first_name':'Gordon',
        'last_name':'Freeman',
        'is_admin': True,
        'bio':'Nunca va a haber Half-life 3'
    }
]

from posts.models import User
for user in users:
    obj = User(**user)
    obj.save()
    print('{}:{}'.format(obj.pk,obj.email))