from django.shortcuts import render

from django.http import HttpResponse

def find_mode(request,listofnum):
    arr=listofnum.split(",")
    num_count=dict()
    for num in arr:
        num_count[num]=num_count.get(num,0)+1
    num_count=sorted(num_count.items(),key=lambda item:item[1])
    num_count.reverse()
    result="<p><span style=color:red>%s</span> appears <span style=background-color:yellow>%s</span> times" %(num_count[0][0],num_count[0][1])
    return HttpResponse(result)