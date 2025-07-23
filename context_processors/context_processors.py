from home.models import SocialMedia , CustomerClub
from shop.models import CategoryParent
from contactus.models import ContactInfo

def context(request):
    links = SocialMedia.objects.all()
    category_parent = CategoryParent.objects.all()
    contact_info = ContactInfo.objects.all()
    return {"links": links , 'category_parent':category_parent , 'contact_info':contact_info}

