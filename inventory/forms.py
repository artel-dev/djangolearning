from django.forms import ModelForm, inlineformset_factory
from .models import PickAndPack, PickAndPackLine


class PickAndPackForm(ModelForm):
    class Meta:
        model = PickAndPack
        fields = "__all__"


class PickAndPackLineForm(ModelForm):
    class Meta:
        model = PickAndPackLine
        fields = "__all__"


pick_and_pack_formset = inlineformset_factory(PickAndPack, PickAndPackLine, fields="__all__")
