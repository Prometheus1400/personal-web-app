from django import forms


class contactForm(forms.Form):
    email = forms.EmailField(max_length=50, required=True)
    organization = forms.CharField(
        label='Company or Organization', max_length=50, required=False)
    message = forms.CharField(label='Message', max_length=500, required=True, widget=forms.Textarea(attrs={'placeholder':'Write your message to me here. :)'}))
    reason = forms.ChoiceField(label='Contact Reason', choices=(
        ('','Please select reason for contacting...'),
        ('1', 'Job Opportunity'),
        ('2', 'Question'),
        ('3', 'Other'),
    ))
