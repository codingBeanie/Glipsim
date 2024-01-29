from rest_framework.views import APIView
from rest_framework.response import Response
from simulation.models import *


class API_Stats(APIView):
    def get(self, request):
        statistics = list(Statistics.objects.values())
        return Response(statistics)


class API_Households(APIView):
    def get(self, request):
        households = list(Household.objects.values())
        for household in households:
            members = Glip.objects.filter(household=household['id']).values()
            count_members_alive = Glip.objects.filter(
                household=household['id'], alive=True).values().count()
            household['members'] = list(members)
            household['count_members_alive'] = count_members_alive

        # remove households with no members
        households = [
            household for household in households if household['members']]
        # remove households with no members alive
        households = [
            household for household in households if household['count_members_alive'] > 0]
        return Response(households)
