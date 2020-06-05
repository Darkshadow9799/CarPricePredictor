from django.shortcuts import render,redirect
import pickle
import pandas as pd
# Create your views here.
dummy_csv=list(pd.read_csv('car_pred/dummy_cvs.csv'))
model_t = dummy_csv[2:-4]
fuel_t = dummy_csv[-4:]
def predictor(request):
    if request.method=="POST":
        milage=int(request.POST['milage'])
        year=int(request.POST['year'])
        model=request.POST['model']
        fuel=request.POST['fuel']
        input_val=[]
        input_val.append(milage)
        input_val.append(year)
        for i in dummy_csv[2:-4]:
            if model==i:
                input_val.append(1)
            else:
                input_val.append(0)
        for i in dummy_csv[-4:]:
            if fuel==i:
                input_val.append(1)
            else:
                input_val.append(0)
        final_input=[]
        final_input.append(input_val)
        reg=pickle.load(open('car_pred/model_lin_reg.sav','rb'))
        result=reg.predict(final_input)
        return render(request,'result.html',{'result':result,})
    else:
        return render(request,'home.html',{
            'model':model_t,
            'fuel':fuel_t,
        })

def back(request):
    return render(request, 'home.html', {
        'model': model_t,
        'fuel': fuel_t,
    })