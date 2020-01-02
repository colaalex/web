import factory.django

from . import models


class RandomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Question

    title = factory.Faker('sentence')
    text = factory.Faker('text')
    author = factory.Iterator(models.User.objects.all())
    rating = factory.Faker('random_int')


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Answer

    text = factory.Faker('text')
    question = factory.Iterator(models.Question.objects.all())
    author = factory.Iterator(models.User.objects.all())
