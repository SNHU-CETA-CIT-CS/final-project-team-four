from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Max and Jackson Final!")
