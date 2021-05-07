from django.test import TestCase
from django.urls import reverse

from .utils import create_choice, create_question


class QuestionDetailViewTests(TestCase):
    def test_future_question_with_choice(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        question = create_question('Future question', 30)
        create_choice(question, 'a future choice')
        url = reverse('polls:detail', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_future_question_no_choices(self):
        """
        The detail view of a question with a pub_date in the future
        and no choice returns a 404 not found.
        """
        question = create_question('Future question', 30)
        create_choice(question, 'a future choice')
        url = reverse('polls:detail', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_past_question_with_choice(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        question = create_question('Past question', -30)
        create_choice(question, 'A choice')
        url = reverse('polls:detail', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, question.question_text)

    def test_past_question_with_multiple_choices(self):
        """
        The detail view of a question with a pub_date in the past
        and multiple choices displays the question's text.
        """
        question = create_question('Past question', -30)
        create_choice(question, 'One choice')
        create_choice(question, 'two choice')
        url = reverse('polls:detail', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, question.question_text)

    def test_past_question_no_choices(self):
        """
        The detail view should return a 4040 for a past question
        with no associated choices.
        """
        question = create_question('Past question', -1)
        url = reverse('polls:detail', args=(question.id, ))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)