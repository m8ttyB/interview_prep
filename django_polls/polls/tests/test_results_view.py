from django.test import TestCase
from django.urls import reverse

from .utils import create_choice, create_question


class QuestionResultViewTest(TestCase):
    def test_past_question_with_no_choices(self):
        """
        The result view of a question that has no choices associated
        with it should return a 404
        """
        question = create_question('A good question', days=-1)
        url = reverse('polls:results', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_past_question_with_choices(self):
        """
        The result view shows results for past questions that have
        choices associated with it.
        """
        question = create_question('A past question with choices', -1)
        choice = create_choice(question, 'A good choice', 37)
        url = reverse('polls:results', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['question'], question)
        self.assertContains(resp, choice.choice_text)

    def test_future_question_with_choices(self):
        """
        The result view should not be available for poll questions
        that have a future publish date.
        """
        question = create_question('A future question with choices', 37)
        create_choice(question, 'A bad choice')
        url = reverse('polls:results', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_future_question_no_choices(self):
        """
        The result view should not show questions that have a future
        publish date.
        """
        question = create_question('A future question with choices', 37)
        url = reverse('polls:results', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_past_question_choices_with_votes(self):
        """
        The result view should return a 200 OK when displaying votes
        for multiple choices
        """
        question = create_question('A past question with choices', -1)
        choice_1 = create_choice(question, 'Choice 1', 37)
        choice_2 = create_choice(question, 'Choice 2', 1)
        url = reverse('polls:results', args=(question.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['question'], question)
        self.assertContains(resp, choice_1.choice_text)
        self.assertContains(resp, choice_2.choice_text)
