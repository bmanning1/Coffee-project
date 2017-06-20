from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from home import views
from accounts.views import register, login, logout, edit_profile, delete_profile
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from coffees import views as coffee_views
from django.views.static import serve
from settings.dev import MEDIA_ROOT
from threads import views as forum_views
from blog import views as blog_views

# Coffee Project URLS

urlpatterns = [
    # Base URLS: Admin and Index
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index),

    # Basic URLS: About and Contact
    url(r'^about/$', views.get_about),
    url(r'^contact/$', views.get_contact),

    # Auth URLS: Register, Profile, Edit Profile, Delete Account, Login, Logout
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', coffee_views.user_purchases, name='profile'),
    url(r'^edit_profile/$', edit_profile, name='edit_profile'),
    url('^delete_profile$', delete_profile, name="delete_profile"),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    # Paypal URLS: Link to Paypal, Cancel, Return
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_views.paypal_return),
    url(r'^paypal-cancel/$', paypal_views.paypal_cancel),

    # Coffees URLS: Purchase and Prices
    url(r'^coffees/$', coffee_views.all_coffees),
    url(r'^prices/$', coffee_views.get_price),

    # Blog URLS: Search, List Blogs and individual Blog
    url(r'^blogresults/$', blog_views.blogresults),
    url(r'^blog/$', blog_views.post_list, name='post_list'),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # Forum URLS: Search, Subjects, Threads, New Thread, Singular Thread, New Post, Edit Post, Delete Post, Thread vote
    url(r'^results/$', forum_views.results),
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
]

if settings.DEBUG:
    # Debug mode
    import debug_toolbar

    urlpatterns += [
        url(r'^debug/', include(debug_toolbar.urls)),
    ]
