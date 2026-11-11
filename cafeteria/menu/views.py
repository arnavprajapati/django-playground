from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Cafeteria!")


def menu_detail(request, item_id):
    return HttpResponse(f"Menu Item ID: {item_id}")