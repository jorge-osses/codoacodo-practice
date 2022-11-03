from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")
    # n = 1
    # html_response = "<h1>Mi web</h1>"
    # for i in range(10):
    #     html_response += f"<h2>Esta es la portada N°{n}</h2>"
    #     n += 1
    # return HttpResponse(html_response)


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")
