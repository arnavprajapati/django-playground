from django.http import HttpResponse
from django.shortcuts import render

menu_items = [
    {
        "id": 1,
        "name": "Masala Dosa",
        "price": 60,
        "description": "Crispy dosa with potato filling",
        "available": True
    },
    {
        "id": 2,
        "name": "Veg Burger",
        "price": 80,
        "description": "Fresh vegetable burger",
        "available": False
    },
]

def home(request):
    return render(request, 'menu/home.html', {
        'menu_items': menu_items
    })


def menu_detail(request, item_id):
    item = next(
        (item for item in menu_items if item['id'] == item_id),
        None
    )

    if item is None:
        return HttpResponse("Menu item not found", status=404)

    return render(request, 'menu/menu_detail.html', {
        'item': item
    })
