import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import SaveMoney


thisPage=0
def index(request):
    return render(request, 'savemoney/index.html')

def detail(request, page=1):
    latest_detail_list = SaveMoney.objects.order_by('-dateTime')[(int(page)-1)*5:int(page)*5]
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


def saveDatailtoModel(request):
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


def downloadCSVFile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="detailALl.csv"'

    writer = csv.writer(response)
    all_detail_list = SaveMoney.objects.order_by('dateTime')[:]
    for index in  all_detail_list:
        writer.writerow([index.dateTime, index.detail, index.money])
    return response

def saveCSVFile(request):
    if request.method == 'POST' and request.FILES["csvFile"]:
        csvFile = request.FILES["csvFile"].read()
        SaveMoney.objects.all().delete()

        csvData = str(csvFile)
        first=2
        end = csvData.find(',')
        while end>0 and first>0:
            dateTime = csvData[first:end]
            first = end + 1
            end = csvData.find(',', first)

            detail = csvData[first:end]
            first = end + 1
            end = csvData.find('r', first) - 1

            money = int(csvData[first:end])
            first = end + 4
            end = csvData.find(',', first)
            saveData(detail, money, dateTime)

    return HttpResponseRedirect(reverse('SaveMoney:detail', args=('1')))

def saveData(detail,money,dateTime):
    saveData = SaveMoney(detail=detail, money=money, dateTime=dateTime)
    saveData.save()
    return 0

