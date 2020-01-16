from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from pulpcore.app.serializers import ApplicabilitySerializer


class ApplicabilityView(APIView):
    """
    Returns applicability information about a given list of repos.
    """

    @swagger_auto_schema(operation_summary="Post appliability query to Pulp",
                         operation_id="applicability_post",
                         responses={400: ApplicabilitySerializer})
    def post(self, request, format=None):
        """
        Returns applicability information for the given repos and nevra lists.
        """

        data = {
            'name': name,
            'epoch':epoch,
        }

        context = {'request': request}
        serializer = ApplicabilitySerializer(data, context=context)
        return Response(serializer.data)