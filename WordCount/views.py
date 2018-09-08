from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
     return render(request,'Home.html')

def count(request):
    FullText= request.GET['FullText']
    WordList=FullText.split()
    WordDictionary ={}
    for word in WordList:
        if word in WordDictionary:
            #Increase the number 
            WordDictionary[word]+=1
        else:
                #Add to Dictionary 
                 WordDictionary[word]=1
    SortedWords=sorted(WordDictionary.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'FullText':FullText,'Count':len(WordList),'SortedWords':SortedWords})
    

def about(request):
    return render(request,'about.html')
