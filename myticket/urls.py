from django.urls import path
from .views import *

urlpatterns=[
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:nit>', CompanyView.as_view(), name='companies_process'),
    path('projects/', ProjectView.as_view(), name='projects_list'),
    path('projects/<int:id>', ProjectView.as_view(), name='projects_process'),
    path('person/', PersonView.as_view(), name='person_list'),
    path('person/<int:dni>', PersonView.as_view(), name='person_process'),
    path('stories/', StoryView.as_view(), name='stories_list'),
    path('stories/<int:project_id>', StoryView.as_view(), name='stories_process'),
    path('story/<int:id>', StoryView.as_view(), name='story_delete'),
    path('tickets/<int:story_id>', TicketView.as_view(), name='ticketbyStory'),
    path('ticket/', TicketView.as_view(), name='tickets_list'),
    path('ticket/<int:id>', TicketView.as_view(), name='tickets_process')
]