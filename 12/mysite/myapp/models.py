from django.db import models

# Модель категории программного обеспечения
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Модель пользователя
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

# Модель программы
class Software(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # Связь с категорией
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Связь с пользователем

    def __str__(self):
        return self.name
