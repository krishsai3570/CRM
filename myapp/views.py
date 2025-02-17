from django.shortcuts import render,redirect

from django.views import View

from myapp.forms import CustomerForm,SignInForm

from django.contrib.auth.forms import UserCreationForm

from myapp.models import Customer

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.mixins import LoginRequiredMixin



class CostumerView(LoginRequiredMixin,View):

    def get(self,request,*args,**kwrags):

        form_instance=CustomerForm()

        return render(request,"customer_add.html",{"form":form_instance})
    

    

    def post(self,request,*args,**kwrags):

        form_instance=CustomerForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            return redirect('list')
        
        return render(request,"customer_add.html",{"form":form_instance})
            
            


            

class CostumerListView(LoginRequiredMixin,View):

    def get(self,request,*args,**kwrags):

        qs=Customer.objects.all()

        return render(request,"customer_list.html",{"data":qs})              


    


class CostumerDetailView(LoginRequiredMixin,View):

    def get(self,request,*args,**kwrags):

        id=kwrags.get("pk")

        qs=Customer.objects.get(id=id)

        return render(request,"customer_detail.html",{"data":qs})
    


def dashboard(request):

    if not request.user.is_authenticated:

        return redirect("signin")

     
    total_customers = Customer.objects.count()  

    recent_customer = Customer.objects.last()  
    
    return render(request, 'dashboard.html', {
        
        'total_customers': total_customers,
        'recent_customers': recent_customer
    })





class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=UserCreationForm()

        return render(request,"signup.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=UserCreationForm(request.POST)

        if form_instance.is_valid():
           

            user=form_instance.save()

            login(request,user)

            return redirect("signin")
        
        return render(request,"signup.html",{"form":form_instance})

        




class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignInForm()

        return render(request,"signin.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=SignInForm(request.POST)

        if form_instance.is_valid():

            username=form_instance.cleaned_data.get("username")
            password=form_instance.cleaned_data.get("password")

            user_obj=authenticate(request,username=username,password=password)

            if user_obj:
                login(request,user_obj)


                return redirect("dashboard")
            
            return render(request,"signin.html",{"form":form_instance})




class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)    

        return redirect("signin")    




class CustomerUpdateView(LoginRequiredMixin,View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Customer.objects.get(id=id)

        form_instane=CustomerForm(instance=qs)

        return render(request,"customer_update.html",{"form":form_instane})



    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        form_instance=CustomerForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Customer.objects.filter(id=id).update(**data)

            return redirect("list")
        


class CustomerDeleteView(LoginRequiredMixin,View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        
        Customer.objects.get(id=id).delete()

        return redirect("list")






        