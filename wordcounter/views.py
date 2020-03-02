from django.shortcuts import render
from django.http import HttpRequest

def home(request: HttpRequest):
    return render(request, 'home.html')

def about(request: HttpRequest):
    return render(request, 'about.html')

def count(request: HttpRequest):
    full_text = request.GET['full_text']
    splitted_words = full_text.split()
    words_counted = len(splitted_words)

    repeated_words = _get_words_with_repetition(splitted_words)

    return render(request, 'count.html', {
        'full_text': full_text,
        'splitted_words': splitted_words,
        'words_counted': words_counted,
        'repeated_words': repeated_words.items()
    })

def _get_words_with_repetition(splitted_words):
    word_dict = {}
    
    for word in splitted_words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict