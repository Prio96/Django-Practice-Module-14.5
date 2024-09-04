from django.shortcuts import render
from .forms import Form1
# Create your views here.
def viewform(request):
    if request.method=='POST':
        form=Form1(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=Form1()
    return render(request,'form.html',{'form':form})


    
