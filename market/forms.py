from django.contrib.auth.models import User
from django import forms

from market.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "category", "seller_note"]


class ProfileForm(forms.ModelForm):
    show_on_board = forms.BooleanField(
        required=False, label="Show my name on the department board"
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
