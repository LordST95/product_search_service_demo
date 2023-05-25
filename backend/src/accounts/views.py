from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import RetrieveAPIView

from accounts.serializers import MemberSerializer


class UserInfoView(RetrieveAPIView, LoginRequiredMixin):
    serializer_class = MemberSerializer

    def get_object(self):
        user = self.request.user
        return user
