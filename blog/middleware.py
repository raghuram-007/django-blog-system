from django.urls import reverse
from django.shortcuts import redirect

class RedirectAuthenticatedUser:
    def __init__(self,get_response):
        self.get_response=get_response
        
    
    def __call__(self,request):
        if request.user.is_authenticated:
            path_to_redirect=[reverse('blog:login'),reverse('blog:sign')]
            
            if request.path in path_to_redirect:
                return redirect(reverse('blog:dashboard'))
            
        response=self.get_response(request)
        return response
        
        