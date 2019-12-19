from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home')
  , url(r'^login/', views.login, name='login')
  , url(r'^logout/', views.logout, name='logout')
  , url(r'^sign/', views.sign, name='sign')
  , url(r'^app/', views.main, name='main')
  , url(r'^newcontact/', views.add_contact, name='acontact')
  , url(
        r'^(?P<contact_id>[0-9]+)/detail/$'
      , views.contact_detail
      , name='detail'
    )
  , url(
        r'^(?P<phone_id>[0-9]+)/editphone/$'
      , views.edit_phone
      , name='ephone'
    )
  , url(
        r'^(?P<contact_id>[0-9]+)/apendphone/$'
      , views.add_phone
      , name='aphone'
    )
  , url(
        r'^(?P<contact_id>[0-9]+)/editcontact/$'
      , views.edit_contact
      , name='econtact'
    )
  , url(
        r'^(?P<phone_id>[0-9]+)/deletephone/$'
      , views.delete_phone
      , name='dphone'
    )
  , url(
        r'^(?P<contact_id>[0-9]+)/deletecontact/$'
      , views.delete_contact
      , name='dcontact'
    )
  , url(
        r'^(?P<contact_id>[0-9]+)/cfdelcontact/$'
      , views.delete_contact_confirmed
      , name='confdeluser'
    )
]
