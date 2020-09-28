from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Auctioneer
from .serializers import AuctioneerSerializer


class AuctioneerListView(ListAPIView):
    """ View all auctioneers without auth, (all view are protected by default) """
    permission_classes = (permissions.AllowAny, )
    queryset = Auctioneer.objects.all()
    serializer_class = AuctioneerSerializer
    pagination_class = None

class AuctioneerView(RetrieveAPIView):
    """ View auctioneer by pk """
    queryset = Auctioneer.objects.all()
    serializer_class = AuctioneerSerializer

class TopSellerView(ListAPIView):
    """ View topseller auctioneers without auth """
    permission_classes = (permissions.AllowAny, )
    queryset = Auctioneer.objects.filter(top_seller=True)
    serializer_class = AuctioneerSerializer
    pagination_class = None
