from django.db import models
from django.contrib.auth.models import User

# Model to store the Questions--
class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # To show the informative information in the DB
    def __str__(self):
        return self.title

# Model to store the Answers--
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # To show the informative information in the DB
    def __str__(self):
        return f"Answer to {self.question.title} by {self.created_by.username}"

class Like(models.Model):
    answer = models.ForeignKey(Answer, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)