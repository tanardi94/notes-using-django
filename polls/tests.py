from asyncio import futures
import datetime
from time import time


from django.utils import timezone
from django.test import TestCase
from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futureQuestion = Question(pub_date=time)

        self.assertIs(futureQuestion.was_published_recently(), False)