from accounts.models import User


def gen_master(apps, schema_editor):
    for id in range(1, 4):
        username = f"user{id}"
        password = f"user{id}"
        first_name = f"이름{id}"
        last_name = f"성{id}"
        email = f"test{id}@test.com"
        gender = 'M'

        User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name,
                                 email=email, gender=gender)
