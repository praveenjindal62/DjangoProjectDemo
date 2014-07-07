from django.shortcuts import render
from userReg.models import UserDetails
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm

class UserDetailsForm(ModelForm):
	class Meta:
		model=UserDetails
		fields=['fname','lname','uname','email','gender']

def NewUser(request):
	form=UserDetailsForm()
	return render(request,'form.html',{'form':form})
def GetDetail(request):
	if(request.method=='POST'):
		fname=request.POST['fname']
		lname=request.POST['lname']
		uname=request.POST['uname']
		email=request.POST['email']
		gender=request.POST['gender']
		nuser=UserDetails(fname=fname,lname=lname,uname=uname,email=email,gender=gender)
		nuser.save()
		return HttpResponseRedirect(reverse('userReg:result',args={nuser.id,}))
def result(request,user_id):
	ruser=UserDetails.objects.get(pk=user_id)
	if not ruser==None:
		return render(request,'result.html',{'user':ruser})

# Create your views here.
