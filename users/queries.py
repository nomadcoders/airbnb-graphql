from .models import User


def resolve_user(info, id):
    return User.objects.get(id=id)
