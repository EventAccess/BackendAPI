from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from database.models import Attendant

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from backendapi import exceptions
from .serializers import AttendantAdmin


@csrf_exempt
@require_POST
@never_cache
def scanned(request, tag: bytes):
    try:
        attendant = Attendant.objects.get(nfc_id=tag)
        # TODO: Queue event
        return JsonResponse({"valid": attendant.is_valid}, status=202)

    except Attendant.DoesNotExist:
        return JsonResponse({"error": "No such tag", "valid": False}, status=404)


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def api_get(request, pk=None):
    if request.method == "GET":
        # If there's no 'pk' parameter, return all attendants
        if pk is None:
            attendants = Attendant.objects.all()
            serializer = AttendantAdmin(attendants, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Otherwise, return a single attendant
        try:
            attendant = Attendant.objects.get(pk=pk)
            serializer = AttendantAdmin(attendant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Attendant.DoesNotExist:
            return Response(
                {"detail": "Attendant not found."}, status=status.HTTP_404_NOT_FOUND
            )

    elif request.method == "POST":
        # Create a new attendant
        serializer = AttendantAdmin(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new attendant to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        # Full update of an existing attendant
        try:
            attendant = Attendant.objects.get(pk=pk)
        except Attendant.DoesNotExist:
            return Response(
                {"detail": "Attendant not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AttendantAdmin(attendant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        # Partial update of an existing attendant
        try:
            attendant = Attendant.objects.get(pk=pk)
        except Attendant.DoesNotExist:
            return Response(
                {"detail": "Attendant not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AttendantAdmin(attendant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Delete an existing attendant
        try:
            attendant = Attendant.objects.get(pk=pk)
        except Attendant.DoesNotExist:
            return Response(
                {"detail": "Attendant not found."}, status=status.HTTP_404_NOT_FOUND
            )

        attendant.delete()
        return Response(
            {"detail": "Attendant deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


"""
def api_get(request):
    if request.method == "GET":
        return Response({"message": "GET request received"}, status=202)
    elif request.method == "POST":
        return Response({"message": "POST request received"}, status=405) """

def base_view(request): #basic frontend registration view.
    return render(request, "base.html")

def registration_view(request):
    return render(request, "registration.html")
