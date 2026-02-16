from django import forms


class AddStudentForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=1,max_value=30)
    email= forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    study_year = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    country= forms.CharField(max_length=30)
    school= forms.CharField(max_length=30)
    
    
    


