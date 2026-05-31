from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, IssueBook, Student
from .forms import BookForm, IssueBookForm


# Home Page
def home(request):

    total_books = Book.objects.count()

    total_students = Student.objects.count()

    issued_books = IssueBook.objects.count()

    returned_books = IssueBook.objects.filter(returned=True).count()

    context = {

        'total_books': total_books,

        'total_students': total_students,

        'issued_books': issued_books,

        'returned_books': returned_books,

    }

    return render(request, 'home.html', context)


# Show All Books
def books(request):

    query = request.GET.get('q')

    if query:

        all_books = Book.objects.filter(title__icontains=query)

    else:

        all_books = Book.objects.all()

    context = {

        'books': all_books

    }

    return render(request, 'books.html', context)


# Add Book
def add_book(request):

    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/books/')

    else:

        form = BookForm()

    context = {

        'form': form

    }

    return render(request, 'add_book.html', context)


# Delete Book
def delete_book(request, id):

    book = Book.objects.get(id=id)

    book.delete()

    return redirect('/books/')


# Edit Book
def edit_book(request, id):

    book = Book.objects.get(id=id)

    if request.method == 'POST':

        form = BookForm(request.POST, instance=book)

        if form.is_valid():

            form.save()

            return redirect('/books/')

    else:

        form = BookForm(instance=book)

    context = {

        'form': form

    }

    return render(request, 'edit_book.html', context)


# Issue Book
def issue_book(request):

    if request.method == 'POST':

        form = IssueBookForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/issued-books/')

    else:

        form = IssueBookForm()

    context = {

        'form': form

    }

    return render(request, 'issue_book.html', context)


# Show Issued Books
def issued_books(request):

    issued = IssueBook.objects.all()

    context = {

        'issued_books': issued

    }

    return render(request, 'issued_book.html', context)


# Return Book
def return_book(request, pk):

    issue = get_object_or_404(IssueBook, id=pk)

    issue.returned = True

    issue.save()

    return redirect('issued_books')