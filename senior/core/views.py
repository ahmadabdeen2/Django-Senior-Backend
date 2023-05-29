from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import UserModel
from .serializers import UserModelSerializer, UserCreationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .utils import preprocess_features
from django.http import HttpResponse

# from .your_ml_module import preprocess_input_data  # Assuming you have this function

User = get_user_model()


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class UserModelViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class UserCreationView(APIView):
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "User created successfully"})
        else:
            return Response(serializer.errors, status=400)



# from .your_ml_module import preprocess_input_data  # Assuming you have this function


User = get_user_model()

class KeystrokeTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid()
        print(serializer.validated_data)
        print(serializer.errors)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise e

        username = request.data.get('username')
        password = request.data.get('password')
        keystroke_data = request.data.get('features')

        print(username)
        print(password)
        print(keystroke_data)
        

        try:
            # Retrieve user instance
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credential oks"}, status=401)
        
        # Preprocess keystroke data
        processed_data = preprocess_features(keystroke_data)

        # Load your model (better to do this once and store in memory)
        keystroke_model = apps.get_app_config('core').keystroke_model

        # Use the model to predict
        predictions = keystroke_model.predict(processed_data)

        # Perform your check on the prediction
        # This will depend on how your model's output is structured
        # user_prediction = predictions[0]
        print(predictions)
        # if user_prediction < 0.7:
        #     return Response({"detail": "Keystroke dynamics do not match."}, status=401)

        # Perform standard Django authentication
        user = authenticate(username=username, password=password)
        if user is not None:
            # If authentication was successful, return the token response
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Unmatching Keystroke"}, status=401)