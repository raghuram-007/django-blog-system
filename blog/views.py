from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from blog.models import Media,About,Category
from blog.forms import ContactForm, ForgetPassword, Postform , RegisterForm, loginform
import logging
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core. paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.core.mail import EmailMessage  # type: ignore





logger=logging.getLogger("TESTING")

# Create your views here.
def intro(request):
    return HttpResponse(f'let begin the blog project...')
def value(request):
    password='Kings_007'
    return HttpResponse(f' welcome to project:{password}')
def id(request,id):
    return HttpResponse(f'successfully completed:{id}')
def user(request,user):
    return HttpResponse(f'welcome back:{user}')
def home(request):
   
    return redirect("intro")

@login_required
def post(request):
    query=request.GET.get('q')
    if query:
        
     host=Media.objects.filter(  Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(categer__name__icontains=query),is_publish=True)
    else:
        host=Media.objects.filter(is_publish=True)
    paginator=Paginator(host,7)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    return render(request,'folders/blog.html',{'page_obj':page_obj, 'hosts': host.exists(),'query':query  })


@login_required
def detail(request,slug):
   
    host=Media.objects.get(slug=slug)
    related_post=Media.objects.filter(categer=host.categer)
    
    
    return render(request,'folders/detail.html',{'hosts':host,'relate':related_post})


def index(request):
    return render(request,'folders/home.html')


def about(request):
 aboutss=About.objects.get()
 return render(request,'folders/about.html',{'abouts':aboutss})



@login_required
def contact(request):
    form=ContactForm()
    success=False
    if request.method=='POST':
         form=ContactForm(request.POST)
         
         if form.is_valid():
             logger=logging.getLogger("TESTING")
             logger.debug(f"{form.cleaned_data['name']} \n{form.cleaned_data['email']}\n {form.cleaned_data['message']}")
             success=True
         else:
             logger=logging.getLogger("TESTING")
             logger.debug('form invalid')
         return render(request,'folders/contact.html',{'form':form,'success':success})
    return render(request,'folders/contact.html')


def signup(request):
    form=RegisterForm()
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
         user=form.save(commit=False)
         user.set_password(form.cleaned_data['password'])
         user.is_staff = False 
         user.save()
         print("register success")
         messages.success(request,"registration are completed successfully ,Now log in..")
         return redirect('blog:login')
         
         
        else:
           messages.error(request,'not submitted')
           print("form error:", form.errors) 
        
        
    return render(request,'folders/signup.html',{'form':form})



def login(request):
    form = loginform()
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            print("login success")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            



            if user is not None:
                auth_login(request, user)
                # print("User is_staff:", user.is_staff)
                # print("User is_superuser:", user.is_superuser)

                # Role-based redirect
                if user.is_staff or user.is_superuser:
                    # print("Redirecting to admin panel...")
                    return redirect(reverse('admin:index'))  # Admin panel
                else:
                    print("Redirecting to user dashboard...")
                    return redirect('blog:dashboard')  # Normal user dashboard
            else:
                print("Invalid credentials")
                messages.error(request, "Invalid username or password")
        else:
            print("Form invalid:", form.errors)

    return render(request, 'folders/login.html', {'form': form})



def logout(request):
    auth_logout(request)
    return redirect('blog:login')



@login_required
def new_post(request):
    category=Category.objects.all()
    form=Postform()
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)   # ✅ Don't save to DB yet
            post.user = request.user         # ✅ Assign the logged-in user
            post.save()   
            post_url=request.build_absolute_uri(reverse('blog:detail',args=[post.slug]))
            subject=f'New Blog Posted:{post.title}'
            message=render_to_string("folders/new_post_email.html",{
                'user':request.user,
                'post':post,
                'post_url':post_url
            })
           
            email=EmailMessage(
                 subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                 to=[user.email for user in User.objects.filter(is_active=True)],  # send to all
                

            )
           
            email.content_subtype = "html"  # Important to send HTML email
            email.send(fail_silently=False)
            return redirect('blog:dashboard')
            
        
        
    return render(request,'folders/create_post.html',{'collec':category ,'form':form})


 
@login_required
def dashboard(request):
 
    
    
    all=Media.objects.filter(user=request.user)
    
  
    
    return render(request,'folders/dashboard.html',{'alls':all})



@login_required
def edit_post(request,post_id):
    form=Postform()
    category=Category.objects.all()
    post=get_object_or_404(Media,id=post_id)
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post was Updated successfully')
            return redirect('blog:dashboard')
           
       
        else:
            messages.error(request,"you are in wrong way")
        
    return render(request,'folders/edit_post.html',{'collec':category,'post':post,'form':form})


@login_required
def delete_post(request,post_id):
    post=get_object_or_404(Media,id=post_id)
    post.delete()
    messages.success(request,'post delete successfully'.title())
    return redirect('blog:dashboard')


@login_required
def publish_post(request,post_id):
    post=get_object_or_404(Media,id=post_id)
    post.is_publish=True
    post.save()
    messages.success(request,"pubished successfully..!")
    return redirect('blog:dashboard')
    
    
    


def forget_password(request):
    form = ForgetPassword()
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "No account found with that email.")
            return redirect("blog:forget")

        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(request).domain

        subject = "Reset your password"
        message = render_to_string("folders/reset_email.html", {
            "domain": domain,
            "uidb64": uidb64,
            "token": token,
            "user": user,
        })

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        messages.success(request, "Password reset link sent to your email.")
        return redirect("blog:forget")  # Don't redirect to reset page directly

    return render(request, 'folders/forget_password.html', {'form': form})



def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password == confirm_password:
                user.set_password(password)
                user.save()
                messages.success(request, "Password successfully reset.")
                return redirect("blog:login")
            else:
                messages.error(request, "Passwords do not match.")

        return render(request, "folders/resetPassword.html")
    else:
        messages.error(request, "Invalid or expired link.")
        return redirect("blog:forget")