from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("<slug:slug>/roof-estimate/", views.RoofCostEstimatorView.as_view(), name="roof_cost_estimator"),
    path("<slug:slug>/roof-estimate/thank-you/", views.RoofEstimateThankYouView.as_view(), name="roof_estimate_thank_you"),
    path("quotes/results/", views.QuoteResultsListView.as_view(), name="quote_results_list"),
]