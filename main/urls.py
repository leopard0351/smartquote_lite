from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "main"


urlpatterns = [
    path("<slug:slug>/roof-estimate/", views.RoofCostEstimatorView.as_view(), name="roof_cost_estimator"),
    path("quotes/results/", views.QuoteResultsListView.as_view(), name="quote_results_list"),
]