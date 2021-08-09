from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/')
def index():
    return 'Hello Dear, lets explore Central Asia'

@app.get('/countries')
def index ():
    return 'Qazaqstan','Ozbekiston','Kyrgyzstan','Turkmenistan','Tadjikistan'

@app.get('/countries/{country}')
def countries(country):
    db_data = {
    'qazaqstan': {
        'Capital': 'Nur-Sultan',
        'population':'18.51 mln',
        'Traditional food':'Beshbarmak,Baursak,Kuyrdak',
        'Traditional drinks': "Kumys, Kozhe, Shubat"
    },
    'ozbekiston':{
       'Capital': 'Toshkent',
       'population':'34.860 mln',
       'Traditional food':'Plov',
       'Traditional drinks': "Special green tea" 
    },
    'kyrgyzstan':{
       'Capital': 'Bishkek',
       'population':'6.637 mln',
       'Traditional food':'Beshbarmak, Chuchvara, Samsa',
       'Traditional drinks': "Maksym Shoro, Chalap Shoro, Jarma Shoro" 
    },
    'turkmenistan':{
       'Capital': 'Ashkhabad',
       'population':'6.108 mln',
       'Traditional food':'Keidjerken kebab, dograma, borek',
       'Traditional drinks': "Gok chai, gara chai" 
    },
    'tadjikistan':{
       'Capital': 'Dushanbe',
       'population':'9.321 mln',
       'Traditional food':'Plov, Kurutob,Kabob, Siyelaf',
       'Traditional drinks': "Green tea"}
}
    if country in db_data:
        result =  db_data [country]
    else:
        result = 'This country is not belong to Central Asia region'
    return result
 
@app.get('/countries/{country}/quote')
def quote(country):
        url = 'https://api.quotable.io/random'
        response = requests.get(url).json()
        result = 'If I would live in %s then my quote would be: %s' % (country, response ['content'])
        return result        

