from django.shortcuts import render


def mag_page(request):
    return render(request, 'mag_app/index.html')
