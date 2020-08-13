from django.shortcuts import render , redirect , HttpResponseRedirect


from django.views import  View


def about(request):

        return render(request , 'about.html')

