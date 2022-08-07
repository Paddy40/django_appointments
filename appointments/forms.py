from django import forms
from appointments.models import Appointmenttable, Patienttable
from appointments.models import Logintable
from appointments.models import Querytable

class addUser(forms.ModelForm):
    class Meta:
      model = Patienttable
      widgets = {
            'address': forms.Textarea(attrs={'placeholder': 'Type placeholder text here..'}),
            'DoB': forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy','class':'datepicker'}),
      }
      fields = ["name", "DoB","sex","email","phone","address","history",]

class addLogin(forms.ModelForm):
    class Meta:
      model = Logintable
      fields = ("uname", "psswd","department","name","givenid",)

class addAppointments(forms.ModelForm):
    class Meta:
      model = Appointmenttable
      fields = ("docname","doctid","patientid","patientname","date","time",)

class addQuery(forms.ModelForm):
    class Meta:
      model = Querytable
      fields = ("name", "phone","email","query",)