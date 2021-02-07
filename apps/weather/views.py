from django.contrib.auth.mixins                                                     import LoginRequiredMixin
from django.views.generic                                                           import View
from django.utils                                                                   import timezone
import pytz
from collections                                                                    import defaultdict
from datetime                                                                       import datetime
from django.views.generic.edit      import CreateView
# from udms.core.mixins                                                               import UserLevelMixin
from django.urls                                                                    import reverse_lazy
from django.shortcuts                                                               import render, redirect, reverse
from django.contrib                                                                 import messages
from .                                                                             import template

from django.db.models                                                               import Count, F, Value, Subquery, Case, When, OuterRef
from django.forms                                                                   import BooleanField, IntegerField
from django.db.models.functions                                                     import Length, Upper

from apps.city.models                                                               import City

from API                                                                            import open_weather_app

from .forms                                                                         import WeatherSelectForm


# class EntitySelectView(View):
#     template_name, userlevel_needed = template.path('EntitySelectView')
#
#     def get(self, request, *args, **kwargs):
#
#         if not request.GET:
#
#             form = EntitySelectForm(request.GET or None)
#             context = {'form': form, 'function': 'questionnaire'}
#
#             return render(request, template_name=self.template_name, context=context)


# class QuestionnaireListView(View):
#     template_name, userlevel_needed = template.path('QuestionnaireListView')
#
#     def get(self, request, *args, **kwargs):
#
#         if not request.GET:
#
#             form = EntityDomainSelectForm(request.GET or None)
#             context = {'form': form}
#
#             return render(request, template_name=self.template_name, context=context)
#
#         else:
#             total_none = 0
#             total_yes = 0
#             total_no = 0
#
#             entity_id = request.GET.get('entity_id')
#             domain_id = request.GET.get('domain_id')
#
#             responses = Response.objects.filter(entity_id=entity_id,  question__section__domain=domain_id)
#
#             questions = Question.objects.filter(section__domain=domain_id)\
#                 .annotate(
#                     response=Subquery(responses.filter(question_id=OuterRef('id')).values('answer'))
#                 )
#
#             domain_text = questions[0].section.domain.domain_text
#
#             for question in questions:
#                 if question.response == True:
#                     total_yes += 1
#                 elif question.response == False:
#                     total_no += 1
#                 else:
#                     total_none += 1
#
#             part_yes  = total_yes / len(questions) * 100
#             part_no   = total_no / len(questions) * 100
#             part_none = total_none / len(questions) * 100
#
#             context = {
#                 'entity_id': entity_id,
#                 'questions': questions,
#                 'part_yes': part_yes,
#                 'part_no': part_no,
#                 'part_none': part_none,
#                 'domain_text': domain_text,
#             }
#
#             return render(request, self.template_name, context=context)
#             # return redirect(reverse_lazy('app-list', kwargs={'npo_id': npo_id}))
#
#             # url_vars = f'?npo_id={npo_id}'
#             #
#             # return redirect(reverse_lazy('app-list') + url_vars)
#
#     def post(self, request, *args, **kwargs):
#
#         entity_id = self.kwargs['entity_id']
#
#         # timezone.now()
#         # user = self.request.user.
#
#         question_answer_ids = dict(request.POST.lists())
#         question_answer_ids.pop('csrfmiddlewaretoken')
#
#         questions = Question.objects.all()
#         entity_object = Entity.objects.get(pk=entity_id)
#         responses = Response.objects.filter(entity_id=entity_id)
#
#         total_yes = 0
#         total_no = 0
#         for question_id, answer_val in question_answer_ids.items():
#
#             if 'YES' in answer_val:
#                 total_yes += 1
#                 answer = True
#             elif 'NO' in answer_val:
#                 total_no += 1
#                 answer = False
#             else:
#                 continue
#
#             response = responses.filter(question_id=question_id).first()
#             if response:
#                 response.answer = answer
#                 response.last_response = timezone.now()
#                 response.user = self.request.user
#                 response.save()
#             else:
#                 Response.objects.create(
#                     question =  questions.get(pk=question_id),
#                     entity =       entity_object,
#                     user =      self.request.user,
#                     answer = answer,
#                     last_response = timezone.now()
#                 )
#
#         return redirect(reverse_lazy('response-list'))


class WeatherSearchView(View):
    template_search  = template.path('WeatherSearchView')
    template_results = template.path('WeatherResultsView')

    def get(self, request, *args, **kwargs):

        if not request.GET:

            form = WeatherSelectForm(request.GET or None)
            context = {'form': form}

            return render(request, template_name=self.template_search, context=context)

        else:

            form = WeatherSelectForm(request.GET or None)

            city_name   = form.data['city_name']
            period      = form.data['period']

            if period == 'today':
                results     = open_weather_app.get_current_weather_by_city_name(city_name)

            elif period == '7_days':
                results     = open_weather_app.get_period_weather_by_city_name(city_name, 20)

            context     = {'form': form, 'city_name': city_name, 'results': results, 'period': period}

            return render(request, template_name=self.template_results, context=context)
