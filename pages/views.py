from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, title_choices
from listings.models import Listing
from artists.models import Artist


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {

        'listings': listings,
        'title_choices': title_choices,
        'price_choices': price_choices

    }
    return render(request, 'pages/index.html', context)


def about(request):
    artists = Artist.objects.order_by('-hire_date')
    # get mvp
    mvp_artists = Artist.objects.all().filter(is_mvp=True)
    context = {
        'artists': artists,
        "mvp_artists": mvp_artists

    }
    return render(request, 'pages/about.html', context)
