from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    words = text.split()
    words_dic = {}

    for word in words:
        if word in words_dic.keys():
            # Increase word count
            words_dic[word] += 1

        else:
            # Add to dictionary
            words_dic[word] = 1

    return render(request, 'result.html', {
        'full': text,
        'total': len(words),
        dictionary': words_dic.items(),
    })
