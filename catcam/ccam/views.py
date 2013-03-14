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
    return render(request, 'base.html',
                             {'pos':pos, 'length':length})

def stay_alive(request):
    global t
    global queue
    global counter
    res = {'pos':-1, 'length':-1}
    if request.session and 'place' in request.session.keys() and request.session['place'] in queue:
        if len(queue) > 0 and request.session['place'] == queue[0]:
            t = time.time()
    else:
        request.session['place'] = counter
        queue.append(counter)
        counter += 1
    res['pos'] = queue.index(request.session['place']) + 1
    res['length'] = len(queue)
    print '{} in {} time {}'.format(request.session['place'], queue, t)
    if time.time() - t > 10:
        if len(queue) > 1:
            queue.pop(0)
    return HttpResponse(simplejson.dumps(res), mimetype='application/json')

def move(direction):
    print direction

def left(request):
    if request.session and 'place' in request.session.keys() and len(queue) > 0 and request.session['place'] == queue[0]:
        move('left')
    return HttpResponse('k')

def right(request):
    if request.session and 'place' in request.session.keys() and len(queue) > 0 and request.session['place'] == queue[0]:
        move('right')
    return HttpResponse('k')
