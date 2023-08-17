from typing import Any, Iterable, Optional
from django.db import models
import uuid

# Esena Social Profile (Profile showed in social app)
class SocialProfile(models.Model):
    
    # Account Relation
    account = models.ForeignKey("accounts.Account", verbose_name="SP Account Owner", on_delete=models.CASCADE, null=True, related_name="social_profiles")

    # management_accounts = models.ManyToManyField("authz.ManagementAccount") user.auth0user.account.management_account.
    
    # Username max_length: 15 - min_lenght: 1 !!! UI CHECK AND SERIALIZER CHECK
    username = models.CharField(verbose_name="Username", max_length=30, unique=True)

    # SocialProfile Info
    display_name = models.CharField(verbose_name="Display Name", max_length=20, blank=True)
    verified_profile = models.BooleanField(verbose_name="Verified Profile", default=False)
    profile_picture = models.ImageField(verbose_name="Profile Picture", upload_to='social_profile/profile_pictures/', blank=True)
    biography_text = models.TextField(verbose_name="Biography Text", blank="true", max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)

    PROFILE_CHOICES = [
        ("Personal", "Personal"),
        ("Brand", "Brand"),
        ("Organization", "Organization"),
        ("Provider", "Provider"),
    ]
    profile_type = models.CharField(verbose_name="Social Profile Type", max_length=20, choices=PROFILE_CHOICES)
    
    #TO-DO: Social Profile settings? JSON? ?? 
    
    # FOLLOWING, BLOCK, PRIVATE, PENDING
    private_profile = models.BooleanField(verbose_name="Private Account", default=False)
    followers = models.ManyToManyField('self',blank=True,related_name='user_followers',symmetrical=False)
    following = models.ManyToManyField('self',blank=True,related_name='user_following',symmetrical=False)
    pending_request = models.ManyToManyField('self',blank=True,related_name='pandingRequest',symmetrical=False)
    blocked_user = models.ManyToManyField('self',blank=True,related_name='user_blocked',symmetrical=False)


    def __str__(self) -> str:
        return f"@{self.username} - {self.get_profile_type_display()} - {self.id}"




# # Esena Brand Social Profile (Aqui se guarda todo lo relacionado a este tipo de perfil) 
# class BrandSP(models.Model):
#     id = models.UUIDField(verbose_name="UUID", default=uuid.uuid4, primary_key=True)
#     social_profile = models.ForeignKey("social_profile.SocialProfile", verbose_name="Social Profile", on_delete=models.CASCADE)

# # Esena Organization Social Profile (Aqui se guarda todo lo relacionado a este tipo de perfil)
# class OrganizationSP(models.Model):
#     id = models.UUIDField(verbose_name="UUID", default=uuid.uuid4, primary_key=True)
#     social_profile = models.ForeignKey("social_profile.SocialProfile", verbose_name="Social Profile", on_delete=models.CASCADE)

# # Esena Provider Social Profile (Aqui se guarda todo lo relacionado a este tipo de perfil)
# class ProviderSP(models.Model):
#     id = models.UUIDField(verbose_name="UUID", default=uuid.uuid4, primary_key=True)
#     social_profile = models.ForeignKey("social_profile.SocialProfile", verbose_name="Social Profile", on_delete=models.CASCADE)