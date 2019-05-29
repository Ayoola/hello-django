import os

#setting our Django environment by using our project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hello_django.settings')

import django

django.setup()

from hello_world.models import User
from faker import Faker

fake=Faker()

def populate(n):
    for i in range(n):
        t=User.objects.get_or_create(first_name=fake.first_name(),last_name=fake.last_name(),email=fake.email())[0]
        t.save()
    return

#if __name__=='__main__':
    #populate(5)

print(User.objects.order_by('first_name'))
