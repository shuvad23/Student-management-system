from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nationality'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guardian Name'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guardian Phone'}),
            'guardian_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guardian Email'}),
            'guardian_relation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Relation with Guardian'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Name'}),
            'program_name': forms.Select(attrs={'class': 'form-select'}),
            'ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID'}),
            'previous_school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Previous School'}),
            'marks_percentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Marks Percentage'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EditStudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nationality'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guardian Name'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guardian Phone'}),
            'guardian_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guardian Email'}),
            'guardian_relation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Relation with Guardian'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Name'}),
            'program_name': forms.Select(attrs={'class': 'form-select'}),
            'ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID'}),
            'previous_school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Previous School'}),
            'marks_percentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Marks Percentage'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }