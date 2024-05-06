from rest_framework import permissions, generics
from .models import Salary
from .permissions import IsAdmin, IsAdminOrIsAgent, IsAgent
from .serializers import SalarySerializer

# Admin only
# get all salaries
class SalaryList(generics.ListAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAdmin]

# get a specific salary
class SalaryDetail(generics.RetrieveAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAdmin]

# save the salary
class SalaryCreate(generics.CreateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAdmin]

# update the salary
class SalaryUpdate(generics.UpdateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAdmin]

# delete the salary
class SalaryDelete(generics.DestroyAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAdmin]