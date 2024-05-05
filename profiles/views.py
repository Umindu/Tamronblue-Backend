from rest_framework import permissions, generics
from .models import Profile
from .permissions import IsAdmin, IsAdminOrIsAgent, IsAgent
from .serializers import ProfileSerializer

# Admin only
# get all profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin]


# Admin and Agent only
# get a specific profile
class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrIsAgent]

# save the profile
class ProfileCreate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrIsAgent]

# update the profile
class ProfileUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrIsAgent]

# delete the profile
class ProfileDelete(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrIsAgent]