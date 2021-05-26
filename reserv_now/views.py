from django.shortcuts import render
from reserv_now.models import HallOne, HallTwo, VipHall
from registration.models import UserProfile


def hall_one(request):
    context = dict()
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context["user_profile"] = user_profile

    tables = HallOne.objects.all()
    context["tables"] = tables
    return render(request, "hall_one.html", context=context)


def reserv_page(request):
    context = dict()
    if request.method == 'POST':
        print("asdasd")
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context["user_profile"] = user_profile
    # aviable tables count for hall 1
    tabbles_list_hallone = HallOne.objects.all()
    tables_av_one = 0
    context['tables'] = tabbles_list_hallone
    for table in context["tables"]:
        if table.reserved == False:
            tables_av_one += 1
    context["tables_av_one"] = tables_av_one

    #aviable tables count for 2 hell
    tabbles_list_halltwo = HallTwo.objects.all()
    table_two_av = 0
    for table in tabbles_list_halltwo:
        if table.reserved == False:
            table_two_av += 1
    context["tables_av_two"] = table_two_av

    #AVIABLE TABLES COUNT FOR VIP HALL
    tabbles_list_viphall = VipHall.objects.all()
    table_vip_av = 0
    for table in tabbles_list_viphall:
        if not table.reserved:
            table_vip_av += 1
    context["tables_av_vip"] = table_vip_av

    return render(request, 'hall_choice_page.html', context)
