from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from rest_framework import generics
from rest_framework.views import APIView

from .models import User
from .serializers import AccountSerializer


class UserActivationView(APIView):
    def post(self, request, uid, token):
        try:
            uid = force_text(urlsafe_base64_decode(uid))
            self.user = User.objects.get(pk=uid)
            self.user.is_active = True
            self.user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')

        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            key_error = "invalid_uid"
            raise key_error


class AccountView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

