from django.shortcuts import render
from datetime import date
from .models import Person

def index(request):
    age_years = age_months = age_days = None
    name = emoji = gender = ''
    birthday_today = False

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')

        if name and dob and gender:
            dob = date.fromisoformat(dob)
            today = date.today()
            birthday_today = (dob.day == today.day and dob.month == today.month)

            age_years = today.year - dob.year
            age_months = today.month - dob.month
            age_days = today.day - dob.day

            if age_days < 0:
                age_months -= 1
                prev_month = (today.month - 1) or 12
                age_days += 30  # Simplified

            if age_months < 0:
                age_years -= 1
                age_months += 12

            emoji = '👨' if gender == 'male' else '👩' if gender == 'female' else '🧑'

    return render(request, 'age_calculator/index.html', {
        'age_years': age_years,
        'age_months': age_months,
        'age_days': age_days,
        'name': name,
        'emoji': emoji,
        'gender': gender,
        'birthday_today': birthday_today
    })