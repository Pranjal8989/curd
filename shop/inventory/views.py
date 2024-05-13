from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
# Create your views here.
def index(request):
    products = Product.objects.all()
    context= {
        'products':products,
    }
    return render(request,"home_images.html",context)


def add(request):
    Categorys= category.objects.all()
    size_type = size.objects.all()
    colors = Color.objects.all()
    context = {
        'Category' : Categorys,
        'sizes':size_type,
        'colors': colors,
    }
    return render(request,"add_product.html",context)

def insert(request):
    if request.method == "POST":
        product_name= request.POST.get('product_name')
        category= request.POST.get('category')
        size= request.POST.get('size')
        color= request.POST.get('color')
        material= request.POST.get('material')
        price= request.POST.get('price')
        quantity= request.POST.get('quantity')
        image = request.FILES.get('image') 
        description= request.POST.get('description')
        query =Product(product_name=product_name,category=category,size=size,color=color,material=material,price=price,quantity=quantity,image=image,description=description)
        query.save()
    return redirect("/list")

def list(request):
    products = Product.objects.all()
    Categorys= category.objects.all()
    size_type = size.objects.all()
    colors = Color.objects.all()
    context= {
        'products':products,
        'Category' : Categorys,
        'sizes':size_type,
        'colors': colors,
    }
    return render(request,"list.html",context)

def delete(request,id):
    data = Product.objects.get(id=id)
    data.delete()
    return redirect("/list")

def edit(request, id):
    categories = category.objects.all()
    sizes = size.objects.all()
    colors = Color.objects.all()
    product = Product.objects.get(id=id)
    
    if request.method == "POST":
        product_name = request.POST['product_name']
        category_id = request.POST['category']
        size_id = request.POST['size']
        color_id = request.POST['color']
        material = request.POST['material']
        price = request.POST['price']
        quantity = request.POST['quantity']
        image_file = request.FILES['images']
        description = request.POST['description']
        
        product.product_name = product_name
        product.category = category_id
        product.size = size_id
        product.color = color_id
        product.material = material
        product.price = price
        product.quantity = quantity
        product.image = image_file
        product.description = description
        product.save()
        
        return redirect("/list")

    context = {
        'products': product,
        'categories': categories,
        'sizes': sizes,
        'colors': colors,
    }
    return render(request, "edit.html", context)



