from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306256293',
        'name': 'Darren Marcello Sidabutar',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)