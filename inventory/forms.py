from django.forms import ModelForm, inlineformset_factory
from .models import PickAndPack, PickAndPackLine, Receive, ReceiveLine


class PickAndPackForm(ModelForm):
    class Meta:
        model = PickAndPack
        fields = "__all__"


class PickAndPackLineForm(ModelForm):
    class Meta:
        model = PickAndPackLine
        fields = "__all__"

class ReceiveForm(ModelForm):
    class Meta:
        model = Receive
        fields = "__all__"


class ReceiveLineForm(ModelForm):
    class Meta:
        model = ReceiveLine
        fields = "__all__"


pick_and_pack_formset = inlineformset_factory(PickAndPack, PickAndPackLine, fields="__all__")
receive_formset = inlineformset_factory(Receive, ReceiveLine, fields="__all__")
