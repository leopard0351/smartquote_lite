from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import RoofCostEstimatorForm
from main.models import BusinessUser, QuotePricing, RoofQuote, FinalQuote
from scripts.logic.quick_estimator import calculate_quick_estimate
from django.db import transaction
from django.contrib import messages
import logging
from django.urls import reverse



logger = logging.getLogger(__name__)


class RoofCostEstimatorView(FormView):
    template_name = "main/roof_cost_estimator.html"
    form_class = RoofCostEstimatorForm

    def dispatch(self, request, *args, **kwargs):
        self.business = get_object_or_404(BusinessUser, slug=self.kwargs["slug"])
        self.pricing = get_object_or_404(QuotePricing, client=self.business)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["business"] = self.business
        return context

    def form_valid(self, form):
        cd = form.cleaned_data

        estimate = calculate_quick_estimate(
            pricing=self.pricing,
            building_type=cd["building_type"],
            material_type=cd["material_type"],
            square_footage=cd["approximate_sqft"],
            stories=cd["stories"],
            roof_complexity=cd["roof_complexity"],
        )

        with transaction.atomic():
            quote = RoofQuote.objects.create(
                business_user=self.business,
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
                estimate_middle=estimate["mid"],
                estimate_max=estimate["high"],
            )

            FinalQuote.objects.create(
                roof_quote=quote,
                pricing_config=self.pricing,
                business_user=self.business,
                building_type=cd["building_type"],
                project_type="new_roof",
                material_type=cd["material_type"],
                square_footage=cd["approximate_sqft"],
                permit_cost=estimate["permit"],
                final_total_low=estimate["low"],
                final_total_mid=estimate["mid"],
                final_total_high=estimate["high"],
                finalized=False,
            )

        return redirect(
            f"{reverse('main:roof_estimate_thank_you', kwargs={'slug': self.business.slug})}?quote={quote.id}"
        )

    def form_invalid(self, form):
        logger.warning("RoofCostEstimatorForm invalid: %s", form.errors.as_json())
        return self.render_to_response(self.get_context_data(form=form))


class RoofEstimateThankYouView(TemplateView):
    template_name = "main/roof_estimate_thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        business = get_object_or_404(BusinessUser, slug=self.kwargs["slug"])
        context["business"] = business

        quote_id = self.request.GET.get("quote")
        quote = None

        if quote_id:
            quote = RoofQuote.objects.filter(
                id=quote_id,
                business_user=business,
            ).first()

        context["quote"] = quote
        return context
        
class QuoteResultsListView(LoginRequiredMixin, ListView):
    model = RoofQuote
    template_name = "main/quote_results_list.html"
    context_object_name = "quotes"
    ordering = ["-created_at"]
    login_url = "/admin/login/"