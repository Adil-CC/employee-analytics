
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        passs = request.POST.get('passs')

        try:
            user = users.objects.get(user=user)
            if user.passs == passs:
                request.session['user_id'] = user.id
                return redirect(powerbi_dashboard)
            else:     
                return HttpResponse("<script>alert('Incorrect password');window.location='/'</script>")
        except users.DoesNotExist:
            return HttpResponse("<script>alert('User not Found');window.location='/'</script>")

    return render(request, 'index.html')

def powerbi_dashboard(request):
    embed_url = "https://app.powerbi.com/view?r=eyJrIjoiNGU1YzkyNDAtMGVjOS00MjA4LWFlM2MtYTcxYTcyMGY4YTg2IiwidCI6IjUwMDBmZmM1LTgxNjQtNDc2MC04MDNkLTE3ZWMwYzdiY2E5ZSJ9"
    return render(request, "emp.html", {'embed_url': embed_url})
