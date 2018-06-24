# exitban


install and activate virtualenv:
```
virtualenv -p python3 venv

. venv/bin/activate
```

install dependencies:
```
pip install -r requirements.txt
```

run code for 10 random National Code (default is 1):
```
python exitban.py -n 10
```

run code, using TOR:
```
python exitban.py -n 10 -t
```


Thanks to *Alireza Amouzadeh* for [National Code Gerator function](https://gist.github.com/Alireza2n/5708c361ca8417dec0f355d8eb51bc2b).