from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from .tasks import send_welcome_email  # ایمپورت تسک Celery

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        profile = serializer.save()  # ذخیره پروفایل جدید
        send_welcome_email.delay(profile.email)  # ارسال ایمیل در پس‌زمینه


