from django.urls import path
from . import views
urlpatterns = [
  path('',views.index,name='index'),
  path('contact/',views.contact,name='contact'),
  path('login/',views.login,name='login'),
  path('registration/',views.registration,name='registration'),
  path('logout/',views.logout,name='logout'),
  path('change_password/',views.change_password,name='change_password'),
  path('seller_index/',views.seller_index,name='seller_index'),
  path('seller_change_password/',views.seller_change_password,name='seller_change_password'),
  path('seller_add_product/',views.seller_add_product,name="seller_add_product"),
  path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
  path('category/',views.category,name='category'),
  path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
  path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
  path('single_product/',views.single_product,name='single_product'),
  path('checkout/',views.checkout,name='checkout'),
  path('cart/',views.cart,name='cart'),
  path('wishlist/',views.wishlist,name='wishlist'),
  path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
  path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
  path('confirmation/',views.confirmation,name='confirmation'),
  path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
  path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
  path('blog/',views.blog,name='blog'),
  path('single_blog/',views.single_blog,name='single_blog'),
  path('tracking/',views.tracking,name='tracking'),
  path('seller_product_details/<int:pk>/',views.seller_product_details,name='seller_product_details'),
  path('profile/',views.profile,name='profile'),
  

]