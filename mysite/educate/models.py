from django.db import models


# Create your models here.
class roles(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)




class permission(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)



class users(models.Model):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    address = models.CharField(max_length=100)
    role_id = models.ForeignKey(roles, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)




class role_permission(models.Model):
    role_id = models.ForeignKey(roles, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(permission, on_delete=models.CASCADE)


class course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, null=True, max_length=254)
    price = models.FloatField()
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)



class course_user(models.Model):
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)




class course_document(models.Model):
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    chapter = models.IntegerField()
    status = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)





class course_document_file(models.Model):
    course_document_id = models.ForeignKey(course_document, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100)
    order = models.IntegerField()
    status = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)




class user_learning_history(models.Model):
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    course_document_file_id = models.ForeignKey(course_document, on_delete=models.CASCADE)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
