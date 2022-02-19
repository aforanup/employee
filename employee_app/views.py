from pyexpat import model
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, DetailView, UpdateView
from . models import Profile, SkillSet
from . forms import ProfileModelForm, SkillSetModelForm, Skill_formset


def HomePage(request):
    profile = Profile.objects.all()
    context = {"profiles": profile}
    return render(request, 'employee_app/index.html', context)


class EmployeeDetailView(DetailView):
    template_name = 'employee_app/details.html'
    model = Profile


class UpdateSkillView(UpdateView):
    template_name = 'employee_app/update_skill.html'
    model = SkillSet
    form_class = SkillSetModelForm

    def get_success_url(self):
        url = reverse_lazy('employee_detail', kwargs={
                           'pk': self.kwargs['profile_pk']})
        return url


class EmployeeView(TemplateView):
    template_name = "employee_app/employeeform.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'profile_form': ProfileModelForm(),
            'skill_formset': Skill_formset()
        })
        return context

    def post(self, request, *args, **kwargs):
        profile = ProfileModelForm(request.POST, request.FILES)
        skill_form = Skill_formset(request.POST)
        if profile.is_valid() and skill_form.is_valid():
            p = profile.save()
            form_set = skill_form.save(commit=False)
            for form in form_set:
                form.profile = p
                form.save()
            return HttpResponseRedirect(reverse_lazy('employee'))
        else:
            print(profile.errors)
            return render(request, self.template_name, context={'profile_form': profile, 'skill_formset': skill_form})


class EmployeeDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('index')
