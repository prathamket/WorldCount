from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
    #{'obj':'This is python object value we are showing throught html'})

    #return HttpResponse('Hello')

def count(request):
    fulltext = request.GET['fulltext']

    word_dic ={}
    wordlist = fulltext.split()


    for word in wordlist:
        if word in word_dic:
            word_dic[word] +=1
        else:
            word_dic[word] = 1

    sorted_word = sorted(word_dic.items(),key=operator.itemgetter(1),reverse=True)
    #print(fulltext)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sorted_word':sorted_word})

def about(request):
    return render(request,'about.html')


def prathamdef(request):
    return HttpResponse("<h1>This is my first django project</h1>")