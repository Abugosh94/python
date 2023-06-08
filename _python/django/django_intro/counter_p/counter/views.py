from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if "visits" not in request.session:
        request.session["visits"]=0
    if "count" in request.session:
        print('count exists!')
        request.session["count"]+=1
    else:
        print("key 'count' does NOT exist")
        request.session["count"]=1

    request.session["visits"] +=1 
    return render(request, 'index.html')

#NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
def addtwo(request):
    request.session["count"]+=1

    return redirect("/")

#SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
def addcustom(request):
    amount = int(request.POST["amount"]) -1 
    request.session["count"]+=amount
    return redirect("/")

#NINJA BONUS: Add a Reset button to reset the counter
def destroy(request):
    request.session.pop("count")
    return redirect("/")

#Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
def destroysession(request):
    request.session.clear()
    return redirect("/")