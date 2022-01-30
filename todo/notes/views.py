from django.http import HttpResponse, request
from django.shortcuts import render
from notes.forms import AddNoteForm, Login
from notes.models import Note
from django.contrib.auth import authenticate, login


def index(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"])
    else:
        form = AddNoteForm()
    notes = Note.objects.all()
    return render(request, "note_list.html", {"notes": notes, "form": form})


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = Login()
    return render(request, 'login.html', {'form': form})
