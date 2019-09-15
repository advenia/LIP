from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from polls.models import PointOfInterest
from django.views.decorators.csrf import csrf_exempt
import numpy
import subprocess


def index(req):
    return HttpResponse("Nothing here")


def tripform(req):
    return render(req, 'polls/tripupload.html')


# @csrf_exempt
# def tripupload(req):
#     _ = PointVisit(
#         point_of_interest=sorted(
#             PointOfInterest.objects.all(),
#             key=lambda a: a.get_distance(numpy.array([float(req.POST['latitude']), float(req.POST['longitude'])]))
#         )[0],
#         start_time=req.POST['start_time'],
#         end_time=req.POST['end_time']
#     )
#     _.save()
#     return HttpResponse("BAF")


def download(req):
    """
    Cool GET request stuff:
    latitude
    longitude
    count (number of points of interest)
    radius (the radius in which to look for points)"""
    def point_of_interest_to_dict(poi):
        d = poi.__dict__
        d.pop('_state')
        return d
    pos = numpy.array([float(req.GET['latitude']), float(req.GET['longitude'])])
    poi_list = sorted(PointOfInterest.objects.all(), key=lambda a: a.get_si_distance(pos))[:int(req.GET['count'])]
    return JsonResponse({
        'points-of-interest': list(map(point_of_interest_to_dict, [p for p in poi_list if p.get_si_distance(pos) < int(req.GET['radius'])]))
    }, safe=False)


@csrf_exempt
def addpoint(req):
    _ = PointOfInterest(
        latitude=req.POST['latitude'],
        longitude=req.POST['longitude'],
        name=req.POST['name'],
        address=req.POST['address']
    )
    _.save()
    return HttpResponse("added point")


def gitpullonlythanks(req):
    subprocess.run(['git', 'pull'], cwd=r'/root/LIP/')
    return HttpResponse('pulled my git')
