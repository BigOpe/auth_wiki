from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect



from account.forms import SignupForm

# Create your views here.

def home(request):
    return render(request, "home.html")
    

def signup(request):

    if request.method == 'POST':
        form =SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            raw_password =form.cleaned_data.get('password1')
            user =authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('home')
    
    else:
        form =SignupForm()
    return render(request, 'signup.html',{'form':form})

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic= entry.signup

    if request.method != 'POST':
        form = SignupForm(instance=entry)
    else:
        form= SignupForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('signup' ,
                                        args=[signup.id]))

    context = {'entry': entry, 'form': form}
    return render(request, 'edit_entry.html', context)

    