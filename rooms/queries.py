from .models import Room
from .types import RoomListResponse


def resolve_rooms(root, info, page=1):
    if page < 1:
        page = 1
    page_size = 5
    skipping = page_size * (page - 1)
    taking = page_size * page
    rooms = Room.objects.all()[skipping:taking]
    total = Room.objects.count()
    return RoomListResponse(arr=rooms, total=total)


def resolve_room(root, info, id):
    return Room.objects.get(id=id)
