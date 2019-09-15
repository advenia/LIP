from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from polls.models import PointOfInterest, PointVisit, GoogleLandmark
import numpy


def index(req):
    return HttpResponse("Nothing here")


def tripform(req):
    return render(req, 'polls/tripupload.html')


def tripupload(req):
    _ = PointVisit(
        point_of_interest=sorted(
            PointOfInterest.objects.all(),
            key=lambda a: a.get_distance(numpy.array([float(req.POST['x']), float(req.POST['y'])]))
        )[0],
        start_time=req.POST['start_time'],
        end_time=req.POST['end_time']
    )
    _.save()
    return HttpResponse("BAF")


# /polls/download?x=-41&y=-43&count=10
def download(req):
    def point_of_interest_to_dict(poi):
        d = poi.__dict__
        d.pop('_state')
        return d
    poi_list = sorted(PointOfInterest.objects.all(), key=lambda a: a.get_distance(numpy.array([float(req.GET['x']), float(req.GET['y'])])))[:int(req.GET['count'])]
    return JsonResponse({
        'points-of-interest': list(map(point_of_interest_to_dict, poi_list))
    }, safe=False)


def googledata(req):
    _ = GoogleLandmark(
        lat=float(req.POST['lat']),
        lng=float(req.POST['lng']),
        icon=req.POST['icon'],
        _id=req.POST['id'],
        name=req.POST['name'],
        place=req.POST['place'],
        reference=req.POST['reference'],
        types=req.POST['jsonstringtypes'],
        vicinity=req.POST['vicinity']
    )
    _.save()
    return HttpResponse()
