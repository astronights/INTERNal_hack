from django.shortcuts import render

# Create your views here.
from django.views import View

from dashboard.forms import DashboardQueryForm


class dashboard(View):
    def get(self, request):
        form = DashboardQueryForm
        return render(request, 'dashboard.html', {'form': form})

    def post(self, request):
        form = DashboardQueryForm
        company_name = request.POST['company_name']
        # from_date = request.POST['from_date']
        # to_date = request.POST['to_date']
        context = {
            'company_name': company_name,
            # 'from_date': from_date,
            # 'to_date': to_date,
        }
        return render(request, 'dashboardFinal.html', {'form': form}, context)
