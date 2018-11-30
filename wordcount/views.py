from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['fulltextarea']
    words=data.split()
    words_len=len(words)
    worddictionary={}
    for w in words:
        if w in worddictionary:
            worddictionary[w] += 1
        else:
            worddictionary[w] = 1
    sortedl=sorted(worddictionary.items(),key=operator.itemgetter(1))
    return render(request,'count.html',{'fulltext':data,'lwords':words_len,'worddict' : sortedl})
