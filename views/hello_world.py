from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    """
    Returns a success message
    """

    def get(self, request, *args, **kwargs):
        """
        View to serve GET requests
        :param request: the request that is to be responded to
        :param args: arguments
        :param kwargs: keyword arguments
        :return: the response for request
        """

        response_data = {
            'status': 'SUCCESS',
            'message': (
                'You have successfully initiated [[app_name]] and taken the '
                'first step to building your Omniport app. Edit '
                'views.hello_world and make this app do magical things. We '
                'can\'t wait to see what you make.'
            ),
            'greetings': 'Team Omniport',
        }

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )
