# views.py
import calendar
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

def year_calendar(request):
    year = None
    months = []

    if request.method == "POST":
        year = int(request.POST.get("year"))

        # Tumia calendar module
        for month in range(1, 13):
            month_name = calendar.month_name[month]
            month_days = calendar.monthcalendar(year, month)

            months.append({
                "name": month_name,
                "days": month_days
            })

    return render(request, "calender.html", {"months": months, "year": year})


@api_view(["GET"])
def api_calendar(request, year):
    year = int(year)
    months = []

    for month in range(1, 12 + 1):
        months.append({
            "month": calendar.month_name[month],
            "weeks": calendar.monthcalendar(year, month)
        })

    return Response({
        "year": year,
        "calendar": months
    })
