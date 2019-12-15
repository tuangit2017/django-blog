from django.shortcuts import render

def about_page(request):

    context = {
        'page_title': 'About',

    }
    return render(request,'about/about.html', context)

def team_page(request):
    context = {
        'page_title': 'Team',
    }
    return render(request,'about/team.html', context)

def project_page(request):
    new_data = [125.6,89.3,68.54,182.62,46.73,73.21,89.14,56.94,34.6]
    movies_name = ['Logan','Wonder Woman','Les Gardiens laxie Vol.2','Dunkerque','Spider-Man Homecoming','Baby Driver','John Wick2','Star Wars Episode VIII','Kong Skull Island','Ragnarok']
    time_min = [137,141,136,106,133,112,122,152,118,130]
    rate = [77,76,67,94,73,86,75,86,62,73]
    #votes = [420215,346166,310416,281939,252420,231734,203056,198563,180312,173344]
    context = {
    	'page_title': 'Projects',
    	'variable': new_data,
        'movies_name': movies_name,
        'time_min': time_min,
        'rate': rate,
        #'votes': votes
    }
    return render(request,'about/projects.html', context)
