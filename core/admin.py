from django.contrib import admin
from .models import Skill, Project, Contact, SocialLink, Service, HomePageContent, AboutContent, Experience, Education, Testimonial, ContactInfo, ExpertiseArea, Stat, CybersecurityTip

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'is_active')
    search_fields = ('platform',)
    list_filter = ('is_active',)

admin.site.register(Service)

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'is_active')
    list_filter = ('version', 'is_active')

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'company')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('degree', 'institution')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('author_name', 'content')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'location', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email', 'phone', 'location')

@admin.register(ExpertiseArea)
class ExpertiseAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'created_at')
    search_fields = ('label',)

@admin.register(CybersecurityTip)
class CybersecurityTipAdmin(admin.ModelAdmin):
    list_display = ('tip', 'created_at')
    search_fields = ('tip',)