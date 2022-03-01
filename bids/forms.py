import re
from django import forms
from . import models


class BidCreation(forms.ModelForm):
    class Meta:
        model = models.Bid
        exclude = ('bidder',)

        # this function will be used for the validation

    def clean(self):

        # data from the form is fetched using super function
        super(BidCreation, self).clean()

        # extract the username and text field from the data
        telephone = self.cleaned_data.get('telephone')
        dob = self.cleaned_data.get('dob')

        # if telephone:
        #     is_phone_valid = re.search("^[+\d]+[\d.\s()]*$", telephone)
        # print(self.cleaned_data)
        #
        # if not is_phone_valid:
        #     self._errors['telephone'] = self.error_class([
        #         "Telephone must start with a plus sign with no other symbols"])

        return self.cleaned_data
