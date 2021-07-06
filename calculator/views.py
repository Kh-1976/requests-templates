from django.shortcuts import render, reverse
from django.http import HttpResponse
from datetime import datetime


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet_view(request):
    template_name = 'calculator/index.html'
    servings = request.GET.get('servings', 1)
    context = {
            'recipe': {
                'яйца, шт': 2 * int(servings),
                'молоко, л': 0.1 * int(servings),
                'соль, ч.л.': 0.5 * int(servings)
            }
    }
    return render(request, template_name, context)


def pasta_view(request):
    template_name = 'calculator/index.html'
    servings = request.GET.get('servings', 1)
    context = {
            'recipe': {
                'макароны, г': 0.3 * int(servings),
                'сыр, г': 0.05 * int(servings)
            }
    }
    return render(request, template_name, context)


def buter_view(request):
    template_name = 'calculator/index.html'
    servings = request.GET.get('servings', 1)
    context = {
            'recipe': {
                'хлеб, ломтик': 1 * int(servings),
                'колбаса, ломтик': 1 * int(servings),
                'сыр, ломтик': 1 * int(servings),
                'помидор, ломтик': 1 * int(servings)
            }
    }

    return render(request, template_name, context)


def none_view(request):
    template_name = 'calculator/index.html'
    context = {
        'recipe': {
        }
        }
    return render(request, template_name, context)