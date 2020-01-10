from django.shortcuts import render, redirect
from .models import list
from .forms import formList
from django.contrib import messages



# Create your views here.
def index(request):

    if request.method == 'POST':
        form = formList(request.POST or None)

        if form.is_valid():
            form.save()
            list_items = list.objects.all()
            messages.success(request, ("Item has been added to the list"))
            return render(request, 'index.html', {'all_items': list_items})

        else:
            return render(request, 'index.html')

    else:

        list_items = list.objects.all()
        return render(request, 'index.html', {'all_items': list_items})



def delete(request, item_id):
    item = list.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ("Item has been deleted"))
    return redirect('index')




def cross_off(request, item_id):
    item = list.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('index')




def uncross(request, item_id):
    item = list.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('index')

