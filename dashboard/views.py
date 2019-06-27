from django.shortcuts import render

# Create your views here.
from django.views import View

from dashboard.forms import DashboardQueryForm

def get(request):
    data = [['05 - 01',703, 1900, 0],
            ['05 - 02',1473,1900, 0],
            ['05 - 03',863,1900, 1],
            ['05 - 04',1494,1900, 1],
            ['05 - 05',965,1900, 1],
            ['05 - 06',568,1900, 1],
            ['05 - 07',189, 1900, 1],
            ['05 - 08',464, 1900, 1],
            ['05 - 09',731, 1900, 0],
            ['05 - 10',306, 1900, 0],
            ['05 - 11',899, 1900, 0],
            ['05 - 12',231, 1900, 0],
            ['05 - 13',262, 1900, 0],
            ['05 - 14',429, 1900, 0],
            ['05 - 15',322, 1900, 0],
            ['05 - 16',315, 1900, 0],
            ['05 - 17',228, 1900, 0],
            ['05 - 18',436, 1900, 0],
            ['05 - 19',287, 1900, 0],
            ['05 - 20',419,1900, 0],
            ['05 - 21',296,1900, 0],
            ['05 - 22',343,1900, 0]]
    context = {
        'pepega' : data
#         'company_name': company_name,
#         # 'from_date': from_date,
#         # 'to_date': to_date,
    }
    return render(request, 'nalika/index.html', context)
    return render(request, 'nalika/index.html')

# def post(request):
#     form = DashboardQueryForm
#     company_name = request.POST['company_name']
#     # from_date = request.POST['from_date']
#     # to_date = request.POST['to_date']
#     context = {
#         'company_name': company_name,
#         # 'from_date': from_date,
#         # 'to_date': to_date,
#     }
#     return render(request, 'dashboardFinal.html', {'form': form}, context)

def doomed(request):
    company = request.POST.get('company')
    daydd1 = request.POST.get('daydd1')
    month1 = request.POST.get('month1')
    daydd2 = request.POST.get('daydd2')
    month2 = request.POST.get('month2')
    data = [['05 - 01',703, 1900]]
    context = {
        'pepega' : data
#         'company_name': company_name,
#         # 'from_date': from_date,
#         # 'to_date': to_date,
    }
    return render(request, 'nalika/index.html', context)