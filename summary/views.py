from modulefinder import packagePathMap
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Video
# Create your views here.
places = {
    "marinamall": "moderately safe",
    "saravanabhavan": "unsafe",
    "expressavenue": "safe",
    "higgimbothoms": "Best place for book lovers",
}

video_src = {
    "marinamall": "/media/video/22/Output_New_4_f4dOGsh.mp4",
    "expressavenue": "/media/video/22/Output_New_7.mp4",
    "saravanabhavan": "/media/video/22/Output_New_3_XhMs36c.mp4",
    "higgimbothoms": "/media/video/22/Output_New_5.mp4"
}


def location(request):

    placekey = list(places.keys())

    return render(request, "summary/places.html",
                  {
                      "placekey": placekey,
                  })


def place(request, p):
    try:
        video = Video.objects.all()
        challenge_text = places[p]
        video_url = video_src[p]
        return render(
            request, "summary/summary.html", {
                "text": challenge_text,
                "site": p,
                "video": video,
                "v": video_url,
            })

        # return HttpResponse(response_data)
    except:
        response_data = render_to_string("404.html")
        #raise Http404()
