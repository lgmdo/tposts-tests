from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.health.serializers import HealthCheckSerializer


@extend_schema(responses=HealthCheckSerializer(), tags=["Health"])
@api_view(["GET"])
def health_check(_) -> Response:
    """
    Returns a simple JSON response for health check
    """
    return Response({"status": "ok"})
