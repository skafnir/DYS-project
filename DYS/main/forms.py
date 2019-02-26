from django import forms


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DonationStep1(forms.Form):
    what_things = forms.MultipleChoiceField()


class DonationStep2(forms.Form):
    amount = forms.IntegerField()


class DonationStep3(forms.Form):
    city = forms.CharField(max_length=64)
    type_of = forms.CharField(max_length=64)


class DonationStep4(forms.Form):
    organization = forms.CharField(max_length=64)


class DonationStep5(forms.Form):
    city = forms.CharField(max_length=64)
    street = forms.CharField(max_length=64)
    postal_code =forms..CharField(max_length=5)
    phone_number = forms.CharField(max_length=17)
    date = forms.DateField()
    time = forms.TimeField()
    extra_info = forms.CharField(widget=forms.Textarea)


