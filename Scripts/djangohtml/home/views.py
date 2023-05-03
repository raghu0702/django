from django.shortcuts import render, redirect
import pandas as pd;
import json
from roboflow import Roboflow
from django.shortcuts import render
#from .models import UploadedImage
#from .forms import ImageUploadForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

def fruitsTable(request):
    df = pd.read_excel("C:/Users/raghu/Downloads/Fruits.xlsx")
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'fruits.html', context)

def vegTable(request):
    df = pd.read_excel("C:/Users/raghu/Downloads/Vegetables.xlsx")
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'veg.html', context)

def medicTable(request):
    df = pd.read_excel("C:/Users/raghu/Downloads/Medicinal_new.xlsx")
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'medic.html', context)

def cerealTable(request):
    df = pd.read_excel("C:/Users/raghu/Downloads/Cereals.xlsx")
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'cereals.html', context)


def predictions(request):
    rf = Roboflow(api_key="dCtQn80N56V8fZxHLgPv")
    project = rf.workspace().project("sem-ii-v2-1")
    model = project.version(1).model
    # infer on a local image
    print(model.predict("your_image.jpg").json())
    model.predict("your_image.jpg").save("prediction.jpg")