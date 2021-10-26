from django.shortcuts import render
from .models import Item

from django.shortcuts import render

from .forms import ItemForm, ItemFormSet

# Create your views here.
def index(request):
    items = Item.objects.all()
    #Edit items
    formsets = ItemFormSet()

    if request.method == 'POST':
        formsets = ItemFormSet(request.POST)
        print(formsets.is_valid(), formsets.errors)
        formsets.save(commit=False)

    #Delete item checked as "delete"

        cds = formsets.cleaned_data

        for i in range(len(cds) - 1):
            if cds[i]["deleteItem"] == True:
                Item.objects.filter(designation = cds[i]["designation"]).delete()
            #Edit item
            else:
                entree = Item.objects.get(designation = cds[i]["designation"])
                entree.price = cds[i]["price"]
                entree.remaining = cds[i]["remaining"]
                entree.deleteItem = cds[i]["deleteItem"]
                entree.save()

    #Add new item
        if cds[len(cds) - 1] != {}:
            Item(designation = cds[len(cds) - 1]["designation"],
                    price = cds[len(cds) - 1]["price"],
                    remaining = cds[len(cds) - 1]["remaining"],
                    deleteItem = cds[len(cds) - 1]["deleteItem"]).save()
            print()

    formsets = ItemFormSet()

    #Total value of merchandises
    ttl = 0
    for item in items:
        ttl += item.price * item.remaining

    context = {
        'items': items,
        'ttl': ttl,
        'forms': formsets,
    }
    
    return render(request, 'index.html', context)

def newItem(request):
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a form instance and populate it with data from the request
        form = ItemForm(request.POST)
        Item(designation = request.POST.get('designation'),
            price = request.POST.get('price'),
            remaining = request.POST.get('remaining')).save()
        return render(request, 'newItem.html', {'form': form})

    #if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm(request.POST)
    return render(request, 'newItem.html', {'form': form})