from rest_framework import permissions, generics
from .models import GrnDetail, Grn
from .permissions import IsAdmin, IsAdminOrIsAgent, IsAgent
from .serializers import GrnSerializer, GrnDetailSerializer

# Admin only
# get all Grn
class GrnList(generics.ListAPIView):
    queryset = Grn.objects.all()
    serializer_class = GrnSerializer
    permission_classes = [IsAdmin]

# get a specific Grn
class GrnDetail(generics.RetrieveAPIView):
    queryset = Grn.objects.all()
    serializer_class = GrnSerializer
    permission_classes = [IsAdmin]

# save the Grn
class GrnCreate(generics.CreateAPIView):
    queryset = Grn.objects.all()
    serializer_class = GrnSerializer
    permission_classes = [IsAdmin]

# update the Grn
class GrnUpdate(generics.UpdateAPIView):
    queryset = Grn.objects.all()
    serializer_class = GrnSerializer
    permission_classes = [IsAdmin]

# delete the Grn
class GrnDelete(generics.DestroyAPIView):
    queryset = Grn.objects.all()
    serializer_class = GrnSerializer
    permission_classes = [IsAdmin]


# Admin only
# get all GrnDetail
class GrnDetailList(generics.ListAPIView):
    queryset = GrnDetail.objects.all()
    serializer_class = GrnDetailSerializer
    permission_classes = [IsAdmin]

# get a specific GrnDetail
class GrnDetailDetail(generics.RetrieveAPIView):
    queryset = GrnDetail.objects.all()
    serializer_class = GrnDetailSerializer
    permission_classes = [IsAdmin]

# save the GrnDetail
class GrnDetailCreate(generics.CreateAPIView):
    queryset = GrnDetail.objects.all()
    serializer_class = GrnDetailSerializer
    permission_classes = [IsAdmin]

# update the GrnDetail
class GrnDetailUpdate(generics.UpdateAPIView):
    queryset = GrnDetail.objects.all()
    serializer_class = GrnDetailSerializer
    permission_classes = [IsAdmin]

# delete the GrnDetail
class GrnDetailDelete(generics.DestroyAPIView):
    queryset = GrnDetail.objects.all()
    serializer_class = GrnDetailSerializer
    permission_classes = [IsAdmin]




# from rest_framework import viewsets
# from .models import GrnDetail, Grn
# from .permissions import IsAdmin
# from .serializers import GrnSerializer, GrnDetailSerializer

# class GrnViewSet(viewsets.ModelViewSet):
#     queryset = Grn.objects.all()
#     serializer_class = GrnSerializer
#     permission_classes = [IsAdmin]

# class GrnDetailViewSet(viewsets.ModelViewSet):
#     queryset = GrnDetail.objects.all()
#     serializer_class = GrnDetailSerializer
#     permission_classes = [IsAdmin]
