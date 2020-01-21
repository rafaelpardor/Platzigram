# Querys

```bash
from posts.models import User
rafael = User.objects.create(
    email='',
    password='',
    first_name='',
    last_name=''
)

juan = User()
juan.save()
juan.delete()

platzi_users = User.objects.filter(email__endswith='@platzi.com')
```
