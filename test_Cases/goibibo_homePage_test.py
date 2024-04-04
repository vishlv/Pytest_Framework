import pytest



from selenium import webdriver as dr


def verify_page_title(launch_app,request):

    print(dr.title)
