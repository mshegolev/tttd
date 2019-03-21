from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', content_type=list,
                  context={'values': ['Если у вас остались вопросы, то задавайте по телефону', '(123) 123-34-56',
                                      'mshegolev@gmail.com']})
