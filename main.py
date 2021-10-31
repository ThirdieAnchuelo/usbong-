from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.app import MDApp
import pandas as pd
import numpy as np
import glob
import cv2 as cv
from kivy.uix.camera import Camera
import time
import requests
import shutil

Window.size = (310, 580)
width = 500
height = 400
dimension = (width, height)

help_str = '''
ScreenManager:   
    LoginRegisterScreen:
    LoginScreen:
    SignupScreen:
    MenuScreen:
    CameraGalleryScreen:
    CameraClick:
    GalleryScreen:
    InfoScreen:
    CreditScreen:
    ClayScreen:
    PeatyScreen:
    LoamScreen:
    SandyScreen:
#---------------------------------------------------------   
<MainScreen>:
    name:"main"
    MDLabel:
        id:username_info
        text:'Hello Main'
        font_style:'H1'
        halign:'center'                 
#--------------------------------------------------------- 
#this is the first page and this is the login and sign up section
<LoginRegisterScreen>:
    name:"loginregister"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
        Image:
            source: "title.png"
            pos_hint: {"center_x": .5, "center_y": .92}
        Image:
            source: "soilmainimage.png"
            pos_hint: {"center_x": .5, "center_y": .50}
        MDLabel:
            text: "                                   -Masanobu Fukuoka"
            font_size: "14sp"
            pos_hint: {"center_y": .76}
            halign:"center"
        MDLabel:
            text: "“The ultimate goal of farming is not the growing of crops, but the cultivation and perfection of human beings.”"
            font_size: "15sp"
            size_hint_x: .85
            pos_hint: {"center_x": .5,"center_y": .82}
            halign:"center"    
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "login"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5] 
        Button:
            text: "SIGNUP"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .09}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "signup"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5]                        
#-----------------------------------------------------------   
#This is the login screen 
<LoginScreen>:
    name:"login"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
        MDFloatLayout:
            Image:
                source: "title.png"
                pos_hint: {"center_x": .5, "center_y": .92}
        MDLabel:
            text: "Sign in to continue"
            font_size: "18sp"
            pos_hint: {"center_x": .6,"center_y": .79}
            color: rgba(135, 133, 193, 255)
        MDLabel:
            text: "Sign in to continue"
            font_size: "18sp"
            pos_hint: {"center_x": .6,"center_y": .79}
            color: rgba(135, 133, 193, 255)
        MDTextField:
            id:login_email
            pos_hint: {'center_y':0.6,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Email'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        MDTextField:
            id:login_password
            pos_hint: {'center_y':0.4,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Password'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'password'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
       #--------LOGIN BUTTON---------
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_press:
                app.login()
                app.username_changer() 
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5]
        MDLabel:
            text: "Don't have an account?"
            font_size:"13sp"
            pos_hint: {"center_x": .68,"center_y": .04}
            color: rgba(135,133,193,255)
        MDTextButton:
            text: "sign up"
            font_size: "13sp"
            pos_hint: {"center_x": .75, "center_y": .04}
            color:rgba(135, 133, 193, 255)
            on_release:
                root.manager.transition.direction ="down"
                root.manager.current ="signup"
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .1,"center_y": .04}
            user_font_size: "25sp"
            theme_text_color: "Custom"
            text_color: rgba (26, 24, 58, 255)
            on_release:
                root.manager.transition.direction ="right"
                root.manager.current ="loginregister"  
#-------------------------------------------------------------                            
<SignUpScreen>:
    name:"signup"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
        MDFloatLayout:
            Image:
                source: "title.png"
                pos_hint: {"center_x": .5, "center_y": .92}
        MDLabel:
            text: "Create the new account"
            font_size: "18sp"
            pos_hint: {"center_x": .7,"center_y": .80}
            color: rgba(135, 133, 193, 255)
     #---------------------User Name-------------------------
        MDTextField:
            id:signup_username
            pos_hint: {'center_y':0.65,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Username'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
     #-----------------EMAIL-----------------------
        MDTextField:
            id:signup_email
            pos_hint: {'center_y':0.53,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Email'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'email'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
      #---------------------password------------------------
        MDTextField:
            id:signup_password
            pos_hint: {'center_y':0.4,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Password'
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'password'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        Button:
            text: "SIGN UP"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .25}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_press:app.signup()
        MDTextButton:
            text: 'Already have an account'
            pos_hint: {'center_x':0.5,'center_y':0.17}
            color: rgba(135, 133, 193, 255)
            on_press:
                root.manager.current = 'login'
                root.manager.transition.direction = 'down'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .1,"center_y": .04}
            user_font_size: "25sp"
            theme_text_color: "Custom"
            text_color: rgba (26, 24, 58, 255)
            on_release:
                root.manager.transition.direction ="right"
                root.manager.current ="loginregister"
        MDLabel:
            text: "BACK"
            font_size:"13sp"
            pos_hint: {"center_x": .68,"center_y": .04}
            color: rgba(135,133,193,255)
#--------------------------------------------------------------
<MenuScreen>:
    name:"menu"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
        Image:
            source: "title.png"
            pos_hint: {"center_x": .5, "center_y": .92}
        Image:
            source: "detect.png"
            size_hint: (None, None)
            size: 80,80
            pos_hint: {"center_x": .1, "center_y": .70}
        Image:
            source: "info.png"
            size_hint: (None, None)
            size: 80,80
            pos_hint: {"center_x": .1, "center_y": .50}
        Image:
            source: "setting.png"
            size_hint: (None, None)
            size: 80,80
            pos_hint: {"center_x": .1, "center_y": .30}
        Button:
            text: "DETECT"
            size_hint: .66, .065
            pos_hint: {"center_x": .55, "center_y": .70}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "camgal"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5]
        Button:
            text: "INFORMATION"
            size_hint: .66, .065
            pos_hint: {"center_x": .55, "center_y": .50}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "info"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5]
        Button:
            text: "CREDITS"
            size_hint: .66, .065
            pos_hint: {"center_x": .55, "center_y": .30}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "credit"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[10]
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="loginregister"
    MDLabel:
        text: "LOGOUT"
        font_size:"13sp"
        pos_hint: {"center_x": .68,"center_y": .04}
        color: rgba(135,133,193,255)
#--------------------------------------------------------------
<CameraGalleryScreen>:
    name:"camgal"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
        Image:
            source: "title.png"
            pos_hint: {"center_x": .5, "center_y": .92}
        Image:
            source: "camera.png"
            size_hint: (None, None)
            size: 80,80
            pos_hint: {"center_x": .1, "center_y": .60}
        Image:
            source: "gallary.png"
            size_hint: (None, None)
            size: 80,80
            pos_hint: {"center_x": .1, "center_y": .45}
        Button:
            text: "CAMERA"
            size_hint: .66, .065
            pos_hint: {"center_x": .55, "center_y": .60}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "camera"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5] 
        Button:
            text: "GALLERY"
            size_hint: .66, .065
            pos_hint: {"center_x": .55, "center_y": .45}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "gallery"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5]
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="menu"
    MDLabel:
        text: "BACK"
        font_size:"13sp"
        pos_hint: {"center_x": .68,"center_y": .04}
        color: rgba(135,133,193,255)
#--------------------------------------------------------------
<CameraClick>:
    name:"camera"
    orientation: "vertical"
    Camera:
        id: camera
        allow_stretch: True
        play: True
        canvas.before:
            PushMatrix:
            Rotate:
                origin:root.width/2, root.height/2
        canvas.after:
            PopMatrix:
    Button:
        text: 'Capture'
        size_hint_y: None
        pos_hint: {"center_y": .20}
        height: '48dp'
        on_press : 
            app.capture_image(self,*args)
    Button:
        text: 'back'
        size_hint_y: None
        pos_hint: {"center_y": .10}
        height: '48dp'
        on_press :
            root.manager.transition.direction ="right"
            root.manager.current ="camgal"
#-------------------------------------------------------
<GalleryScreen>:
    name:"gallery"
    id:model_layout
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
    MDBoxLayout:
        orientation: "vertical"
        size: root.width,root.height
        padding:15
        spacing:15
        Image:
            id: my_image
            source: ""
        FileChooserIconView
            id:filechooser
            on_selection: model_layout.selected(filechooser.selection)
        MDRaisedButton:
            text: " TRESHOLDING "
            pos_hint: {"center_x": .55, "center_y": .60}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            pos_hint:{"center_x":0.5,"center_y":0}     
            on_press: root.tresholding()
        MDRaisedButton:
            text: "          CNN          "
            pos_hint: {"center_x": .55, "center_y": .60}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            pos_hint:{"center_x":0.5,"center_y":0}     
            on_press: root.cnn()
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="camgal"
#-------------------------------------------------------
<InfoScreen>:
    name:"info"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
        Image:
            source: "title.png"
            pos_hint: {"center_x": .5, "center_y": .92}
        Button:
            text: "CLAY"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .68}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "clay"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5] 
        Button:
            text: "PEATY"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .55}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "peaty"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[5]
        Button:
            text: "LOAM"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .42}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "loam"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[10]
        Button:
            text: "SANDY"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .29}
            background_color: rgba(255, 147, 0, 255)
            color:rgba(255, 147, 0, 255)
            on_release:
                root.manager.transition.direction ="left"
                root.manager.current = "sandy"
            canvas.before:
                Color:
                    rgb: rgba(255, 147, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius:[10]
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="menu"
    MDLabel:
        text: "Back"
        font_size:"13sp"
        pos_hint: {"center_x": .68,"center_y": .04}
        color: rgba(135,133,193,255)
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="menu"
#--------------------------------------------------------------
<CreditScreen>:
    name:"credit"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1
        MDLabel:
            bold: True
            text: "USBONG: Soil Viability Classifier using Binary Thresholding and CNN Technique."
            font_size: "23sp"
            pos_hint: {"center_y": .83}
            halign:"center"
            color: rgba(240,230,140,255)
        MDLabel:
            text: ("A Mobile based application written by four graduating students namely:")
            font_size: "16sp"
            pos_hint: {"center_y": .65}
            halign:"center"
            color: rgba(135, 133, 193, 255)
        MDLabel:
            bold: True
            text: ("Anchuelo Victoriano III")
            font_size: "18sp"
            pos_hint: {"center_y": .55}
            halign:"center"
            color: rgba(255, 255, 255, 255)
        MDLabel:
            bold: True
            text: ("Fabian Abraham")
            font_size: "18sp"
            pos_hint: {"center_y": .50}
            halign:"center"
            color: rgba(255, 255, 255, 255)
        MDLabel:
            bold: True
            text: ("Mallabo Salvacion")
            font_size: "18sp"
            pos_hint: {"center_y": .45}
            halign:"center"
            color: rgba(255, 255, 255, 255)
        MDLabel:
            bold: True
            text: ("Martinez Katrina")
            font_size: "18sp"
            pos_hint: {"center_y": .40}
            halign:"center"
            color: rgba(255, 255, 255, 255) 
        MDLabel:
            text: ("Performed using Pycharm that mainly composed of Python Programs with the goal of classifying soil type by the use of Binary Thresholding and Soil Fertility by using CNN.")
            font_size: "16sp"
            pos_hint: {"center_y": .25}
            halign:"center"
            color: rgba(135, 133, 193, 255)
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="menu"
#-----------------------------------------------------------
<ClayScreen>:
    name:"clay"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1        
        orientation: "vertical"
        size: root.width,root.height
        padding:15
        spacing:15
        Image:
            source: "Clay.jpeg"
            pos_hint: {"center_x": .5, "center_y": .88}    
    MDLabel:
        bold: True
        text: "Clay Soil"
        color: rgba(240,230,140,255)
        pos_hint: {"center_x": .54, "center_y": .68}
        valign: 'top'
        font_size: '20sp'
    MDLabel:
        text: ("Clay soils are the heaviest of soil types and are often considered the hardest to work with. They hold onto water and often take longer to warm in the spring. Soil compaction and cracking is also a big risk of clay soils. Ultimately this doesn’t just look ugly. It also keep plant roots from breaking through hard layers of clay. Unlike sandy soils, clay soils are rich with nutrients! by using it, nutrients are stored for much longer and have a tendency not to leech away.")
        font_size: "13sp"
        pos_hint: {"center_y": .53}
        halign:"center"
        color: rgba(255, 255, 255, 255)  
    MDLabel:
        bold: True
        text: "Advantages"
        font_size: '20sp'
        theme_text_color: 'Custom'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .36}
        halign:"left"
    MDLabel:
        text: "Clay soils hold onto nutrients so the plant has the food it needs and Great for growing things that need a lot of water"
        font_size: "13sp"
        theme_text_color: 'Custom'
        pos_hint: {"center_y": .29}
        halign:"center"
        color: rgba(255, 255, 255, 255)   
    MDLabel:
        bold: True
        text: "Disadvantages"
        theme_text_color: 'Custom'
        font_size: '20sp'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .21}
        halign:"left"  
    MDLabel:
        text: "Holds onto water, slow to drain ,Slow to warm in the spring, Compacts easily and Tends to be alkaline "
        theme_text_color: 'Custom'
        font_size: "13sp"
        pos_hint: {"center_y": .14}
        halign:"center"
        color: rgba(255, 255, 255, 255)
    MDLabel:
        text: "Back"
        font_size:"13sp"
        pos_hint: {"center_x": .68,"center_y": .04}
        color: rgba(135,133,193,255)
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="info"
#-----------------------------------------------------------
<PeatyScreen>:
    name:"peaty"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1        
        orientation: "vertical"
        size: root.width,root.height
        padding:15
        spacing:15
        Image:
            source: "peaty.png"
            pos_hint: {"center_x": .5, "center_y": .88}    
    MDLabel:
        bold: True
        text: "Peaty Soil"
        color: rgba(240,230,140,255)
        pos_hint: {"center_x": .54, "center_y": .73}
        valign: 'top'
        font_size: '20sp'
    MDLabel:
        text: ("peat is a soil material consisting of partially decomposed organic matter, found mainly in swamps and bogs in various parts of the northern temperate zone but also in some semitropical and tropical regions. Peat is formed by the slow decay of successive layers of aquatic and semiaquatic plants, e.g., sedges, reeds, rushes, and mosses, and is the earliest stage of transition from compressed plant growth to the formation of coal.")
        font_size: "13sp"
        pos_hint: {"center_y": .58}
        halign:"center"
        color: rgba(255, 255, 255, 255)  
    MDLabel:
        bold: True
        text: "Advantages"
        font_size: '20sp'
        theme_text_color: 'Custom'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .43}
        halign:"left"
    MDLabel:
        text: "In general they easily become waterlogged and are usually acidic so you will not be able to grow lime loving plants. The acidity also means that they support only a limited range of beneficial soil organisms."
        font_size: "13sp"
        theme_text_color: 'Custom'
        pos_hint: {"center_y": .34}
        halign:"center"
        color: rgba(255, 255, 255, 255)   
    MDLabel:
        bold: True
        text: "Disadvantages"
        theme_text_color: 'Custom'
        font_size: '20sp'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .24}
        halign:"left"  
    MDLabel:
        text: "They are potentially very fertile and can be cultivated quite intensively. The addition of lime to selected areas will enable you to grow fruit and vegetables. You can make the most of your ornamental garden by growing the many beautiful acid loving plants. "
        theme_text_color: 'Custom'
        font_size: "13sp"
        pos_hint: {"center_y": .15}
        halign:"center"
        color: rgba(255, 255, 255, 255)
    MDLabel:
        text: "Back"
        font_size:"13sp"
        pos_hint: {"center_x": .68,"center_y": .04}
        color: rgba(135,133,193,255)
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="info"
#-----------------------------------------------------------
<LoamScreen>:
    name:"loam"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1        
        orientation: "vertical"
        size: root.width,root.height
        padding:15
        spacing:15
        Image:
            source: "loamy.jpeg"
            pos_hint: {"center_x": .5, "center_y": .88}    
    MDLabel:
        bold: True
        text: "Loam Soil"
        color: rgba(240,230,140,255)
        pos_hint: {"center_x": .54, "center_y": .72}
        valign: 'top'
        font_size: '20sp'
    MDLabel:
        text: ("Considered the most fertile of soil type, loamy soils are a combination of sandy, clay and silt particles. The clay and silt particles improve moisture retention while the sand minimizes compaction and improves drainage. Loamy soils don’t get dried out in the summer, but also don’t get water-logged in winter.")
        font_size: "13sp"
        pos_hint: {"center_y": .60}
        halign:"center"
        color: rgba(255, 255, 255, 255)  
    MDLabel:
        bold: True
        text: "Advantages"
        font_size: '20sp'
        theme_text_color: 'Custom'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .47}
        halign:"left"
    MDLabel:
        text: "Drought resistant due to water-holding capacity, Faster to warm up in the spring, compared to clay , Can hold nutrients, making soils fertile and a Good infiltration of air and water"
        font_size: "13sp"
        theme_text_color: 'Custom'
        pos_hint: {"center_y": .38}
        halign:"center"
        color: rgba(255, 255, 255, 255)   
    MDLabel:
        bold: True
        text: "Disadvantages"
        theme_text_color: 'Custom'
        font_size: '20sp'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .28}
        halign:"left"  
    MDLabel:
        text: "Depending on how your soil was formed, some loamy soils can contain stones that may affect harvesting of some crops. "
        theme_text_color: 'Custom'
        font_size: "13sp"
        pos_hint: {"center_y": .19}
        halign:"center"
        color: rgba(255, 255, 255, 255)
    MDLabel:
        text: "Back"
        font_size:"13sp"
        pos_hint: {"center_x": .68,"center_y": .04}
        color: rgba(135,133,193,255)
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="info"
#-----------------------------------------------------------
<SandyScreen>:
    name:"sandy"
    MDFloatLayout:
        md_bg_color:56/255,40/255,81/255,1        
        orientation: "vertical"
        size: root.width,root.height
        padding:15
        spacing:15
        Image:
            source: "Sandy.jpeg"
            pos_hint: {"center_x": .5, "center_y": .88}    
    MDLabel:
        bold: True
        text: "Sandy Soil"
        color: rgba(240,230,140,255)
        pos_hint: {"center_x": .54, "center_y": .68}
        valign: 'top'
        font_size: '20sp'
    MDLabel:
        text: ("Sandy soils are light and gritty to the touch. Because sandy soils have large particles, they dry out quickly, are often low in nutrients and acidic. Both water and fertilizer have a tendency to leach out of the soil - escaping to waterways before the plant can utilize them.")
        font_size: "13sp"
        pos_hint: {"center_y": .57}
        halign:"center"
        color: rgba(255, 255, 255, 255)  
    MDLabel:
        bold: True
        text: "Advantages"
        font_size: '20sp'
        theme_text_color: 'Custom'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .47}
        halign:"left"
    MDLabel:
        text: "Warms up quickly in the spring"
        font_size: "13sp"
        theme_text_color: 'Custom'
        pos_hint: {"center_x": .54,"center_y": .42}
        halign:"left"
        color: rgba(255, 255, 255, 255)   
    MDLabel:
        bold: True
        text: "Disadvantages"
        theme_text_color: 'Custom'
        font_size: '20sp'
        text_color: (240,128,128)
        pos_hint: {"center_x": .54,"center_y": .35}
        halign:"left"  
    MDLabel:
        text: "Dries out quickly in the summer , Nutrients and water often leech away especially with rainfall and Often acidic."
        theme_text_color: 'Custom'
        font_size: "13sp"
        pos_hint: {"center_y": .28}
        halign:"center"
        color: rgba(255, 255, 255, 255)
    MDLabel:
        text: "Back"
        font_size:"13sp"
        pos_hint: {"center_x": .68,"center_y": .04}
        color: rgba(135,133,193,255)
    MDIconButton:   
        icon: "arrow-left"
        pos_hint: {"center_x": .1,"center_y": .04}
        user_font_size: "25sp"
        theme_text_color: "Custom"
        text_color: rgba (26, 24, 58, 255)
        on_release:
            root.manager.transition.direction ="right"
            root.manager.current ="info"
'''


class LoginRegisterScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class CameraGalleryScreen(Screen):
    pass


class CameraClick(Screen):
    pass


class GalleryScreen(Screen):
    def selected(self, filename):
        try:
            self.filename = filename
            self.ids.my_image.source = self.filename[0]
            self.path = self.ids.my_image.source = self.filename[0]
            string = filename[0]
            # print(string)
            self.src_dir = string
            dst_dir = f"gallery"
            for file in glob.iglob(self.src_dir):
                shutil.copy(file, dst_dir)
            # print("Copied to Uploaded images folder")
        except:
            pass

    def tresholding(self):

        # img = cv.imread(self.img_path)
        img = cv.imread(self.src_dir)
        # print(self.src_dir)

        back_button = MDFlatButton(text="Back", pos_hint={"center_x": 0.5, "center_y": 0.25},
                                   on_press=self.close_dialog)
        resized = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
        # print(resized.shape)
        # cv.imshow('output',resized)
        adjusted_image = cv.convertScaleAbs(resized, alpha=1, beta=-30)  # Adjusting the Brightness of the Image
        # cv.imshow("adjusted",adjusted_image)
        # Converting to grayscale
        gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
        # cv.imshow ('Gray',gray)
        blur = cv.GaussianBlur(gray, (1, 1), cv.BORDER_DEFAULT)  # BLUR
        ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
        # cv.imshow('Thresh',thresh)
        # print(thresh.shape)
        threshflat = thresh.flatten()
        # print(threshflat)
        # contours, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        # print(f'{len(contours)}contour(s) found!')
        i = 0
        x = 0
        y = 0
        # Looping to access the values of thresholded image
        for i in threshflat:
            if i == 0:
                x += 1  # black
            elif i == 255:
                y += 1  # white
        black = x
        white = y
        if (white >= 30 and white <= 71000) and (black >= 130000 and black <= 200000):

            self.dialog = MDDialog(title='TRESHOLDING',
                                   text="Type of soil detected:{}".format(
                                       "\n \n LOAM\n \nLoamy soil a relatively even mix of sand, silt and clay, feels fine-textured and slightly damp. It has ideal characteristics for gardening, lawns and shrubs"),
                                   size_hint=(0.9, 1),
                                   buttons=[back_button])
            self.dialog.open()
            # print("type of soils:")
            # print("loam")
        elif (white >= 28000 and white <= 200000) and (black >= 3000 and black <= 180000):
            self.dialog = MDDialog(title='TRESHOLDING',
                                   text="Type of soil detected:{}".format(
                                       "\n \n SANDY\n \nSand is a naturally occurring granular material composed of finely divided rock and mineral particles. A soil containing more than 85% sand-sized particles by mass "),
                                   size_hint=(0.9, 1),
                                   buttons=[back_button])
            self.dialog.open()
            # print("type of soils:")
            # print("sandy")
        # declaring global variables (are used later on)

    def cnn(self):
        img = cv.imread(self.src_dir)
        back_button = MDFlatButton(text="Back", pos_hint={"center_x": 0.5, "center_y": 0.25},
                                   on_press=self.close_dialog)
        clicked = False
        r = g = b = x_pos = y_pos = 0
        # Reading csv file with pandas and giving names to each column
        index = ["color", "color_name", "hex", "R", "G", "B"]
        csv = pd.read_csv('colors.csv', names=index, header=None)
        # calculate the average color of each row of our image
        avg_color_per_row = np.average(img, axis=0)
        # calculate the averages of our rows
        avg_colors = np.average(avg_color_per_row, axis=0)
        # avg_color is a tuple in BGR order of the average colors
        # but as float values
        # so, convert that array to integers
        int_averages = np.array(avg_colors, dtype=np.uint8)
        # create a new image of the same height/width as the original
        average_image = np.zeros((height, width, 3), np.uint8)
        # and fill its pixels with our average color
        average_image[:] = int_averages

        # function to calculate minimum distance from all colors and get the most matching color

        def get_color_name(R, G, B):
            global cname
            minimum = 100
            for i in range(len(csv)):
                d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
                if d <= minimum:
                    minimum = d
                    cname = csv.loc[i, "color_name"]
            return cname

        def draw_function(event, x, y, flags, param):
            if event == cv.EVENT_LBUTTONDOWN:
                global r, g, b, x_pos, y_pos, clicked
                clicked = True
                x_pos = x
                y_pos = y

        # finally, show it side-by-side with the original
        # cv.imshow("Avg Color", average_image)

        b, g, r = average_image[0, 0]
        r = int(r)
        g = int(g)
        b = int(b)

        text = get_color_name(r, g, b)
        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        # print("\ndetails about soil (base on color of soil):")
        self.dialog = MDDialog(title='COLOR DETECTION',
                               text=text, size_hint=(1.08, 0.75),
                               buttons=[back_button])
        self.dialog.open()
        # print(text)
        # print(f'avg_colors: {avg_colors}')
        # print(f'int_averages: {int_averages}')

    def close_dialog(self, obj):
        self.dialog.dismiss()

    pass


class InfoScreen(Screen):
    pass


class CreditScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class ClayScreen(Screen):
    pass


class PeatyScreen(Screen):
    pass


class LoamScreen(Screen):
    pass


class SandyScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginRegisterScreen(name="loginregister"))
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(MainScreen(name="main"))
sm.add_widget(SignupScreen(name="signup"))
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(CameraGalleryScreen(name="camgal"))
sm.add_widget(CameraClick(name="camera"))
sm.add_widget(GalleryScreen(name="gallery"))
sm.add_widget(InfoScreen(name="info"))
sm.add_widget(CreditScreen(name="credit"))
sm.add_widget(ClayScreen(name="clay"))
sm.add_widget(PeatyScreen(name="peaty"))
sm.add_widget(LoamScreen(name="loam"))
sm.add_widget(SandyScreen(name="sandy"))


class MainApp(MDApp):

    def build(self):
        global cam
        cam = Camera()
        self.title = 'USBONG APP'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.strng = Builder.load_string(help_str)
        self.url = "https://usbong2-d4d37-default-rtdb.firebaseio.com/.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signup').ids.signup_email.text
        signupPassword = self.strng.get_screen('signup').ids.signup_password.text
        signupUsername = self.strng.get_screen('signup').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            # print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            # print(to_database)
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('login').manager.current = 'login'
            cancel_btn_username_dialogue = MDFlatButton(text='ok', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Sign Up Success!', text='Thank you for sign up  \n you can login right now',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

    auth = 'fazSyO4TjZpwm1YfrtSS5csWIson04LX14fqcvsp'

    def login(self):
        loginEmail = self.strng.get_screen('login').ids.login_email.text
        loginPassword = self.strng.get_screen('login').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('menu').manager.current = 'menu'
        else:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid', text='incorrect password or username \n\n please try again',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

    def username_changer(self):
        if self.login_check:
            # self.strng.get_screen('main').ids.username_info.text = f"welcome {self.username}"
            # print("login success")
            cancel_btn_username_dialogue = MDFlatButton(text='ok', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Login Success!', text=f"welcome to the usbong app \n\n {self.username}",
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

    def capture_image(self, *args):
        global cam
        self.timestr = time.strftime("%Y%m%d_%H%M%S")
        cam.export_to_png("gallary/IMG_{}.png".format(self.timestr))
        # print("Captured")
        cancel_btn_username_dialogue = MDFlatButton(text='ok', on_release=self.close_username_dialog)
        self.dialog = MDDialog(title='Captured', text="your picture is saved in gallery section",
                               size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
        self.dialog.open()

    def close_username_dialog(self):
        self.dialog.dismiss()


if __name__ == '__main__':
    MainApp().run()

