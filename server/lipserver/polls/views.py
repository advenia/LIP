from django.http import HttpResponse
from django.shortcuts import render
from polls.models import PointOfInterest, PointVisit
import numpy


def index(req):
    return HttpResponse("Nothing here")


def tripform(req):
    return render(req, 'polls/tripupload.html')


def tripupload(req):
    try:
        _ = PointVisit(
            point_of_interest=sorted(PointOfInterest.objects.all(), key=lambda a: a.get_distance(numpy.array([float(req.POST['x']), float(req.POST['y'])])))[0],
            start_time=req.POST['start_time'],
            end_time=req.POST['end_time']
        )
        print(_)
        _.save()
        return HttpResponse(_.__str__())
    except Exception as e:
        return HttpResponse(e.__str__())


def download(req):
    x, y = map(float, [req.GET['x'], req.GET['y']])
    return HttpResponse(str(x + y))
