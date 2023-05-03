from django.shortcuts import render

from .models import Product

from django.core.paginator import Paginator

def index(request):
    product_objects = Product.objects.all()


    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects, 2)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_objects': product_objects})

def detail(request, pk):
    product_object = Product.objects.get(pk=pk)
    return render(request, 'shop/detail.html', {'product_object': product_object})


def checkout(request):

    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        adress = request.POST.get('adress', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip = request.POST.get('zip', "")
    return render(request, 'shop/checkout.html')