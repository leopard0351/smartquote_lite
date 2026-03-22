from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import RoofCostEstimatorForm
from main.models import BusinessUser, QuotePricing, RoofQuote, FinalQuote
from scripts.logic import quick_estimator


class RoofCostEstimatorView(TemplateView):
    template_name = "main/roof_cost_estimator.html"

    def get(self, request, slug, *args, **kwargs):
        business = get_object_or_404(BusinessUser, slug=slug)
        form = RoofCostEstimatorForm()
        return render(request, self.template_name, {
            "form": form,
            "business": business,
            "result": None,
        })

    def post(self, request, slug, *args, **kwargs):
        business = get_object_or_404(BusinessUser, slug=slug)
        pricing = get_object_or_404(QuotePricing, client=business)
        form = RoofCostEstimatorForm(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {
                "form": form,
                "business": business,
                "result": None,
            })

        cd = form.cleaned_data

        estimate = quick_estimator(
            pricing=pricing,
            building_type=cd["building_type"],
            material_type=cd["material_type"],
            square_footage=cd["approximate_sqft"],
            stories=cd["stories"],
            roof_complexity=cd["roof_complexity"],
        )

        quote = RoofQuote.objects.create(
            business_user=business,
            first_name=cd["first_name"],
            last_name=cd["last_name"],
            email=cd["email"],
            phone=cd["phone"],
            address=cd["address"],
            project_type="new_roof",
            building_type=cd["building_type"],
            stories=cd["stories"],
            final_area_sqft=cd["approximate_sqft"],
            square_footage=cd["approximate_sqft"],
            material_type=cd["material_type"],
            roof_complexity=cd["roof_complexity"],
            permission_for_quote=cd["permission_for_quote"],
            have_insurance=cd["have_insurance"],
            estimate_min=estimate["low"],
            estimate_max=estimate["high"],
        )

        FinalQuote.objects.create(
            roof_quote=quote,
            pricing_config=pricing,
            business_user=business,
            building_type=cd["building_type"],
            project_type="new_roof",
            material_type=cd["material_type"],
            square_footage=cd["approximate_sqft"],
            permit_cost=estimate["permit"],
            final_total_low=estimate["low"],
            final_total_high=estimate["high"],
            finalized=False,
        )

        return render(request, self.template_name, {
            "form": RoofCostEstimatorForm(),
            "business": business,
            "result": estimate,
            "quote": quote,
        })
    
class QuoteResultsListView(LoginRequiredMixin, ListView):
    model = RoofQuote
    template_name = "main/quote_results_list.html"
    context_object_name = "quotes"
    ordering = ["-created_at"]
    login_url = "/admin/login/"