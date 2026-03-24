from django import forms

class RoofCostEstimatorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))

    building_type = forms.ChoiceField(choices=[
        ("residential", "Residential"),
        ("commercial", "Commercial"),
    ])

    approximate_sqft = forms.IntegerField(min_value=500, label="Approximate Roof Square Footage")
    stories = forms.IntegerField(min_value=1, max_value=10, initial=1)

    material_type = forms.ChoiceField(choices=[
        ("asphalt", "Asphalt"),
        ("composite", "Composite"),
        ("metal", "Metal"),
        ("clay_tile", "Clay Tile"),
        ("concrete_tile", "Concrete Tile"),
        ("wood_shingles", "Wood Shingles"),
        ("rolled_roofing", "Rolled Roofing"),
        ("solar_shingles", "Solar Shingles"),
        ("copper", "Copper"),
        ("bur", "BUR"),
        ("comm_metal", "Commercial Metal"),
        ("epdm", "EPDM"),
        ("modified_bitumen", "Modified Bitumen"),
        ("pvc", "PVC"),
        ("tpo", "TPO"),
        ("green_roof", "Green Roof"),
    ])

    roof_complexity = forms.ChoiceField(choices=[
        ("Simple", "Simple"),
        ("Moderate", "Moderate"),
        ("Complex", "Complex"),
        ("Extreme", "Extreme"),
    ])

    permission_for_quote = forms.TypedChoiceField(
        choices=((True, "Yes"), (False, "No")),
        coerce=lambda x: x == "True",
        widget=forms.RadioSelect,
        required=True,
    )

    have_insurance = forms.TypedChoiceField(
        choices=((True, "Yes"), (False, "No")),
        coerce=lambda x: x == "True",
        widget=forms.RadioSelect,
        required=True,
    )