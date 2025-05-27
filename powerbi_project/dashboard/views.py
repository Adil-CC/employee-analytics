
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id

                # Replace this URL with your actual Power BI Dashboard link
                powerbi_url = "https://app.powerbi.com/view?r=YOUR-DASHBOARD-ID"
                return redirect(powerbi_dashboard)
            else:
                return HttpResponse("Incorrect password", status=401)
        except CustomUser.DoesNotExist:
            return HttpResponse("User not found", status=404)

    return render(request, 'login.html')

def powerbi_dashboard(request):
  #  embed_url = "https://app.powerbi.com/reportEmbed?reportId=dc98b537-0ccc-40d0-904f-180f7e0e6e6f&autoAuth=true&ctid=5000ffc5-8164-4760-803d-17ec0c7bca9e"
    return render(request, "dashboard.html",)