from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Item,Transaction,Client
from django.shortcuts import render,get_object_or_404
from django import forms


def index(request):
	items_list=Item.objects.all()
	context={
		'items_list':items_list,	
	}	
	return render(request,'index.html',context)

def details(request,item_id):
	item=get_object_or_404(Item,pk=item_id)
	clients=Client.objects.all()
	return render(request,'details.html',{'item':item,'clients':clients})

def transferitm(request,item_id):
	client=Client.objects.get(place=request.POST.get("client"))
	item=Item.objects.get(pk=item_id)
	quantity=request.POST.get("quantity")
	transaction=Transaction(quantity=quantity,item=item,client=client)
	transaction.save()
	item.quantity=item.quantity-int(quantity)
	item.save()
	return render(request,'transferitm.html',{'transaction':transaction,'quantity':quantity,'item':item,'client':client})

def returnitm(request,item_id):
	client=Client.objects.get(place=request.POST.get("client"))
	item=Item.objects.get(pk=item_id)
	quantity=request.POST.get("quantity")
	transaction=Transaction(quantity=quantity,item=item,client=client)
	transaction.save()
	item.quantity=item.quantity+int(quantity)
	item.save()
	return render(request,'returnitm.html',{'transaction':transaction,'quantity':quantity,'item':item,'client':client})	
