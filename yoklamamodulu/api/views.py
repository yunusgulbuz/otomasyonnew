
from rest_framework.generics import ListAPIView

from yoklamamodulu.api.serializers import DersSerializer
from yoklamamodulu.models import Dersler


class DersView(ListAPIView):
    queryset = Dersler.objects.all()
    serializer_class = DersSerializer
