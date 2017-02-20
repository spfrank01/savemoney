from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.utils import timezone
from .models import SaveMoney

#IndexView(generic.DetailView):
#    model = SaveMoney
#    template_name = 'savemoney/index.html'

#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by('-pub_date')[:10]
    #context_object_name = 'latest_question_list'
#income, expenses
thisPage=0
def index(request):
    return render(request, 'savemoney/index.html')

def detail(request, page=1):
    latest_detail_list = SaveMoney.objects.order_by('-dateTime')[(int(page)-1)*5:int(page)*5]
    thisPage = page
    total=0
    count=0
    all_detail_list = SaveMoney.objects.order_by('-dateTime')[:]
    for i in  all_detail_list:
    	total += i.money
    	count += 1
    lastPage = int((count-1)/5+1)
    context = {'latest_detail_list': latest_detail_list, 
    			 	'total':total,
    			 	'page':int(page),
    			 	'lastPage':lastPage}
    return render(request, 'savemoney/showdetail.html', context)

#def saveValue(request):
#p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
	#data = SaveMoney.objects.create()	

def save(request):
	try:
		detail = request.POST['detail']
		money = request.POST['moneyValue']
		moneyType = request.POST['moneyType']
	except:
		detail = ""
		money = ""
		moneyType = ""
	else:
		if moneyType == "out":
			money = int(money)*(-1)
		saveData = SaveMoney(detail=detail, money=money, dateTime=timezone.now())
		saveData.save()
	return HttpResponseRedirect(reverse('SaveMoney:detail', args=('1')))

def olderPage(request, page):
	olderPage = str(int(page) +1)
	return HttpResponseRedirect(reverse('SaveMoney:detail', args=(olderPage)))

def newerPage(request, page):
	newerPage = str(int(page) -1)
	return HttpResponseRedirect(reverse('SaveMoney:detail', args=(newerPage)))