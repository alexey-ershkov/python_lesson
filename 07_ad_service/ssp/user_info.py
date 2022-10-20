from random import choice

GENDERS = ['male', 'female']
GEO = ['moscow', 'nn']


def get_user_info():
    return {'gender': choice(GENDERS), 'geo': choice(GEO)}
