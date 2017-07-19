from django.shortcuts import render,redirect,HttpResponse
from myPolls.models import Video, Ticket
from django.template import context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from myPolls.form import LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def listing(request, cate=None):
    # print(cate)
    context = {}
    video_lists = Video.objects.all()
    if cate is None:
        print('*' * 10)
        video_lists = Video.objects.all()
    if cate == 'editors':
        print(cate)
        print('*' * 50)
        video_lists = Video.objects.filter(editors_choice=True)
    elif cate =='all':
        print('*' * 100)
        print(cate)
        video_lists = Video.objects.all()
    paginator = Paginator(video_lists,9)
    page = request.GET.get('page')
    try:
        video_list = paginator.page(page)
    except PageNotAnInteger:
        video_list = paginator.page(1)
    except EmptyPage:
        video_list = paginator.page(paginator.num_pages)
    context['video_list'] = video_list
    return render(request,'listing.html',context)

def detail(request, id):
    context  = {}
    video_info = Video.objects.get(id=id)
    voter_id = request.user.profile.id
    like_count = Ticket.objects.filter(choice='like', video_id=id).count()
    try:
        user_ticket = Ticket.objects.get(voter_id=voter_id, video_id=id)
        context['user_ticket'] = user_ticket
        context['like_count'] = like_count
    except:
        pass
    context['video_info'] = video_info
    return render(request, 'detail.html', context)


def detail_vote(request, id):
    voter_id = request.user.profile.id
    try:
        user_ticket = Ticket.objects.get(voter_id=voter_id, video_id=id)
        user_ticket.choice = request.POST['vote']
        user_ticket.save()
    except ObjectDoesNotExist:
        new_ticket= Ticket(voter_id=voter_id, video_id=id, choice=request.POST['vote'])
        new_ticket.save()
    return redirect(to='detail', id=id)





def login_index(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='list')
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(username=username,password=password)
            # if user:
            #     login(request, user)
            #     return redirect(to='list')
            # else:
            #     return HttpResponse('<h1>NOT A  User</h1>')
    context['form'] = form
    return render(request, 'register_login.html', context)

def register_index(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # login(request, form.get_user)
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request, 'register_login.html', context)


# def listing_editors(request, cate):
#
#     context = {}
#     # if cate is None:
#     #     video_lists = Video.objects.all()
#     if cate == 'editors':
#         video_lists = Video.objects.filter(editors_choice=True)
#     else:
#         video_lists = Video.objects.all()
#     print(cate)
#     print('*' * 20)
#     paginator = Paginator(video_lists,9)
#     page = request.GET.get('page')
#     try:
#         video_list = paginator.page(page)
#     except PageNotAnInteger:
#         video_list = paginator.page(1)
#     except EmptyPage:
#         video_list = paginator.page(paginator.num_pages)
#     context['video_list'] = video_list
#     return render(request,'listing.html',context)
