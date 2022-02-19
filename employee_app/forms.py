from django import forms
from django.forms import inlineformset_factory
from . models import Profile, SkillSet


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class SkillSetModelForm(forms.ModelForm):
    class Meta:
        model = SkillSet
        fields = '__all__'


Skill_formset = inlineformset_factory(
    Profile, SkillSet, form=SkillSetModelForm, can_delete=False
)
