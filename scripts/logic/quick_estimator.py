from decimal import Decimal
from main.models import QuotePricing

def calculate_quick_estimate(*, pricing: QuotePricing, building_type: str, material_type: str,
                             square_footage: int, stories: int, roof_complexity: str):
    D = Decimal
    sqft = D(str(square_footage))

    if building_type == "residential":
        material_low = D(getattr(pricing, f"{material_type}_price_low", 0))
        material_high = D(getattr(pricing, f"{material_type}_price_high", 0))
        labor_rate = D(getattr(pricing, f"{material_type}_labor_rate", 0))
        underlay_rate = D(getattr(pricing, f"{material_type}_underlay_rate", 0))
        profit_low = D(pricing.residential_profit_low_per_sqft)
        profit_high = D(pricing.residential_profit_high_per_sqft)

        if stories == 2:
            stories_mult = D(pricing.second_floor_multiplier)
        elif stories == 3:
            stories_mult = D(pricing.third_floor_multiplier)
        elif stories == 4:
            stories_mult = D(pricing.fourth_floor_multiplier)
        elif stories > 4:
            stories_mult = D(pricing.max_multiplier)
        else:
            stories_mult = D("1")

        complexity_map = {
            "Simple": D(pricing.simple_complexity_multiplier_res),
            "Moderate": D(pricing.moderate_complexity_multiplier_res),
            "Complex": D(pricing.complex_complexity_multiplier_res),
            "Extreme": D(pricing.extreme_complexity_multiplier_res),
        }
        complexity_mult = complexity_map.get(roof_complexity, D("1"))

        permit = D(pricing.residential_permit_base) + ((sqft / D("100")) * D(pricing.residential_permit_per_sq))

    else:
        material_low = D(getattr(pricing, f"{material_type}_price_low", 0))
        material_high = D(getattr(pricing, f"{material_type}_price_high", 0))
        labor_rate = D(getattr(pricing, f"{material_type}_labor_rate", 0))
        underlay_rate = D(getattr(pricing, f"{material_type}_underlay_rate", 0))
        profit_low = D(pricing.commercial_profit_low_per_sqft)
        profit_high = D(pricing.commercial_profit_high_per_sqft)

        stories_mult = D("1")

        complexity_map = {
            "Simple": D(pricing.simple_complexity_multiplier_com),
            "Moderate": D(pricing.moderate_complexity_multiplier_com),
            "Complex": D(pricing.complex_complexity_multiplier_com),
            "Extreme": D(pricing.extreme_complexity_multiplier_com),
        }
        complexity_mult = complexity_map.get(roof_complexity, D("1"))

        permit = D(pricing.commercial_permit_base) + ((sqft / D("100")) * D(pricing.commercial_permit_per_sq))

    total_low = ((material_low + labor_rate + underlay_rate + profit_low) * sqft * stories_mult * complexity_mult) + permit
    total_high = ((material_high + labor_rate + underlay_rate + profit_high) * sqft * stories_mult * complexity_mult) + permit

    return {
        "low": round(float(total_low), 2),
        "high": round(float(total_high), 2),
        "mid": round(float((total_low + total_high) / 2), 2),
        "permit": round(float(permit), 2),
    }