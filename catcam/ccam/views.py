from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
import time
# Create your views here.
queue = []
counter = 0
t = 0

def index(request):
    global queue
    global counter
    if 'place' in request.session.keys():
        if request.session['place'] not in queue:
            request.session['place'] = counter
            queue.append(counter)
            counter += 1
    else:
        request.session['place'] = counter
        queue.append(counter)
        counter += 1
    pos = queue.index(request.session['place']) + 1
    length = len(queue)
    return render(request, 'home.html',
                             {'pos':pos, 'length':length})

def stay_alive(request):
    global t
    res = {'pos':-1, 'length':-1}
    if 'place' in request.session.keys():
        if request.session['place'] == queue[0]:
            t = time.time()
        res['pos'] = queue.index(request.session['place']) + 1
        res['length'] = len(queue)
    if time.time() - t > 10:
        if len(queue) > 0:
            queue.pop(0)
    return HttpResponse(simplejson.dumps(res), mimetype='application/json')
