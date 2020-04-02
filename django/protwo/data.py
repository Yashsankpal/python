import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo.settings')
import django
django.setup()
from faker import Faker
from _protwo.models import User



fakegen = Faker()

def data(n=3):
    for i in range(n):
        fake_name = fakegen.name().split()
        first_name = fake_name[0]
        last_name = fake_name[1]
        email = fakegen.email()

        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)

if __name__ == '__main__':
    print("generating databases")
    data(15)
    print("created/updated")