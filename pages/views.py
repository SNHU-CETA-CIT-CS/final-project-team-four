from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Maxx and Jackson Final!")
