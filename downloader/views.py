from django.shortcuts import render
from pytube import YouTube

# Create your views here.

# test_url = "https://www.youtube.com/watch?v=57JeRBZMbiE&t=135s"


def home(request):
    if request.method == "POST":
        url = request.POST["url"]
        if "youtube" in url:
            try:
                video = YouTube(url)
                title = video.title
                streams = video.streams.filter(
                    file_extension="mp4", progressive=True).order_by('resolution')
                print("Title : ", title)

            except Exception as e:
                error_message = str(e)
                return render(request, 'home.html', {'error_message': error_message})

            return render(request, 'home.html', {'streams': streams})
    return render(request, "home.html")
