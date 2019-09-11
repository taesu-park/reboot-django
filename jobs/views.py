from django.shortcuts import render
from decouple import config
from .models import PastLife
from faker import Faker
import requests
# from faker import Faker
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')

def result(request):
    name = request.GET.get('name')
    # DB에 이름이 있으면,
    past_life = PastLife.objects.filter(name=name).first()
    if not past_life:
        # 이름이 없으면,
        fake = Faker('ko_KR')
        job = fake.job()
        past_life = PastLife.objects.create(name=name, job=job)
    # 직업 결과에 따라, giphy 요청
    job = past_life.job

    api_key = config('GIPHY_API_KEY')
    # 1. url 설정
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=ko'

    # 2. 요청 보내기
    response = requests.get(url).json()
    # 3. 응답 결과에서 이미지 url 뽑기
    try:
        image_url = response['data'][0].get('images').get('original').get('url')
    except:
        image_url = None
    context = {
        'past_life':past_life,
        'image_url':image_url
    }
    return render(request, 'jobs/result.html', context)
    