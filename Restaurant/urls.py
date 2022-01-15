from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home' ),
    path('home_after/', home_after_login, name='home_after'),
    path('admin_panel/', AdminPanel.as_view(), name='admin_panel'), 
    path('admin_panel/add_category',AddCategory.as_view(), name = 'add_category'),
    path('admin_panel/food_list/edit_food/<int:pk>/',EditFood.as_view(), name = 'edit_food'),
    path('admin_panel/food_list/delete_food/<int:pk>/',DeleteFood.as_view(), name = 'delete_food'),
    path('menu_list/<int:pk>/', MenuList.as_view(), name='menu_list'),
    path('admin_panel/food_list/',  FoodList.as_view(), name='food_list'),
    
	path('cart/', cart, name="cart"),
    path("cart/delete_ordered_item/<int:pk>/",DeleteOrderedItem.as_view(),name = 'delete_ordered_item'),
    path("cart/edit_ordered_item/<int:pk>/",EditOrderedItem.as_view(),name = 'edit_ordered_item'),
	path('item/<int:pk>/', items, name="items"),
    # path('cart/menu_to_cart/', items, name='items'),

    # path('search/', autocompleteModel, name='search_bar'),
    path("signup_base/",SignupBase.as_view(), name = "signup_base"),
    path("signup_admin/",signup_admin,name = "signup_admin"),
    path("signup_manager/",signup_manager,name = "signup_manager"),
    path("signup_customer/",signup_customer,name = "signup_customer"),

    path('customer_panel/', CustomerPanel.as_view(), name='customer_panel'),
    path('customer_panel/edit_profile/<int:pk>/', CustomerEditProfile.as_view(), name='customer_edit_profile'),
    path('customer_panel/add_address/', CustomerAddAddress.as_view(), name='customer_add_address'),


    path('manager_penal/', ManagerPanel.as_view(), name='manager_panel'), 
    path('manager_penal/edit_manager_info/<int:pk>/', EditManagerInfo.as_view(), name='edit_manager_info'), 
    path('manager_penal/view_branch_info/<int:pk>/', ViewBranchInfo.as_view(), name='view_branch_info'), 
    path('manager_penal/edit_branch_info/<int:pk>/', EditBranchInfo.as_view(), name='edit_branch_info'), 
    path('manager_penal/view_branch_menu/<int:pk>/', ViewBranchMenu.as_view(), name='view_branch_menu'),
    path('manager_penal/edit_branch_menu/<int:pk>/', EditBranchMenu.as_view(), name='edit_branch_menu'),
    # path('manager_penal/create_branch_menu/<int:pk>/', CreateBranchMenu.as_view(), name='create_branch_menu'),
    path('manager_penal/create_branch_menu/', CreateBranchMenu.as_view(), name='create_branch_menu'),
    path('manager_penal/delete_branch_menu/<int:pk>/', DeleteBranchMenu.as_view(), name='delete_branch_menu'),


]



urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)