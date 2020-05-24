from django.urls import path

from acc import views

urlpatterns = [
    # accounting/ index page for accounting
    path('<int:userId>',views.index, name='acc_index'),

    # ex: /accounting/1(quarter)/2016(year)/1(user_id)
    path('<int:qtr>/<int:year>/<int:userId>',views.quartleyReport, name='acc_quartleyReport'),

    # ex: accounting/uploadFile
    path('uploadFile', views.uploadFile, name='acc_uploadFile'),

]
