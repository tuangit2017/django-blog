from django.shortcuts import render


	
def newblog(request):

    context = {
        'page_title':'New Blog',

    }

    return render(request, 'newblog/home.html', context)
