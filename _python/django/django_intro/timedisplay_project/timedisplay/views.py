from django.shortcuts import render, redirect
from datetime import datetime
    
def index(request):
    context = {
        "time": datetime.now().strftime((("%I:%M %p"))),
        "date" : datetime.now().strftime(("%Y-%m-%d"))
    }
    return render(request,'index.html', context)

def time_display(request):
    return redirect("/")
