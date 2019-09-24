from django.urls import path, include
from . import views

urlpatterns = [
    path('view-all/', views.home_view, name='home_view'),
    path('add/', views.addRegion, name='add_region'),
    path('update/<int:id>/', views.updateRegion, name='update_region'),
    path('view/<int:id>/', views.viewRegion, name='view_region'),
    path('delete/<int:id>/', views.deleteRegion, name='delete_region'),
    path('', views.dashboard, name='dashboard_view'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('View_all_employees/', views.empl_view, name='view_employee'),
    path('employee_details/<int:id>/', views.viewEmployee, name='employeeView'),
    path('update_employee/<int:id>/', views.updateEmployee, name='update_employee'),
    path('delete_employee/<int:id>/', views.deleteEmployee, name='delete_employee'),
]
