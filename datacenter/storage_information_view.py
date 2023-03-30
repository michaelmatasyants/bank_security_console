from django.utils.timezone import localtime
from django.shortcuts import render
from datacenter.models import Visit, format_duration


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        loacal_entered_at = localtime(visit.entered_at).strftime(
            '%d %B %Y %H:%M')
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': loacal_entered_at,
                'duration': format_duration(visit.get_duration()),
             },
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
