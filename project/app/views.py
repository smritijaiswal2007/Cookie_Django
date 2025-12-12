from django.shortcuts import render

# Create your views here.
def landing(req):
    return render('req','landing.html')
def set1(req):
    return render(req,'landing.html',{'set1':'set1'})
def set_data(req):
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        p=req.POST.get('password')
        print(n,e,p)
        response = render(req,'landing.html',{'msg':'Cookies Set Successfully'})
        response.set_cookie('name',n,max_age=60*5)
        response.set_cookie('email',e)
        response.set_cookie('password',p)
        return response

def get_data(req):
    print(req.COOKIES)
    n=req.COOKIES.get('name')
    e=req.COOKIES.get('email')
    p=req.COOKIES.get('password')
    data={
        'name':n,
        'email':e,
        'password':p
    }
    return render (req,'landing.html',{'data':data})
def delete_data(req):
    if req.COOKIES:
        response = render(req,'landing.html',{'msg':'Cookie Data Deleted '})
        response.delete_cookie('name')
        response.delete_cookie('email')
        if req.COOKIES.get('password'):
            response.delete_cookie('password')
        return response
    else:
        msg = "Dont Have Cookies "
        return render (req,'landing.html',{'msg':msg})
        

