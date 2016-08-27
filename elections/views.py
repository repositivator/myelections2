from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate, Poll, Choice
import datetime


def index(request):
    candidates = Candidate.objects.all()
    # str = ''
    # for candidate in candidates:
    #     str += "<p>{}기호 {}번({})<br>".format(candidate.name, candidate.party_number, candidate.area)
    #     str += candidate.introduction+"</p>"
    # return HttpResponse(str)

    context = {"candidates":candidates}

    return render(request, 'elections/index.html', context)


def area(request, area):
    today = datetime.datetime.now()

    try:
        poll = Poll.objects.get(area=area, start_date__lte=today, end_date__gte=today)
        candidates = Candidate.objects.filter(area=area)
    except Exception:
        poll = None
        candidates = None

    context = {"candidates":candidates, "area":area, "poll":poll}

    return render(request, 'elections/area.html', context)


def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    selection = request.POST['choice']

    try:
        choice = Choice.objects.get(poll_id=poll_id, candidate_id=selection)
        choice.votes += 1
        chocie.save()
    except Exception:
        choice = Choice(poll_id = poll_id, candidate_id=selection, vote = 1)
        choice.save()

    return HttpResponse("finish")

















