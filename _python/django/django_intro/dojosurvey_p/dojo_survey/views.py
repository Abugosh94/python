from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == 'POST':
        name_from_form = request.POST["name"]
        location_from_form = request.POST["location"]
        language_from_form = request.POST["language"]
        gender_from_form = request.POST["gender"]
        comment_from_form = request.POST["comment"]
    context= {
        "name": name_from_form,
        "location": location_from_form,
        "language": language_from_form,
        "gender": gender_from_form,
        "comment": comment_from_form
    }

    return render(request,'result.html', context)
