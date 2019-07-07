import pyrebase
from django.shortcuts import render
from collections import OrderedDict

config = {
    'apiKey': "AIzaSyDWhUaHDhdC6R7J-rlddFaxqPjcGEqrENM",
    'authDomain': "quicksearch-177.firebaseapp.com",
    'databaseURL': "https://quicksearch-177.firebaseio.com",
    'projectId': "quicksearch-177",
    'storageBucket': "quicksearch-177.appspot.com",
    'messagingSenderId': "637425734410"
  };

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

database=firebase.database()

def firebase(request):

    """idtoken = request.session['uid']
    a = auth.get_account_info(idtoken)
    a = a['user/links']
    a = a[0]
    a = a['localId']"""

    uname = request.user.username
    data = database.child('user').child('links').get().val()
    data_l = list(data.items())

    data_list = []
    for x in data_l:
        d = {
            'pageId':x[1]['pageId'],
            'username': x[1]['useName']
        }
        if d['username']  == uname:
            data_list.append(d)


    context = {
        'data_list': data_list
    }

    return render(request,'recent.html',context)

