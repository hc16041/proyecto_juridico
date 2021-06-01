
from django.contrib import admin
from django.urls import path, include,re_path
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login, LoginView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from Sistema_juridico.views import Inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Sistema_juridico.urls',)),
    path('inicio/',Inicio.as_view(),name='inicio'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout',logout_then_login,name='logout'),
    path('accounts/password_reset',PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_email.html'), name='password_reset'),
    path('accounts/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('accounts/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    
handler404 = 'Sistema_juridico.views.handler404'
handler403 = 'Sistema_juridico.views.handler403'