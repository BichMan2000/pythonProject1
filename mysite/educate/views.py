from django.shortcuts import render
from.models import users,user_learning_history,roles,permission,role_permission,course_document_file,course_document,course,course_user
 #Create your views here.
def list(request):
   Data = {'student':users.objects.all().order_by("-create_at")}
   return render(request,'educate/educate.html',Data)
def Student(request,id):
  Student= users.objects.get(id=id)
  return render(request,'educate/student.html',{'user':Student})