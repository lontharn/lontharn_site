from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile, UserExperience, ExperienceWork, UserEducation

import nested_admin


class UserProfileInline(nested_admin.NestedStackedInline):
    model               = UserProfile
    can_delete          = False
    verbose_name        = 'Personal Profile'
    verbose_name_plural = 'Personal Profiles'


class ExperienceWorkInline(nested_admin.NestedTabularInline):
    model               = ExperienceWork
    verbose_name        = 'Experience Work'
    verbose_name_plural = 'Experience Works'
    sortable_field_name = "position"
    extra = 1


class UserExperienceInline(nested_admin.NestedTabularInline):
    model               = UserExperience
    verbose_name        = 'Personal Experience'
    verbose_name_plural = 'Personal Experiences'
    sortable_field_name = "position"
    inlines = (ExperienceWorkInline, )
    extra = 1


class UserEducationInline(nested_admin.NestedTabularInline):
    model               = UserEducation
    verbose_name        = 'Personal Education'
    verbose_name_plural = 'Personal Educations'
    sortable_field_name = "position"
    extra = 1


class CustomUserAdmin(nested_admin.NestedModelAdmin):
    inlines = (
        UserProfileInline,
        UserExperienceInline,
        UserEducationInline
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

