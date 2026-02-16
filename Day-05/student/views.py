from django.shortcuts import render
from .forms import AddStudentForm

def student_form(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddStudentForm()

    return render(request, "add_student.html", {"form": form})