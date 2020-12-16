import collections
import json
from django.http import HttpResponse
import cursor as cursor
from django.db.backends import mysql
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from pluginServer.models import Time

def plugin_list(request):
    times = Time()
    time = Time.objects.all()
    listx = []
    listy = []
    listForCircle = []
    count = 0
    for rm in time:
        if(count<rm.id):
            count = rm.id
        print(count)
    for hs in time:
        if count ==rm.id:
            times = hs
            print(hs.go)

    ti =times
    if ti.c != 0:
        listx.append("c")
        listForCircle.append(eval("{'name':\"c\",'y':"+str(ti.c/ti.total*100)+"}"))
    if ti.cpp != 0:
        listx.append("cpp")
        listForCircle.append(eval("{'name':\"cpp\",'y':"+str(ti.cpp/ti.total*100)+"}"))

    if ti.go != 0:
        listx.append("go")
        listForCircle.append(eval("{'name':\"go\",'y':"+str(ti.go/ti.total*100)+"}"))

    if ti.hs != 0:
        listx.append("haskell")
        listForCircle.append(eval("{'name':\"haskell\",'y':"+str(ti.hs/ti.total*100)+"}"))

    if ti.java != 0:
        listx.append("java")
        listForCircle.append(eval("{'name':\"java\",'y':"+str(ti.java/ti.total*100)+"}"))

    if ti.js != 0:
        listx.append("js")
        listForCircle.append(eval("{'name':\"js\",'y':"+str(ti.js/ti.total*100)+"}"))

    if ti.kt != 0:
        listx.append("kotlin")
        listForCircle.append(eval("{'name':\"kotlin\",'y':"+str(ti.kt/ti.total*100)+"}"))

    if ti.other != 0:
        listx.append("other")
        listForCircle.append(eval("{'name':\"other\",'y':"+str(ti.other/ti.total*100)+"}"))

    if ti.rs != 0:
        listx.append("rust")
        listForCircle.append(eval("{'name':\"rust\",'y':"+str(ti.rs/ti.total*100)+"}"))

    if ti.py != 0:
        listx.append("python")
        listForCircle.append(eval("{'name':\"python\",'y':"+str(ti.py/ti.total*100)+"}"))

    if ti.total != 0:
        listx.append("total")

    if ti.c != 0:
        listy.append(float(str(ti.c)))
    if ti.cpp != 0:
        listy.append(float(str(ti.cpp)))
    if ti.go != 0:
        listy.append(float(str(ti.go)))
    if ti.hs != 0:
        listy.append(float(str(ti.hs)))
    if ti.java != 0:
        listy.append(float(str(ti.java)))
    if ti.js != 0:
        listy.append(float(str(ti.js)))
    if ti.kt != 0:
        listy.append(float(str(ti.kt)))
    if ti.other != 0:
        listy.append(float(str(ti.other)))
    if ti.rs != 0:
        listy.append(float(str(ti.rs)))
    if ti.py != 0:
        listy.append(float(str(ti.py)))
    if ti.total != 0:
        listy.append(float(str(ti.total)))

    return render(request, 'dashboard_with_pivot.html', {'Time': ti, 'X': listx, 'Y': listy,'Z':listForCircle})
