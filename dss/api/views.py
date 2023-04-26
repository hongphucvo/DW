from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from .models import Customer
from .serializers import CustomerSerializer
from tensorflow.keras.models import load_model
import pandas as pd

class CustomerListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 0. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        # todos = []
        # serializer = CustomerSerializer(todos, many=True)
        data = pd.read_csv('''../model/btl_dw.csv''',header=0).drop(['loan_repaid'],axis=1)
        return Response(data.to_dict(orient='records'), status=status.HTTP_200_OK)
        # return Response({"msg":'This is DSS Pay loan'}, status=status.HTTP_200_OK)

        
    # 1. Predict
    def post(self, request, *args, **kwargs):
        data = request.data
        model = load_model('../model/full_data_project_model.h5')
        x_test = pd.DataFrame(data=data)
        if len(data)<1:
            return Response('Can not predict', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        pred = model.predict(x_test.drop(['loan_repaid'],axis=1).values.reshape(x_test.shape[0],78))
        result=list(map(lambda prediction: prediction[0], pred))
        return Response(result, status=status.HTTP_200_OK)
        # return Response({'predictions':result}, status=status.HTTP_200_OK)
   