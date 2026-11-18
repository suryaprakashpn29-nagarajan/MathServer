from django.shortcuts import render
def Churn_rate(request):
    ic= float(request.POST.get('InitCust', '0'))
    cl= float(request.POST.get('CustLost', '0'))
    churn_rate = ((ic-cl)*100)/ic if request.method == 'POST' and ic != 0 else 0
    print("Customers Lost Count =",cl)
    print("Initial Customers Count =",ic)
    print("Churn Rate =",churn_rate)
    return render(request, 'churnapp/math.html',{'ic': ic, 'cl': cl, 'churn_rate': churn_rate})
