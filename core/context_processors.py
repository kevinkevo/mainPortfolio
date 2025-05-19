# your_app/context_processors.py
from .models import ContactInfo, SocialLink,AboutContent

def footer_context(request):
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    social_links = SocialLink.objects.filter(is_active=True)
    about_content = AboutContent.objects.filter(is_active=True).first()
    return {
        'footer_contact': contact_info,
        'footer_social_links': social_links,
        'footer_about': about_content,
    }