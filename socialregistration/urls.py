"""

Updated on 19.12.2009

@author: alen, pinda
"""
from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url('^setup/$', 'socialregistration.views.setup',
        name='socialregistration_setup'),

    url('^logout/$', 'socialregistration.views.logout',
        name='social_logout'),

    url('^disconnect/(?P<network>\d+)/(?P<object_type>\d+)/(?P<object_id>\d+)/$', 'socialregistration.views.disconnect', name='disconnect'),
)

# Setup Facebook URLs if there's an API key specified
if getattr(settings, 'FACEBOOK_API_KEY', None) is not None:
    urlpatterns = urlpatterns + patterns('',
        url('^facebook/login/$', 'socialregistration.views.facebook_login',
            name='facebook_login'),

        url('^facebook/connect/$', 'socialregistration.views.facebook_connect',
            name='facebook_connect'),

        url('^xd_receiver.htm', 'django.views.generic.simple.direct_to_template',
            {'template':'socialregistration/xd_receiver.html'},
            name='facebook_xd_receiver'),
    )

#Setup Twitter URLs if there's an API key specified
if getattr(settings, 'TWITTER_CONSUMER_KEY', None) is not None:
    oauth_data =  {
        'consumer_key'      : getattr(settings, 'TWITTER_CONSUMER_KEY', ''),
        'secret_key'        : getattr(settings, 'TWITTER_CONSUMER_SECRET_KEY', ''),
        'request_token_url' : getattr(settings, 'TWITTER_REQUEST_TOKEN_URL', ''),
        'access_token_url'  : getattr(settings, 'TWITTER_ACCESS_TOKEN_URL', ''),
        'authorization_url' : getattr(settings, 'TWITTER_AUTHORIZATION_URL', ''),
    }
    redirect_params = oauth_data.copy()
    redirect_params.update({ 'callback_url': 'twitter_callback'})

    callback_params = oauth_data.copy()
    callback_params.update({ 'callback_url': 'twitter'})


    urlpatterns += patterns('',
        url('^twitter/redirect/$', 'socialregistration.views.oauth_redirect', redirect_params,
            name='twitter_redirect'),

        url('^twitter/callback/$', 'socialregistration.views.oauth_callback', callback_params,
            name='twitter_callback'
        ),
        url('^twitter/$', 'socialregistration.views.twitter', name='twitter'),
    )

urlpatterns += patterns('',
    url('^openid/redirect/$', 'socialregistration.views.openid_redirect', name='openid_redirect'),
    url('^openid/callback/$', 'socialregistration.views.openid_callback', name='openid_callback')
)
