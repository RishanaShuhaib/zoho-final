from django.urls import path
from . import views

urlpatterns = [
    # -------------------------------Company section--------------------------------
    path('Company/Dashboard',views.company_dashboard,name='company_dashboard'),
    path('Company/Staff-Request',views.company_staff_request,name='company_staff_request'),
    path('Company/Staff-Request/Accept/<int:pk>',views.staff_request_accept,name='staff_request_accept'),
    path('Company/Staff-Request/Reject/<int:pk>',views.staff_request_reject,name='staff_request_reject'),
    path('Company/All-Staffs',views.company_all_staff,name='company_all_staff'),
    path('Company/Staff-Approval/Cancel/<int:pk>',views.staff_approval_cancel,name='staff_approval_cancel'),
    path('Company/Profile',views.company_profile,name='company_profile'),
    path('Company/Profile-Editpage',views.company_profile_editpage,name='company_profile_editpage'),
    path('Company/Profile/Edit/Basicdetails',views.company_profile_basicdetails_edit,name='company_profile_basicdetails_edit'),
    path('Company/Password_Change',views.company_password_change,name='company_password_change'),
    path('Company/Profile/Edit/Companydetails',views.company_profile_companydetails_edit,name='company_profile_companydetails_edit'),
    path('Company/Module-Editpage',views.company_module_editpage,name='company_module_editpage'),
    path('Company/Module-Edit',views.company_module_edit,name='company_module_edit'),
    path('Company/Renew/Payment_terms',views.company_renew_terms,name='company_renew_terms'),
    path('Company/Show-Godown-Details', views.show_godown_details, name='show_godown_details'),
    path('Company/Add-Godown/', views.add_godown, name='add_godown'),
    path('Company/Save-Item', views.save_item, name='save_item'),
    path('Company/Add-Unit', views.add_unit, name='add_unit'),
    path('Company/Show-Holidays/', views.show_holidays, name='show_holidays'),
    path('Company/Add-Holiday/', views.add_holiday, name='add_holiday'),
    path('Company/Holiday-Overview//', views.holiday_overview, name='holiday_overview'),
    path('Company/Godown-Overview/<int:godown_id>/', views.godown_overview, name='godown_overview'),
    path('Company/Edit_Godown/', views.edit_godown, name='edit_godown'),
    path('Company/Edit_Page/<int:godown_id>/', views.edit_page, name='edit_page'),
    path('Company/Delete_Godown/<int:godown_id>/', views.delete_godown, name='delete_godown'),
    path('Company/Add_Comment/<int:godown_id>/', views.add_comment, name='add_comment'),
    path('Company/Show_Comments/<int:godown_id>/', views.show_comments, name='show_comments'),
    path('Company/Edit_Comment/', views.edit_comment, name='edit_comment'),
    path('Company/Delete-Comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('Company/Get-Godown-history/', views.get_godown_history, name='get_godown_history'),
    path('Company/Get-Holiday-history/', views.get_holiday_history, name='get_holiday_history'),
    path('Company/Edit-Holidaypage/<int:holiday_id>/', views.edit_holidaypage, name='edit_holidaypage'),
    path('Company/Edit-Holiday/', views.edit_holiday, name='edit_holiday'),
    path('Company/Delete_Holiday/<int:holiday_id>/', views.delete_holiday, name='delete_holiday'),
    path('Company/Add_Commentholiday/', views.add_commentholiday, name='add_commentholiday'),
    path('Company/Get_Comments/', views.get_comments, name='get_comments'),
    path('Company/Toggle_Godown_Status/<int:godown_id>/<str:new_status>/', views.toggle_godown_status, name='toggle_godown_status'),
    




    # -------------------------------Staff section--------------------------------
    path('Staff/Dashboard',views.staff_dashboard,name='staff_dashboard'),
    path('Staff/Profile',views.staff_profile,name='staff_profile'),
    path('Staff/Profile-Editpage',views.staff_profile_editpage,name='staff_profile_editpage'),
    path('Staff/Profile/Edit/details',views.staff_profile_details_edit,name='staff_profile_details_edit'),
    path('Staff/Password_Change',views.staff_password_change,name='staff_password_change'),



    # -------------------------------Zoho Modules section--------------------------------
  
    
]