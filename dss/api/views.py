from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from .models import Customer
from .serializers import CustomerSerializer

class CustomerListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        
        # todos = Todo.objects.filter(user = request.user.id)
        todos = []
        serializer = CustomerSerializer(todos, many=True)
        return Response(request.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = CustomerSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # 3. Predict
    def post(self, request, *args, **kwargs):
        data = request.data
        from tensorflow.keras.models import load_model
        model = load_model('full_data_project_model.h5')

        return Response('good', status=status.HTTP_200_OK)


        serializer = CustomerSerializer(data=data)
        return Response(serializer.get_value(), status=status.HTTP_200_OK)
        # {
        #     'task': request.data.get('task'), 
        #     'completed': request.data.get('completed'), 
        #     'user': request.user.id
        # }
        serializer = CustomerSerializer(data=data)
        
        return Response('good', status=status.HTTP_200_OK)
    