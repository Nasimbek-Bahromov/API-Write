from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ContactSerializer, BannerSerializer, ServiceSerializer, InfoSerializer
from main.models import Contact, Banner, Service, Info

#contact uchun yozdim
@api_view(['GET'])
def contact_list(request):
    contact = Contact.objects.all()
    serializer_data =  ContactSerializer(contact, many = True)
    return Response(serializer_data.data)


#banner uchun yozdim
class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerCreateView(generics.CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDetailView(generics.RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerUpdateView(generics.UpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDeleteView(generics.DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

#service uchun yozdim
    
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


#info uchun yozdim
class InfoListView(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoCreateView(generics.CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoDetailView(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoUpdateView(generics.UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoDeleteView(generics.DestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer