from django import forms

class ApplicationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    dob = forms.DateField(label='Date of Birth')
    age = forms.IntegerField(label='Age', min_value=0)
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phone = forms.CharField(label='Phone Number', max_length=10)
    email = forms.EmailField(label='Email Address')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    district = forms.ChoiceField(label='District', choices=[('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Kozhikode', 'Kozhikode'), ('Kottayam', 'Kottayam')])
    branch = forms.ChoiceField(label='Branch', choices=[])
    account_type = forms.ChoiceField(label='Account Type', choices=[('savings', 'Savings Account'), ('current', 'Current Account'), ('fixed_deposit', 'Fixed Deposit')])
    materials_provided = forms.ChoiceField(label='Materials Provided', choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')])
