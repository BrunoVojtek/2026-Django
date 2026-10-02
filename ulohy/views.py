from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse('<h1>Ahoj</h1>')

def o_mne(request):
    kontext = {
        'meno':'Bruno',
        'vek':17,
        'zaluby':['programovanie', 'hudba', 'pivo']
    }
    return render(request,'ulohy/o_mne.html',kontext)