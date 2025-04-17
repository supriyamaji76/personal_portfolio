from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    number = models.CharField(max_length=15, null=True)
    content = models.TextField(max_length=500)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
SKILL_CATEGORIES = [
    ('Language', 'Language'),
    ('Technology', 'Technology'),
    ('Course', 'Course'),
    ('Database', 'Database'),
]

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)

    def __str__(self):
        return f"{self.name} ({self.category})"