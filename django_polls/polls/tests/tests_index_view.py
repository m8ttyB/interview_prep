from django.test import TestCase
from django.urls import reverse

from .utils import create_choice, create_question


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        resp = self.client.get(reverse('polls:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No polls are available.')
        self.assertQuerysetEqual(resp.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question('past question 1', -30)
        create_choice(question, 'Past choice')
        resp = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(resp.context['latest_question_list'],
                                 [question])

    def test_only_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question('future question', 30)
        resp = self.client.get(reverse('polls:index'))
        self.assertContains(resp, 'No polls are available.')
        self.assertQuerysetEqual(resp.context['latest_question_list'], [])

    def test_question_without_choices(self):
        """
        Past questions that don't have choices are not displayed on the
        index page.
        """
        question = create_question("No choices", -1)
        resp = self.client.get(reverse('polls:index'))
        self.assertContains(resp, 'No polls are available.')

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question('future question', 30)
        question = create_question('past question', -1)
        create_choice(question, 'One good choice')
        resp = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(resp.context['latest_question_list'],
                                 [question])

    def test_two_past_questions(self):
        """
        The questions index page may display multiple past questions.
        """
        question_1 = create_question('Question 1', -30)
        question_2 = create_question('Question 2', -5)
        create_choice(question_1, 'choice 1')
        create_choice(question_1, 'choice 1 again')
        create_choice(question_2, 'choice 2')
        resp = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(resp.context['latest_question_list'],
                                 [question_1, question_2])
