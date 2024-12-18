from django.shortcuts import render
from .service import get_all_characters, get_character_by_page, get_character_by_id

def index(request):
    # Получаем номер страницы из параметров запроса, по умолчанию 1
    page = request.GET.get('page', 1)
    
    try:
        # Получаем персонажей для текущей страницы
        characters = get_character_by_page(page=page)
    except ValueError as e:
        characters = []  # В случае ошибки возвращаем пустой список
    except Exception as e:
        return render(request, 'error.html', {"error": str(e)})
    if not characters:
        return render(request, 'error.html', {"error": "No characters found"}) 
    
    next_page = characters['info']['next'].split('=')[1] if characters['info']['next'] else None
    previous_page = characters['info']['prev'].split('=')[1] if characters['info']['prev'] else None
    context = {
        'characters': characters['results'],
        'current_page': page,  # Текущая страница
        'next_page': next_page,  # Следующая страница
        'previous_page': previous_page  # Предыдущая страница
    }
    return render(request, 'index.html', context=context)

def detail(request, id):
    character = get_character_by_id(id)
    context = {
        'character': character
    }
    return render(request, 'detail.html', context=context)