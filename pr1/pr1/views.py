from django.http import HttpResponse
from django.shortcuts import render




def index1(request):
    return render(request,'index1.html')


def removepunc(request):
    djtext=request.POST.get('text1','default')
    ch=request.POST.get('remove','off')
    fullcap=request.POST.get('upper','off')
    newLineRemover=request.POST.get('newLineRemover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    punc='''!@#$%^&*()_<>?:;'"[]{\}/~`,.'''
   
    pun=[]
    
    if ch=='on':
        analyze=''
        for i in djtext:
            if i not in punc:
                analyze=analyze+i
        pun.append('Remove Puncuation')
        params={'Purpose':' - '.join(pun),'analyzed_text':analyze}
        djtext=analyze
           
    if fullcap=='on':
        analyze=''
        
        for i in djtext:
            analyze=analyze+i.upper()
        pun.append('Uppercase')
        params={'Purpose':' - '.join(pun),'analyzed_text':analyze}
        djtext=analyze

         
    if newLineRemover=='on':
        analyze=''
       
        for i in djtext :
                if i!='\n' and i!='\r':
                    analyze=analyze+i
                else:
                    pass
        pun.append('New Line Remover')
        params={'Purpose':' - '.join(pun),'analyzed_text':analyze}
        djtext=analyze

            
    if extraspaceremover=='on':
        analyze=''
           
        for index,i in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyze=analyze+i
        pun.append('Extra Space Remover')
        params={'Purpose':' - '.join(pun),'analyzed_text':analyze}
        
    if (ch!='on' and fullcap!='on' and newLineRemover!='on' and extraspaceremover!='on'):
        return HttpResponse('Error')
    
    return render(request,'index2.html',params)
