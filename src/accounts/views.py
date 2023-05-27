from rest_framework.generics import RetrieveAPIView

from accounts.serializers import MemberSerializer


class UserInfoView(RetrieveAPIView):
    serializer_class = MemberSerializer

    def get_object(self):
        user = self.request.user
        return user
