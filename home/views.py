from django.shortcuts import render


# Basic Views: Index, About and Contact

def get_index(request):
    # Index view ('index.html' template)
    return render(request, 'index.html')


def get_about(request):
    # About page view ('About.html' template)
    return render(request, 'About.html')


def get_contact(request):
    # Contact page view ('contact.html' template)
    return render(request, 'contact.html')
