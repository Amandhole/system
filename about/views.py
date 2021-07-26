from django.shortcuts import redirect, render
from about.models import Data 

# Create your views here.
def add(request):
    if request.method=='POST':
      title=request.POST['title']
      price=request.POST['price']
      author=request.POST['author']
      publisher=request.POST['publisher']
      book=Data(title=title,price=price,publisher=publisher,author=author)
      book.save()
    return render(request,'creat_book.html')  

def read_book(request):  
  data=Data.objects.all()[::-1]
  context={'book_data':data}
  return render(request,'read_book.html',context)

def update_book(request,id):
      data=Data.objects.get(id=id)
      context={'data1':data}
      if request.method=='POST':
            title=request.POST['title']
            price=request.POST['price']
            author=request.POST['author']
            publisher=request.POST['publisher']
            book=Data(id=id,title=title,price=price,author=author,publisher=publisher)
            book.save()
            return redirect('read')
      return render(request,'update_book.html',context)      


