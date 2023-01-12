from django.shortcuts import render
from .models import Director,Movie

# Create your views here.

def director_list(request):
    directors = Director.objects.all()
    context = {'directors': directors}
    return render(request, 'directors/director_list.html',context)

def director_detail(request, director_id):
    director = Director.objects.get(id=director_id)
    context = {'director': director}
    return render(request,'directors/director_detail.html',context)

def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request,'movies/movie_list.html',context)

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {'movie': movie}
    return render(request,'movies/movie_detail.html',context)


from .models import Director, Movie

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_directors = Director.objects.all().count()
    num_movies = Movie.objects.all().count()


    context = {
        'num_directors': num_directors,
        'num_movies': num_movies,
    }

    return render(request, 'index.html', context=context)