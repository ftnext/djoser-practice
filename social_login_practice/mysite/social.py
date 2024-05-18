from django.http import JsonResponse
from django.views import View


class RedirectSocialView(View):
    def get(self, request):
        return JsonResponse(
            {
                "code": str(request.GET["code"]),
                "state": str(request.GET["state"]),
            }
        )
