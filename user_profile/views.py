from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models.certification import Certification
from .models.experience import Experience
from .models.hackathon import Hackathon
from .models.project import Project
from .models.socials import Social
import json


# Utility function to handle JSON request body
def json_body(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None


@csrf_exempt
@require_http_methods(["POST"])
def update_or_create_social(request, username):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    socials, created = Social.objects.update_or_create(
        username=username,
        defaults={'linkedin': data.get('linkedin'), 'github': data.get('github')}
    )
    return JsonResponse(
        {'id': socials.id, 'username': socials.username, 'linkedin': socials.linkedin, 'github': socials.github})


@csrf_exempt
@require_http_methods(["POST"])
def create_experience(request, username):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    experience = Experience(username=username, **data)
    experience.save()
    return JsonResponse({'id': experience.id, 'company': experience.company, 'designation': experience.designation,
                         'duration': experience.duration}, status=201)


@csrf_exempt
@require_http_methods(["PUT"])
def update_experience(request, username, id):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    try:
        experience = Experience.objects.get(id=id, username=username)
        for attr, value in data.items():
            setattr(experience, attr, value)
        experience.save()
        return JsonResponse({'id': experience.id, 'company': experience.company, 'designation': experience.designation,
                             'duration': experience.duration})
    except Experience.DoesNotExist:
        return HttpResponseNotFound('Experience not found')


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_experience(request, username, id):
    try:
        experience = Experience.objects.get(id=id, username=username)
        experience.delete()
        return JsonResponse({'message': 'Experience deleted'})
    except Experience.DoesNotExist:
        return HttpResponseNotFound('Experience not found')


@csrf_exempt
@require_http_methods(["POST"])
def create_project(request, username):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    project = Project(username=username, **data)
    project.save()
    return JsonResponse(
        {'id': project.id, 'name': project.name, 'description': project.description, 'link': project.link}, status=201)


@csrf_exempt
@require_http_methods(["PUT"])
def update_project(request, username, id):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    try:
        project = Project.objects.get(id=id, username=username)
        for attr, value in data.items():
            setattr(project, attr, value)
        project.save()
        return JsonResponse(
            {'id': project.id, 'name': project.name, 'description': project.description, 'link': project.link})
    except Project.DoesNotExist:
        return HttpResponseNotFound('Project not found')


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_project(request, username, id):
    try:
        project = Project.objects.get(id=id, username=username)
        project.delete()
        return JsonResponse({'message': 'Project deleted'})
    except Project.DoesNotExist:
        return HttpResponseNotFound('Project not found')


@csrf_exempt
@require_http_methods(["POST"])
def create_hackathon(request, username):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    hackathon = Hackathon(username=username, **data)
    hackathon.save()
    return JsonResponse(
        {'id': hackathon.id, 'name': hackathon.name, 'year': hackathon.year, 'achievements': hackathon.achievements},
        status=201)


@csrf_exempt
@require_http_methods(["PUT"])
def update_hackathon(request, username, id):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    try:
        hackathon = Hackathon.objects.get(id=id, username=username)
        for attr, value in data.items():
            setattr(hackathon, attr, value)
        hackathon.save()
        return JsonResponse({'id': hackathon.id, 'name': hackathon.name, 'year': hackathon.year,
                             'achievements': hackathon.achievements})
    except Hackathon.DoesNotExist:
        return HttpResponseNotFound('Hackathon not found')


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_hackathon(request, username, id):
    try:
        hackathon = Hackathon.objects.get(id=id, username=username)
        hackathon.delete()
        return JsonResponse({'message': 'Hackathon deleted'})
    except Hackathon.DoesNotExist:
        return HttpResponseNotFound('Hackathon not found')


@csrf_exempt
@require_http_methods(["POST"])
def create_certification(request, username):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    certification = Certification(username=username, **data)
    certification.save()
    return JsonResponse(
        {'id': certification.id, 'name': certification.name, 'issuingAuthority': certification.issuing_authority},
        status=201)


@csrf_exempt
@require_http_methods(["PUT"])
def update_certification(request, username, id):
    data = json_body(request)
    if data is None:
        return HttpResponseBadRequest("Invalid JSON")

    try:
        certification = Certification.objects.get(id=id, username=username)
        for attr, value in data.items():
            setattr(certification, attr, value)
        certification.save()
        return JsonResponse(
            {'id': certification.id, 'name': certification.name, 'issuingAuthority': certification.issuing_authority})
    except Certification.DoesNotExist:
        return HttpResponseNotFound('Certification not found')


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_certification(request, username, id):
    try:
        certification = Certification.objects.get(id=id, username=username)
        certification.delete()
        return JsonResponse({'message': 'Certification deleted'})
    except Certification.DoesNotExist:
        return HttpResponseNotFound('Certification not found')


@require_http_methods(["GET"])
def get_profile(request, username):
    try:
        experiences = list(
            Experience.objects.filter(username=username).values('id', 'company', 'designation', 'duration'))
        projects = list(Project.objects.filter(username=username).values('id', 'name', 'description', 'link'))
        hackathons = list(Hackathon.objects.filter(username=username).values('id', 'name', 'year', 'achievements'))
        certifications = list(Certification.objects.filter(username=username).values('id', 'name', 'issuing_authority'))
        socials = Social.objects.filter(username=username).values('id', 'linkedin', 'github').first()

        return JsonResponse({
            'experiences': experiences,
            'projects': projects,
            'hackathons': hackathons,
            'certifications': certifications,
            'socials': socials
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
