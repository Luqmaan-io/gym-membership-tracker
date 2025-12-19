"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# my_project/urls.py - REPLACE ENTIRE FILE
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
import os
from django.views.static import serve  # ADD THIS IMPORT

# Import app views
from gym import views as index_views
from members import views as members_views
from memberships import views as memeberships_views
from attendance import views as attendance_views
from payments import views as payments_views

urlpatterns = [
    # ⚠️ DIRECT STATIC FILE SERVING - PUT THIS FIRST
    path('static/<path:path>', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'static'),
    }),
    
    # Your existing routes
    path('', include('about.urls')),
    path('gym/', index_views.index, name='index'),
    path('members/', include('members.urls')),
    path('memberships/', memeberships_views.memberships, name='memberships'),
    path('attendance/', attendance_views.attendance, name='attendance'),
    path('payments/', payments_views.payments, name='payments'),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

# REMOVE OR COMMENT OUT this block - we're serving directly above
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)