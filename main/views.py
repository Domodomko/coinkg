from django.http import Http404
from django.utils import timezone
from django.core.mail import send_mail

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *

from rest_framework_json_api.pagination import JsonApiPageNumberPagination, JsonApiLimitOffsetPagination


class MyLimitPagination(JsonApiLimitOffsetPagination):
    offset_query_param = 'offset'
    limit_query_param = 'limit'
    default_limit = 7
    max_limit = None


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = MyLimitPagination


class NewsDetailView(APIView):
    queryset = News.objects.filter(publish__lte=timezone.now())
    serializer_class = NewsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.queryset.get(id=pk)
        except self.queryset.model.DoesNotExist:
            raise Http404
        else:
            instance.views += 1
            instance.save()
            serializer = self.serializer_class(instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class SuccessStoryListView(generics.ListAPIView):
    queryset = SuccessStory.objects.all()
    serializer_class = SuccessStorySerializer


class AboutUsListView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class FeedBackCreateView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedbackSerializer

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        content = request.POST.get('content', '')
        message = 'Имя: ' + name + '; ' \
                  + 'Email: ' + email + '; ' \
                  + 'Телефон: ' + phone + '; ' \
                  + 'Сообщение: ' + content
        send_mail('FeedBack', message, 'dasdasddsda@mail.ru',
                  ['sergey_shinn@mail.ru'],
                  fail_silently=False,
                  )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreditListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class CreditsInfoListView(generics.ListAPIView):
    queryset = CreditsInfo.objects.all()
    serializer_class = CreditsInfoSerializer
