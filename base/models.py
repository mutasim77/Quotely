from django.db import models

""" 
this below class is equal to: 

CREATE TABLE Post (
    id INT PRIMARY KEY AUTO_INCREMENT,
    image VARCHAR(255),
    content VARCHAR(150) NOT NULL,
    author VARCHAR(100),
    date DATE DEFAULT CURRENT_TIMESTAMP
);

"""
class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    content = models.CharField(max_length=150, help_text="Write your quote here")
    author = models.CharField(max_length=100, help_text="The author of the quote", null=True)
    date = models.DateField(auto_now_add=True)