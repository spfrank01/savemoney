from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from .models import SaveMoney

#IndexView(generic.DetailView):
#    model = SaveMoney
#    template_name = 'savemoney/index.html'

#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by('-pub_date')[:10]
    #context_object_name = 'latest_question_list'
#income, expenses
def index(request):
    return render(request, 'savemoney/index.html')

def detail(request):
    latest_detail_list = SaveMoney.objects.order_by('-dateTime')[:]
    context = {'latest_detail_list': latest_detail_list}
    return render(request, 'savemoney/showdetail.html', context)

#def saveValue(request):
#p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
	#data = SaveMoney.objects.create()	