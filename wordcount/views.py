from django.shortcuts import render

def index(request):
    return render(request, 'wordcount/index.html')

def result(request):
    word_amount = len(list(filter(None, request.POST['text'].strip().split(' '))))
    if word_amount == 0:
        return render(request, 'wordcount/error.html')    

    context = {'word_amount' : word_amount}
    return render(request, 'wordcount/result.html', context)
