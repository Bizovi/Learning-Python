from django.shortcuts import render
from django.http import HttpResponse

# some fake posts
posts = [
    {
        'author':'Bizovi Mihai',
        'title':'Caratheodori Theorem',
        'content':'''In order to build adequate models of economic and
            other complex phenomena, we have to take into account their
            inherent stochastic nature. Data is just the appearance, an
            external manifestation of some latent processes
             (seen as random mechanisms).
             Even though we won’t know the exact outcome for sure,
              we can model general regularities and relationships as a
              result of the large scale of phenomena.
              For more ideas see (Ruxanda 2011)''',
        'date':'2018-09-10'
    },
    {
        'author':'Bizovi Mihai',
        'title':'King County Home Prices Prediction',
        'content':'''The King County Homes prices prediction challenge
            is an excellent dataset for trying out and experimenting
            with various regression models. As we’ll see in the
            following post on Moscow flats, the modeler deals with
            similar challenges: skewed data and outliers, highly
            correlated variables (predictors), heteroskedasticity
            and a geographical correlation structure.
            Ignoring one of these may lead to undeperforming models,
            so in this post we’re going to carefully explore the
            dataset, which should inform which modeling strategy
            to choose.''',
        'date':'2018-08-01'
    }
]

# Create some views so that it does something
def home(request):
    """
    Input: request, mandatory
    Return: what they want to see when hit home/

    Templates:
        1. HttpResponse('<h1>Blog Home</h1>')
        2. Shortcut django.shortcuts.render the template
    Context:
        can pass information into the template
    """
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
