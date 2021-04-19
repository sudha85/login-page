from django.db import models

class login(models.Model):
    login_text=models.CharField(max_length=100)
    def __str__(self):
        return self.login_text

class Register(models.Model):
    Register_text=models.CharField(max_length=50)
    def __str__(self):
        return self.Register_text

class ResetPassword(models.Model):
    ResetPasword_text=models.CharField(max_length=50)
    def __str__(self):
        return self.ResetPassword_text
