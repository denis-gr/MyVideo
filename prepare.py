from django.contrib.auth import get_user_model

from wagtail.models import Page, Site

from videos.models import MainPage


#create admin account
get_user_model().objects.create_superuser(username="admin", password="admin")

# delete default page
Page.objects.filter(title="Welcome to your new Wagtail site!").delete()

root_page = Page.objects.all()[0]

#create main page
main_page = MainPage()
main_page.title = "Main page"
root_page.add_child(instance=main_page)
root_page.save()

#create site
Site.objects.create(**{
    "hostname": "https://8000-denisgr-myvideo-x5gkonzz9sw.ws-eu87.gitpod.io/",
    "port": 8000,
    "site_name": "main", 
    "root_page": main_page, 
    "is_default_site": True, 
})
