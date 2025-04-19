from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HealthCheckSerializer


@extend_schema(responses=HealthCheckSerializer, tags=["Health"])
class HealthCheckView(APIView):
    """
    Returns a simple JSON response for health check
    """

    def get(self, _):
        serializer = HealthCheckSerializer({"status": "ok"})
        return Response(serializer.data)

