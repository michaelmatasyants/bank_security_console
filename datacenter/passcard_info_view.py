from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime
from django.shortcuts import render
from datacenter.models import Passcard, Visit, format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for passcard_visit in Visit.objects.filter(passcard=passcard):
        loacal_entered_at = localtime(passcard_visit.entered_at).strftime(
            '%d %B %Y %H:%M')
        this_passcard_visits.append(
            {
                'entered_at': loacal_entered_at,
                'duration': format_duration(passcard_visit.get_duration()),
                'is_strange': passcard_visit.is_long()
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
