import datetime

from django.utils import timezone

from polls.models import Choice, Question


def create_choice(question, choice_text, votes=0):
    """
    Create a choice for the given 'question' choice_text'.
    """
    return Choice.objects.create(question=question, choice_text=choice_text, votes=votes)


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)