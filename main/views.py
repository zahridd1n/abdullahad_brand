from django.shortcuts import render
from . import models


def index(request):
    headers = models.Header.objects.filter()
    services = models.Service.objects.all()
    banner = models.Banner.objects.last()
    skills_title = models.SkillsTitle.objects.last()
    skills = models.Skills.objects.all()
    works_progress = models.WorkProgress.objects.filter()[:4]
    portfolio = models.Portfolio.objects.filter()[:6]
    team = models.Team.objects.filter()[:3]
    testimonials = models.Testimonial.objects.all()
    blogs = models.Blog.objects.all()
    company_data = models.CompanyData.objects.last()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        message = request.POST.get('message')
        models.Contact.objects.create(name=name, email=email, message=message, company=company, phone=phone)
    context = {
        'headers': headers,
        'services': services,
        'banner': banner,
        'skills_title': skills_title,
        'skills': skills,
        'works_progress': works_progress,
        'portfolio': portfolio,
        'team': team,
        'testimonials': testimonials,
        'blogs': blogs,
        'company_data': company_data,
    }
    return render(request, 'index.html', context=context)
