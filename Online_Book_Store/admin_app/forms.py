from django import forms
from . models import *

class BookForm(forms.Form):
    title = forms.CharField(max_length=200, label="Book Title")
    author = forms.CharField(max_length=100, label="Author Name")
    category = forms.ModelChoiceField(  #here we are importing category foreign key.
        queryset = Category.objects.all(),  #means the dropdown will show all categories from the Category model.
        empty_label="Select Category"    #adds a default blank choice in the dropdown.
    )
    price = forms.DecimalField(max_digits=6, decimal_places=2, label="Price")
    description = forms.CharField(widget=forms.Textarea, label="Book Description") #widget=forms.textarea - widget makes this a multi-line input instead of a single-line text box.

class CategoryForm(forms.ModelForm): #form is directly tied to the Category model.
#Meta is an inner class in Django used to configure metadata for a form or model. It’s not a field itself—it’s like a “settings panel” for your form or model that tells Django how to behave.
    class Meta:   #Meta, fields, model, widgets, help_texts are inbuilt functions
        model=Category #Tells Django which model this form is for.
        fields=['category_name', 'cat_description']  #Specifies which model fields to include in the form.

        labels = {
            'category_name': 'Category Name',
            'cat_description': 'Description',
        }

        widgets = {  #widgets → Customize the HTML rendering of fields (e.g., adding CSS classes, placeholders).
            'category_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'cat_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter category descriptions'}),
        }

        help_texts = {
            'category_name': 'Enter a short and unique name for the category.',
        }

#Use forms.Form when you want full control and the form isn’t directly tied to a model.

#Use forms.ModelForm when the form is tied to a model — Django handles a lot automatically, and you can just customize it via Meta.

#ModelChoiceField is great for dropdowns from other models (like ForeignKeys).

#widgets and help_texts improve user experience with better styling and guidance.