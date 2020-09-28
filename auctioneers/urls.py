from django.urls import path
from .views import AuctioneerListView, AuctioneerView, TopSellerView

urlpatterns = [
    path('', AuctioneerListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', AuctioneerView.as_view()),
]
