from django.shortcuts import redirect, render

from .models import Students

# Create your views here.

def index(request):
    std = Students.objects.all()
    context = {
        'stds':std
    }
    return render(request, 'index.html', context)



def addStudent(request):
    if(request.method == 'POST'):
        fname = request.POST.get("userFname")
        lname = request.POST.get("userLname")
        email = request.POST.get("userEmail")
        stdObj = Students(firstName = fname, lastName = lname, email = email)
        stdObj.save()
        return redirect(index)
    return render(request, 'addStudent.html')




def update(request , id):
    stdUpd = Students.objects.get(id = id)
    context = {
        'stdUpd' : stdUpd
    }
    if(request.method == 'POST'):
        fname = request.POST.get("userFname")
        lname = request.POST.get("userLname")
        email = request.POST.get("userEmail") 
        stdObj = Students(id = id,firstName = fname, lastName = lname, email = email)
        stdObj.save()
        return redirect(index)
    return render(request, 'update.html',context)


def delete(request, id):
    stdDel = Students.objects.get(id = id)
    stdDel.delete()
    return redirect(index)