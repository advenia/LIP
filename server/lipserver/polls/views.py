from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from polls.models import PointOfInterest, PointUser
from django.views.decorators.csrf import csrf_exempt
from math import  max
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


@csrf_exempt
def userpoint(req):
    _ = PointUser(
        user=req.POST['user'],
        latitude=req.POST['latitude'],
        longitude=req.POST['longitude'],
        time=req.POST['time']
    )
    _.save()
    return HttpResponse("user baffed")


def download(req):
    """
    Cool GET request stuff:
    latitude
    longitude
    count (number of points of interest)
    radius (the radius in which to look for points)"""
    pos = numpy.array([float(req.GET['latitude']), float(req.GET['longitude'])])

    def point_of_interest_to_dict(poi):
        d = poi.__dict__
        d.pop('_state')
        return d

    def content_rating(poi):
        durations = [n.time - c.time for c, n in zip(PointUser.objects.all(), PointUser.objects.all()[1:])]
        a_duration = sum(durations) / max(len(durations))
        visits = sorted(PointUser.objects.all(), key=lambda a: a.time)
        a_visit = len(visits) / max(1, (visits[-1] - visits[0]).days)
        return a_duration * a_visit / max(1, poi.get_si_distance(pos))

    poi_list = sorted(PointOfInterest.objects.all(), key=content_rating, reverse=True)[:int(req.GET['count'])]
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
