from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
    	self.name=None
    	self.message=None
    	super(ContactForm,self).__init__(*args,**kwargs)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

    def clean_name(self):
    	self.name=self.cleaned_data.get('name',None)


    def save(self,id=None):
    	print(self.name)



class ContactForm2(forms.Form):
    name = forms.CharField()
    message_p = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
