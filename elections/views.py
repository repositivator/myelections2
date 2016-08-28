from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
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
        print("checked update")
        choice.votes += 1
        choice.save()
    except Exception:
        choice = Choice(poll_id = poll_id, candidate_id=selection, votes = 1)
        print("checked new one")
        choice.save()

    return HttpResponseRedirect("/areas/{}/results".format(poll.area))


def results(request, area):
    candidates = Candidate.objects.filter(area=area)

    polls = Poll.objects.filter(area=area)
    poll_results = []

    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date

        total_votes = Choice.objects.filter(poll_id=poll.id).aggregate(Sum('votes'))
        result['total_votes'] = total_votes['votes__sum']

        rates = []
        for candidate in candidates:
            try:
                choice = Choice.objects.get(poll_id = poll.id, candidate_id=candidate.id)
                rates.append(round(choice.votes*100/result['total_votes'],1))
            except Exception:
                rates.append(0)
        result['rates'] = rates

        poll_results.append(result)

    context = {'candidates':candidates, 'area':area, 'poll_results':poll_results}

    return render(request, 'elections/result.html', context)















