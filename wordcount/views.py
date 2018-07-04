from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')     #django searches for second argument in render method from the directory list in settings file

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    wordCount = len(wordList)
    wordDictionary = {}
    #convert to list

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] = wordDictionary[word] + 1
        else:
            wordDictionary[word] = 1

    sortedwords=sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)   #key is what is being sorted in the given list

    return render(request, 'count.html',{'fulltext':fulltext,'wordCount':wordCount,'sortedwords':sortedwords}) 

def about(request):
    return render(request, 'about.html')

