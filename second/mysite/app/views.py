from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.



def movie_list(request):
    movie_objects= Movies.objects.all()




    #to get movie_name for search
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_objects = Movies.objects.filter(name__icontains=movie_name)



    # to get page number
    paginator=Paginator(movie_objects,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, 'app/movie_list.html', {'page_obj':page_obj})
