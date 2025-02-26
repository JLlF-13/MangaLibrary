from django.shortcuts import render, redirect
from django.contrib import messages
from biblioteca.models import Manga, Status, Origin, Language, Type
from django.shortcuts import render, redirect, get_object_or_404

def home_view(request):
    mangas=Manga.objects.all().order_by('name')
    total_spent = sum(manga.total_spend for manga in mangas)
    total_owned = sum(manga.owned for manga in mangas)
    total_collections = len(mangas)
    context = {
        'mangas': mangas,
        'total_spent': total_spent,
        'total_owned': total_owned,
        'total_collections': total_collections
    }
    #<td><a href="{% url 'view_manga' manga.id %}"><i class="fa-regular fa-eye"></i></a></td>
    #<td><a href="{% url 'edit_manga' manga.id %}"><i class="fa-regular fa-pen-to-square"></i></a></td>
    #<td><a href="{% url 'delete_manga' manga.id %}"><i class="fa-regular fa-x"></i></a></td>
    return render(request, 'Pages/home.html', context)

def create_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        photo = request.FILES['photo']
        observations = request.POST.get('observations', '')
        owned = request.POST['owned']
        total_books = request.POST['total_books']
        avg_price = request.POST['avg_price']
        total_spend = request.POST['total_spend']
        status_id = request.POST['status_id']
        origin_id = request.POST['origin_id']
        language_id = request.POST['language_id']
        type_id = request.POST['type_id']

        status = Status.objects.get(id=status_id)
        origin = Origin.objects.get(id=origin_id)
        language = Language.objects.get(id=language_id)
        type_ = Type.objects.get(id=type_id)

        # Verificar si ya existe un manga con el mismo nombre y idioma
        if Manga.objects.filter(name=name, language_id=language).exists():
            messages.error(request, 'This manga already exists in this language.')
            return redirect('create')

        manga = Manga(
            name=name,
            photo=photo,
            observations=observations,
            owned=owned,
            total_books=total_books,
            avg_price=avg_price,
            total_spend=total_spend,
            status_id=status,
            origin_id=origin,
            language_id=language,
            type_id=type_
        )
        manga.save()

        return redirect('home')  # Redirige a la vista principal después de agregar el manga

    statuses = Status.objects.all()
    origins = Origin.objects.all()
    languages = Language.objects.all()
    types = Type.objects.all()
    return render(request, 'Pages/create.html', {'statuses': statuses, 'origins': origins, 'languages': languages, 'types': types})

def manga_view(request, id):
    manga = get_object_or_404(Manga, id=id)
    return render(request, 'Pages/view.html', {'manga': manga})

def update_view(request, id):
    manga = get_object_or_404(Manga, id=id)
    if request.method == 'POST':
        manga.name = request.POST.get('name', manga.name)
        if 'photo' in request.FILES:
            manga.photo = request.FILES['photo']
        manga.observations = request.POST.get('observations', manga.observations)
        manga.owned = request.POST.get('owned', manga.owned)
        manga.total_books = request.POST.get('total_books', manga.total_books)
        manga.avg_price = request.POST.get('avg_price', manga.avg_price)
        manga.total_spend = request.POST.get('total_spend', manga.total_spend)
        manga.status_id = Status.objects.get(id=request.POST.get('status_id', manga.status_id.id))
        manga.origin_id = Origin.objects.get(id=request.POST.get('origin_id', manga.origin_id.id))
        manga.language_id = Language.objects.get(id=request.POST.get('language_id', manga.language_id.id))
        manga.type_id = Type.objects.get(id=request.POST.get('type_id', manga.type_id.id))
        manga.save()
        return redirect('home')

    statuses = Status.objects.all()
    origins = Origin.objects.all()
    languages = Language.objects.all()
    types = Type.objects.all()
    return render(request, 'Pages/update.html', {'manga': manga, 'statuses': statuses, 'origins': origins, 'languages': languages, 'types': types})

def delete_view(request, id):
    manga = get_object_or_404(Manga, id=id)
    manga.delete()
    return redirect("/")