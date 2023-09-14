from rest_framework.views import APIView
from rest_framework import status
from .serializers import Personserializer
from .models import Person
from django.http import JsonResponse


class PersonView(APIView):
    serializer_class = Personserializer

    def post(self, request):
        """
        The endpoint to add a new person object - CREATE
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']

        # checks if a person with the same name already exists
        if Person.objects.filter(name=name).exists():
            return JsonResponse({"error":"person already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        #create a new person object
        new_person = Person()
        new_person.name = name
        new_person.save()
        data = {
            "message": "Person created successfully",
            "id": new_person.id,
            "name": new_person.name
        }
        return JsonResponse(data=data, status=status.HTTP_201_CREATED, safe=False)
        

    def get(self, request, user_id):
        """
        The endpoint to add a gets person object - READ
        """
        #get the person object from the db by id
        try:
            person = Person.objects.get(id=user_id)
        except:
            return JsonResponse({"error":"person does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(person, context={'request': request})
        data = serializer.data
        data["id"] = person.id
        return JsonResponse(data=data, status=status.HTTP_200_OK)


    def patch(self, request, user_id):
        """
        The endpoint to add a updates person object - UPDATE
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data["name"]

        try:
            person = Person.objects.get(id=user_id)
        except:
            return JsonResponse({"error":"person does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            person.name = name
            person.save()
        except:
            return JsonResponse({"error":"name already taken, Pick another name"}, status=status.HTTP_404_NOT_FOUND)
        data = {
            "message":"Person updated successfully",
            "id": person.id,
            "name": person.name

        }
        return JsonResponse(data, status=status.HTTP_200_OK)


    def delete(self, request, user_id):
        """
        The endpoint to add a deletes person object - DELETE
        """

        try:
            person = Person.objects.get(id=user_id)
        except:
            return JsonResponse({"error":"person does not exist"}, status=status.HTTP_404_NOT_FOUND)

        #deletes a person object
        person.delete()
        return JsonResponse({"message":"person object deleted successfully"}, status=status.HTTP_200_OK) 

    
