from django.db import models
import uuid

class BusinessUser(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.company_name or self.name


class QuotePricing(models.Model):
    client = models.ForeignKey(BusinessUser, on_delete=models.CASCADE, related_name="pricing_profiles")

    residential_profit_low_per_sqft = models.DecimalField(max_digits=5, decimal_places=2, default=1.25)
    residential_profit_high_per_sqft = models.DecimalField(max_digits=5, decimal_places=2, default=2.50)

    commercial_profit_low_per_sqft = models.DecimalField(max_digits=5, decimal_places=2, default=0.75)
    commercial_profit_high_per_sqft = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)

    asphalt_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=1.25)
    composite_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=3.75)
    metal_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=4.50)
    clay_tile_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=7.00)
    concrete_tile_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)
    wood_shingles_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=4.50)
    copper_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=18.00)
    rolled_roofing_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=1.50)
    solar_shingles_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=15.00)

    asphalt_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=2.75)
    composite_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=6.00)
    metal_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=8.00)
    clay_tile_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)
    concrete_tile_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=7.50)
    wood_shingles_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=6.50)
    copper_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=30.00)
    rolled_roofing_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=3.00)
    solar_shingles_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=20.00)

    bur_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=3.50)
    epdm_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=4.50)
    modified_bitumen_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=4.50)
    pvc_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=6.50)
    tpo_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)
    green_roof_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=12.00)
    comm_metal_price_low = models.DecimalField(max_digits=6, decimal_places=2, default=6.00)

    bur_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)
    epdm_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=6.00)
    modified_bitumen_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=6.00)
    pvc_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=9.00)
    tpo_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=6.50)
    green_roof_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=20.00)
    comm_metal_price_high = models.DecimalField(max_digits=6, decimal_places=2, default=8.00)

    second_floor_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.05)
    third_floor_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.10)
    fourth_floor_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.15)
    max_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.20)

    asphalt_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
    composite_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.20)
    metal_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)
    clay_tile_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.75)
    concrete_tile_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)
    wood_shingles_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.75)
    copper_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=2.50)
    rolled_roofing_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
    solar_shingles_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)

    bur_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.75)
    epdm_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)
    modified_bitumen_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.60)
    pvc_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.75)
    tpo_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.60)
    green_roof_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)
    comm_metal_labor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=2.00)

    asphalt_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.10)
    composite_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.20)
    metal_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.40)
    clay_tile_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.30)
    concrete_tile_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.25)
    wood_shingles_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.20)
    copper_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)
    rolled_roofing_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.90)
    solar_shingles_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.50)

    bur_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.25)
    epdm_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
    modified_bitumen_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.10)
    pvc_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.30)
    tpo_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.20)
    green_roof_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=2.50)
    comm_metal_underlay_rate = models.DecimalField(max_digits=5, decimal_places=2, default=1.40)

    simple_complexity_multiplier_res = models.DecimalField(max_digits=4, decimal_places=2, default=1.00)
    moderate_complexity_multiplier_res = models.DecimalField(max_digits=4, decimal_places=2, default=1.05)
    complex_complexity_multiplier_res = models.DecimalField(max_digits=4, decimal_places=2, default=1.10)
    extreme_complexity_multiplier_res = models.DecimalField(max_digits=4, decimal_places=2, default=1.20)

    simple_complexity_multiplier_com = models.DecimalField(max_digits=4, decimal_places=2, default=1.00)
    moderate_complexity_multiplier_com = models.DecimalField(max_digits=4, decimal_places=2, default=1.07)
    complex_complexity_multiplier_com = models.DecimalField(max_digits=4, decimal_places=2, default=1.12)
    extreme_complexity_multiplier_com = models.DecimalField(max_digits=4, decimal_places=2, default=1.25)

    residential_permit_base = models.DecimalField(max_digits=6, decimal_places=2, default=500.00)
    residential_permit_per_sq = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)

    commercial_permit_base = models.DecimalField(max_digits=6, decimal_places=2, default=750.00)
    commercial_permit_per_sq = models.DecimalField(max_digits=5, decimal_places=2, default=15.00)

    def __str__(self):
        return f"Pricing for {self.client}"


class RoofQuote(models.Model):
    quote_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    business_user = models.ForeignKey(BusinessUser, on_delete=models.CASCADE, null=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=255)
    project_type = models.CharField(max_length=50, default="new_roof")
    building_type = models.CharField(max_length=50)
    stories = models.PositiveIntegerField(default=1)
    square_footage = models.FloatField(null=True, blank=True)
    final_area_sqft = models.FloatField(null=True, blank=True)

    material_type = models.CharField(max_length=50)
    roof_complexity = models.CharField(max_length=20)

    permission_for_quote = models.BooleanField(default=False)
    have_insurance = models.BooleanField(default=False)

    estimate_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estimate_middle = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    estimate_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.quote_id}"


class FinalQuote(models.Model):
    roof_quote = models.OneToOneField(RoofQuote, on_delete=models.CASCADE)
    pricing_config = models.ForeignKey(QuotePricing, on_delete=models.SET_NULL, null=True, blank=True)
    business_user = models.ForeignKey(BusinessUser, on_delete=models.SET_NULL, null=True, blank=True)

    building_type = models.CharField(max_length=50, null=True, blank=True)
    project_type = models.CharField(max_length=50, null=True, blank=True)
    material_type = models.CharField(max_length=50, null=True, blank=True)
    square_footage = models.PositiveIntegerField(null=True, blank=True)

    permit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    final_total_low = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    final_total_high = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    finalized = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FinalQuote {self.id} - {self.roof_quote.quote_id}"