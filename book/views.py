from django.db.models import Sum, Max, Min, Avg
from book.models import Book
from django.shortcuts import render
from django.views.generic import ListView

def example(request):                                                        # function based view implementing aggregate 
    # data = Book.objects.aggregate(sum=Sum('ratings_count'))                # getting the sum of the ratings_count field .. this feild is an big integer field 

    data = Book.objects.aggregate(sum=Sum('ratings_count'), max=Max('ratings_count'),min=Min('ratings_count'),avg=Avg('ratings_count')) 
    # gets all of the following, sum, max, min, avg 

    print(data)
    return render(request, 'index.html', {"data":data})


class Example(ListView):                                                      # classed based view implementing aggregate 
    
    model = Book
    template_name = "index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(Example, self).get_context_data(*args, **kwargs)           # getting all the data from Book
        context['ratings_count'] = Book.objects.aggregate(Sum('ratings_count'))    # accessing ratings_count bound to the aggregate logic .. returns the sum of the ratings_count 
        return context                                                             # returning value of context varuale which is the sum 
