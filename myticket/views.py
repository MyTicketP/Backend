from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.views import APIView
from .serializers import PersonSerializer
import json
from .models import *

# Create your views here.

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,  **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, nit=0):
        if (nit > 0):
            companies = list(Company.objects.filter(nit=nit).values())
            if len(companies) > 0:
                company = companies[0]
                datos={'message':"Success",'companies':company}
            else:
                datos={'message':"Company not found... "}
            return JsonResponse(datos)
        else:         
            companies=list(Company.objects.values())
            if len(companies)>0:
                datos={'companies':companies}
            else:
                datos={'message':"Companies not found... "}

            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Company.objects.create(nit=jd['nit'], name=jd['name'], tel=jd['tel'], dir=jd['dir'], email=jd['email'])
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self, request, nit):
        jd=json.loads(request.body)
        companies = list(Company.objects.filter(nit=nit).values())
        if len(companies) > 0:
            company = Company.objects.get(nit=nit)
            company.name = jd['name']
            company.tel = jd['tel']
            company.dir = jd['dir']
            company.email=jd['email']
            company.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Companies not found... "}
        
        return JsonResponse(datos)

    def delete(self, request, nit):
        companies = list(Company.objects.filter(nit=nit).values())
        if len(companies) > 0:
            Company.objects.filter(nit=nit).delete()
            datos={'message':"Success"}
        else: 
            datos={'message':"Company not found... "}
        
        return JsonResponse(datos)



class ProjectView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,  **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id=0):
        if (id > 0):
            projects = list(Project.objects.filter(id=id).values())
            if len(projects) > 0:
                datos={'message':"Success",'projects':projects}
            else:
                datos={'message':"Project not found... "}
            return JsonResponse(datos)
        else:         
            projects=list(Project.objects.values())
            if len(projects)>0:
                datos={'message':"Success",'projects':projects}
            else:
                datos={'message':"Projects not found... "}

            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Project.objects.create(name=jd['name'], company_id=jd['company_id'])
        datos={'message':"Success"}
        return JsonResponse(datos)


    def delete(self, request, id):
        projects = list(Project.objects.filter(id=id).values())
        if len(projects) > 0:
            Project.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else: 
            datos={'message':"Project not found... "}
        
        return JsonResponse(datos)




class PersonView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,  **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, dni=0):
        if (dni > 0):
            people = list(Person.objects.filter(dni=dni).values())
            if len(people) > 0:
                person = people[0]
                datos={'message':"Success",'people':person}
            else:
                datos={'message':"Person not found... "}
            return JsonResponse(datos)


    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def delete(self, request, dni):
        people = list(Person.objects.filter(dni=dni).values())
        if len(people) > 0:
            Person.objects.filter(dni=dni).delete()
            datos={'message':"Success"}
        else: 
            datos={'message':"Person not found... "}
        
        return JsonResponse(datos)





class StoryView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,  **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, project_id=0):
        if (project_id > 0):
            stories = list(Story.objects.filter(project_id=project_id).values())
            if len(stories) > 0:
                datos={'message':"Success",'stories':stories}
            else:
                datos={'message':"Stories not found... "}
            return JsonResponse(datos)
        else:         
            stories=list(Story.objects.values())
            if len(stories)>0:
                datos={'message':"Success",'stories':stories}
            else:
                datos={'message':"Stories not found... "}

            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Story.objects.create(name=jd['name'], project_id=jd['project_id'], person_id=jd['person_id'])
        datos={'message':"Success"}
        return JsonResponse(datos)


    def delete(self, request, id):
        stories = list(Story.objects.filter(id=id).values())
        if len(stories) > 0:
            Story.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else: 
            datos={'message':"Story not found... "}
        
        return JsonResponse(datos)





class TicketView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,  **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, story_id=0):
        if (story_id > 0):
            tickets = list(Ticket.objects.filter(story_id=story_id).values())
            if len(tickets) > 0:
                datos={'message':"Success",'tickets':tickets}
            else:
                datos={'message':"Ticket not found... "}
            return JsonResponse(datos)
        else:         
            tickets=list(Ticket.objects.values())
            if len(tickets)>0:
                datos={'message':"Success",'tickets':tickets}
            else:
                datos={'message':"Tickets not found... "}

            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Ticket.objects.create(state=jd['state'], text=jd['text'], validity=jd['validity'], story_id=jd['story_id'])
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        tickets = list(Ticket.objects.filter(id=id).values())
        if len(tickets) > 0:
            ticket = Ticket.objects.get(id=id)
            ticket.state = jd['state']
            ticket.text = jd['text']
            ticket.validity = jd['validity']
            ticket.story_id=jd['story_id']
            ticket.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Tickets not found... "}
        
        return JsonResponse(datos)

    def delete(self, request, id):
        tickets = list(Ticket.objects.filter(id=id).values())
        if len(tickets) > 0:
            Ticket.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else: 
            datos={'message':"Ticket not found... "}
        
        return JsonResponse(datos)