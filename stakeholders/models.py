from django.db import models

class Stakeholder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, default="Users", help_text="Lucide Icon Name")
    image = models.ImageField(upload_to="stakeholders/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Solution Card"
        verbose_name_plural = "Solution Cards"

    def __str__(self):
        return self.title

class SolutionsPage(models.Model):
    """Model to control the static text of the Solutions Page via Admin"""
    hero_title = models.CharField(max_length=200, default="Our Solutions")
    hero_subtitle = models.TextField(default="Tailored ecosystems for every stakeholder in the financial world.")
    
    cta_title = models.CharField(max_length=200, default="Ready to join the ecosystem?")
    cta_text = models.TextField(default="Whether you are a client looking for experts or a professional seeking work, XpertAI has a place for you.")
    
    # Adding Button Fields to match Database Schema & Frontend
    cta_btn_primary = models.CharField(max_length=50, default="Sign Up Now")
    cta_btn_secondary = models.CharField(max_length=50, default="Contact Sales")
    
    class Meta:
        verbose_name = "Solutions Page Content"
        verbose_name_plural = "Solutions Page Content"

    def __str__(self):
        return "Solutions Page Settings"