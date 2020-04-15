from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from authentication.serializers import *
from django.utils.encoding import force_bytes, force_text


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

        # if self.context["view"].token_generator.check_token(self.user, token):
        #     self.user.is_active = True
        #     self.user.save()
        # is_token_valid = self.context["view"].token_generator.check_token(
        #     self.user, self.initial_data.get("token", "")
        # )
        # if is_token_valid:
        #     self.user.is_active = True
        #     self.user.save()


# class RegistrationAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = RegistrationSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializers_class = LoginSerializer
#
#     def post(self, request):
#         user = request.data
#         serializer = self.serializers_class(data=user)
#         serializer.is_valid(raise_exception=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class ProfileAPIView(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthenticated, )
#     serializer_class = ProfileSerializer
#     queryset = User.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(request.user)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def update(self, request, *args, **kwargs):
#         serializer_data = request.data
#
#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status.HTTP_200_OK)