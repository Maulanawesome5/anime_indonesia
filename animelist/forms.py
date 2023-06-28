from django import forms


class Pencarian(forms.Form):
    """
    Class untuk membuat form HTML dari modul bawaan Django
    """
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control me-2",
                "type": "search",
                "placeholder": "Search",
                "aria-label": "Search",
            }
        )
    )
