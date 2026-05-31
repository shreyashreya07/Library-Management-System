from django import forms
from .models import Book
from .models import IssueBook



class BookForm(forms.ModelForm):

    class Meta:
        model = Book

        fields = ['title', 'author', 'category', 'quantity']
class IssueBookForm(forms.ModelForm):

    class Meta:

        model = IssueBook

        fields = ['student', 'book', 'due_date']