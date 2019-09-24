from django.shortcuts import render,  redirect, get_object_or_404
from .models import ourData, schedule
from .forms import addRegionForm
from django.contrib import messages

# Create your views here.
def home_view(request):
    get_data = ourData.objects.all().order_by('-id')
    myTemplate = 'demo/home.html'
    context = {
        'myData' : get_data
    }
    return render(request, myTemplate, context)

def dashboard(request):
    get_data = ourData.objects.all().order_by('-id')
    myTemplate = 'demo/dashboard.html'
    context = {
        'myData' : get_data
    }
    return render(request, myTemplate, context)


def addRegion(request):
    form   = addRegionForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('add_region')
    else:
        form = addRegionForm()
    context = {
        'form': form,
    }
    myTemplate = 'demo/addRegion.html'
    return render(request, myTemplate, context)

def updateRegion(request, id):
    instance = get_object_or_404(ourData, pk = id)
    form = addRegionForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, f'Region has been updated successifully!')
        return redirect ('home_view')
    context = {
        'form': form,
        'messages': messages
    }
    myTemplate = 'demo/addRegion.html'
    return render(request, myTemplate, context)


# View Schedule
def viewRegion(request, id):
    get_data = get_object_or_404(ourData, pk = id)
    context = {
        'myData': get_data,
    }
    myTemplate =  'demo/viewRegion.html'
    return render(request,myTemplate,context)


# Delete Schedule
def deleteRegion(request, id):
    get_data = get_object_or_404(ourData, pk = id)
    get_data.delete()
    messages.success(request, f'Region deleted successfull!')
    return redirect('home_view')


# ============================== Test Custom Form  ==============================

def empl_view(request):
    get_empl = schedule.objects.all().order_by('-id')
    context = {
        'empls': get_empl
    }
    myTemplate = 'demo/emplView.html'
    return render(request, myTemplate, context)

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        project = request.POST.get('p_name')
        appointmentDate = request.POST.get('app_date')
        get_salary = request.POST.get('salary')
        d_contract = request.POST.get('d_contract')
        e_contract = request.POST.get('e_contract')
        form = schedule( full_name = name, project_name = project, appointment_date = appointmentDate, salary = get_salary, date_of_contract = d_contract, end_of_contract = e_contract)
        form.save()
        return redirect('add_employee')
    else:
        myTemplate = 'demo/addEmployee.html'
        return render(request, myTemplate,{})


def updateEmployee(request, id):
    get_data = get_object_or_404(schedule, pk = id)

    if request.method == 'POST':
            name = request.POST.get('name')
            project = request.POST.get('p_name')
            appointmentDate = request.POST.get('app_date')
            get_salary = request.POST.get('salary')
            d_contract = request.POST.get('d_contract')
            e_contract = request.POST.get('e_contract')
            # MyModel.objects.filter(pk=some_value).update(field1='some value')
            toUpdate = schedule.objects.filter(pk = get_data.id)
            toUpdate.update( full_name = name, project_name = project, appointment_date = appointmentDate, salary = get_salary, date_of_contract = d_contract, end_of_contract = e_contract)
            return redirect ('view_employee')
    context = {
        'myData': get_data,
        'messages': messages
    }
    myTemplate = 'demo/updateEmployee.html'
    return render(request, myTemplate, context)


def viewEmployee(request, id):
    get_data = get_object_or_404(schedule, pk = id)
    context = {
        'myData': get_data,
    }
    myTemplate =  'demo/viewEmployee.html'
    return render(request,myTemplate,context)


# Delete Schedule
def deleteEmployee(request, id):
    get_data = get_object_or_404(schedule, pk = id)
    get_data.delete()
    messages.success(request, f'Employee deleted successfull!')
    return redirect('view_employee')
