from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def admin_home(request):
    return HttpResponse("Welcome Admin")

def add_book(request):
    form=BookForm() #storing the function in the forms.py in a variable
    if request.method=='POST': #POST is used when we get value from a form and to store it to a database.
        form=BookForm(request.POST)
        if form.is_valid(): #to validate the data enters in the form
            title=form.cleaned_data['title']
            author=form.cleaned_data['author']
            category=form.cleaned_data['category']
            price=form.cleaned_data['price']
            description=form.cleaned_data['description']
            Book.objects.create(
                title=title,
                author=author,
                category =category,
                price=price,
                description=description
            )
    return render(request,'add_book.html',{'form':form}) #storing the form in a variable like in for loop.


def category_list(request):
    cat = Category.objects.all()
    return render(request, 'category_list.html', {'cat': cat})

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def admin_dashboard(request):
    books = Book.objects.all()
    total_books = Book.objects.count()
    total_categories = Category.objects.count()
    return render(request, 'admin_dashboard.html', {
        'books': books,
        'total_books': total_books,
        'total_categories': total_categories
    })

def edit_book(request, id):
    book= Book.objects.get(id=id) #get by id bcz we need to edit or delete indivdually.
    if request.method=='POST': #post is an http method to create data #get to get data
        form=BookForm(request.POST)
        if form.is_valid():
            book.title=form.cleaned_data['title']
            book.author=form.cleaned_data['author']
            book.category=form.cleaned_data['category']
            book.price=form.cleaned_data['price']
            book.description=form.cleaned_data['description']
            book.save()
            return redirect('admin_dashboard')
    else:
        form=BookForm(initial={ #initial is used to display the old values in the fields while editing and using normal form
            'title':book.title, 
            'author':book.author,
            'category':book.category,
            'price':book.price,
            'description':book.description
        })
    return render(request, 'edit_book.html',{'form':form})

def delete_book(request, id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('admin_dashboard')
  
def edit_category(request, id):
    category= Category.objects.get(id=id)
    if request.method=="POST":
        form=CategoryForm(request.POST, instance=category) #instance is used when form object is there
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form=CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form':form})

def delete_category(request, id):
    category= Category.objects.get(id=id)
    category.delete()
    return redirect('category_list')