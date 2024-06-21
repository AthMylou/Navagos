from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from .views import CategoryListCreateView, CategoryDetailView, QuestionListCreateView, QuestionDetailView, AnswerListCreateView, AnswerDetailView, QuestionAnswerListCreateView, QuestionAnswerDetailView, TestListCreateView, TestDetailView, TestQuestionListCreateView, TestQuestionDetailView, UserViewSet, UserLogIn

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('answers/', AnswerListCreateView.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerDetailView.as_view(), name='answer-detail'),
    path('question-answers/', QuestionAnswerListCreateView.as_view(), name='question-answer-list-create'),
    path('question-answers/<int:pk>/', QuestionAnswerDetailView.as_view(), name='question-answer-detail'),
    path('tests/', TestListCreateView.as_view(), name='test-list-create'),
    path('tests/<int:pk>/', TestDetailView.as_view(), name='test-detail'),
    path('test-questions/', TestQuestionListCreateView.as_view(), name='test-question-list-create'),
    path('test-questions/<int:pk>/', TestQuestionDetailView.as_view(), name='test-question-detail'),
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('api-user-login/', UserLogIn.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
]

