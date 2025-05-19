from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Lucide icon name")
    proficiency = models.IntegerField(default=80)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    technologies = models.ManyToManyField(Skill)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('x', 'X'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Lucide icon name")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.platform

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Lucide icon name (e.g., 'code', 'brush')")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['title']

    def __str__(self):
        return self.title

class HomePageContent(models.Model):
    title = models.CharField(max_length=100, default="Hi, I’m Kevin")
    subtitle = models.CharField(max_length=100, default="A FREELANCE FULL STACK DEVELOPER")
    description = models.TextField(
        default="I build dynamic and scalable web applications, handling both front-end and back-end development. Crafting beautiful and functional web experiences with modern technology."
    )
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    cv_file = models.FileField(upload_to='cv_files/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    version = models.CharField(max_length=10, default='home1')

    def __str__(self):
        return f"{self.title} - {self.version}"

    class Meta:
        verbose_name = "Homepage Content"
        verbose_name_plural = "Homepage Contents"

class AboutContent(models.Model):
    name = models.CharField(max_length=100, default="Kevin")
    introduction = models.TextField(
        default="With over 4 years of experience in web development, I specialize in building scalable applications using modern technologies. I'm passionate about creating user-friendly interfaces and writing clean, efficient code."
    )
    personal_info = models.TextField(
        default="When I'm not coding, you can find me exploring new technologies, contributing to open-source projects, or sharing my knowledge through technical blog posts."
    )
    profile_image = models.ImageField(upload_to='about_images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    about = models.ForeignKey(AboutContent, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    about = models.ForeignKey(AboutContent, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Testimonial(models.Model):
    about = models.ForeignKey(AboutContent, on_delete=models.CASCADE, related_name='testimonials')
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)
    content = models.TextField()
    author_image = models.ImageField(upload_to='testimonial_images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Testimonial by {self.author_name}"

class ContactInfo(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Contact: {self.email}"

# New Models for Homepage Enhancements
class ExpertiseArea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Lucide icon name (e.g., 'code', 'shield')")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Stat(models.Model):
    label = models.CharField(max_length=100)  # e.g., "Projects Completed"
    value = models.IntegerField()  # e.g., 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label

class CybersecurityTip(models.Model):
    tip = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tip