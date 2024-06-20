from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def cat_stats(request):
    context = {
        'name': 'Василий',
        'age': '1год',
        'happiness_level': '10',
        'hunger_level': '40'
    }
    return render(request, 'cat_stats.html', context=context)


def create_cat(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        print(request.POST.get('name')),
        print(request.POST.get('age')),
        print(request.POST.get('hunger_level')),
        print(request.POST.get('happiness_level'))
        CatsDb.cats.append(
            {
                'name': name,
                'age': 1,
                'hunger_level': 40,
                'happiness_level': 40
            }
        )


def play_cat():
    CatsDb.cats.hunger_level -= 10
    CatsDb.cats.happiness_level += 15


def feed_cat():
     CatsDb.cats.hunger_level += 15
     CatsDb.cats.happiness_level += 5
     if CatsDb.cats.hunger_level > 100:
         CatsDb.cats.happiness_level -= 30


def wake_cat():
    CatsDb.cats.happiness_level -= 5


def action(request):
    if request.method == 'GET':
        if option == '1':
            play_cat()
        if option == '2':
            feed_cat()
        if option == '3':
            wake_cat()

