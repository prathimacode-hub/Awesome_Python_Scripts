from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date,datetime,timedelta
from pyowm.owm import OWM
from ipregistry import IpregistryClient


today = datetime.now()
api_key_owm='your_API_key_for OWM'# get your API key from https://home.openweathermap.org/
owm = OWM(api_key_owm)
mgr = owm.weather_manager()
api_key_ipregistry="Your_API_key_for ipregistry" #get your API key from https://ipregistry.co/

def ipinfo():
    #to get the IP address of the user
    client = IpregistryClient(api_key_ipregistry)  
    ipInfo = client.lookup() 
    x=ipInfo.location
    latitude=x['latitude']
    longitude = x['longitude']
    location=x['city']+","+x['region']['name']+","+x['country']['name']
    return(latitude,longitude,location)
latitude, longitude, current_location = ipinfo()
one_call = mgr.one_call(lat=latitude, lon=longitude)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def current_weather1(one_call):
            #function to return current weather details
            current_humidity=str(one_call.current.humidity)
            current_precipitation_percentage=one_call.current.precipitation_probability
            if(type(current_precipitation_percentage)==int or type(current_precipitation_percentage)==float):
                current_precipitation_percentage=current_precipitation_percentage*100
            current_status=str(one_call.current.status)
            current_temp = str(one_call.current.temperature('celsius')['temp'])
            current_temp_feel = str(one_call.current.temperature('celsius')['feels_like'])
            current_wind_speed= str(one_call.current.wnd['speed'])
            return(current_humidity,str(current_precipitation_percentage),current_status,current_temp,current_temp_feel,current_wind_speed)

        def forecastfunc(day,one_call):
            #function to return future forecasted weather details of user chosen date
            forecast_humidity = str(one_call.forecast_daily[day].humidity)
            forecast_precipitation_percentage = str(one_call.forecast_daily[day].precipitation_probability)
            forecast_status = str(one_call.forecast_daily[day].status)
            forecast_temp_min = str(one_call.forecast_daily[day].temperature('celsius')['min'])
            forecast_temp_max = str(one_call.forecast_daily[day].temperature('celsius')['max'])
            forecast_feelslike = one_call.forecast_daily[day].temperature('celsius')['feels_like_day']+ one_call.forecast_daily[day].temperature('celsius')['feels_like_eve']+ one_call.forecast_daily[day].temperature('celsius')['feels_like_morn']
            forecast_feelslike = str(round(forecast_feelslike/3,3))
            forecast_windspeed = str(one_call.forecast_daily[day].wnd['speed'])
            return(forecast_humidity,forecast_precipitation_percentage,forecast_status,forecast_temp_max,forecast_temp_min,forecast_feelslike)
        def button_Called():
            #function to present current weather feathers at user's location
            global one_call,current_location
            self.lineEdit.setText('')
            self.lineEdit.setPlaceholderText("default your location is considered")
            self.comboBox.setCurrentIndex(0)
            latitude, longitude, current_location = ipinfo()
            one_call = mgr.one_call(lat=latitude,lon=longitude)
            forecast_display_func('today')
        def do_action():
            global one_call,current_location
            if(not (user_input_loc:=self.lineEdit.text())==""):
                reg = owm.city_id_registry()
                list_of_loc = reg.locations_for(user_input_loc)
                try:
                    exact_loc = list_of_loc[0]
                    lat = exact_loc.lat
                    lon = exact_loc.lon
                    current_location = user_input_loc
                    one_call = mgr.one_call(lat=lat,lon=lon)
                except:
                    self.lineEdit.setText('city name not exact. Please enter correct name')
            else:
                one_call = mgr.one_call(lat=latitude, lon=longitude)
        def forecast_display_func(text1):
            #function to display the weather report 
            
            current_humidity,current_precipitation_percentage,current_status,current_temp,current_temp_feel,current_wind_speed= current_weather1(one_call)
            flag=True
            if(str((today+timedelta(days=3)).strftime("%Y-%m-%d"))==text1):
                day=3
            elif('tomorrow' in text1):
                day=1
            elif(str((today+timedelta(days=2)).strftime("%Y-%m-%d"))==text1):
                day=2
            else:
                flag=False
                self.textBrowser_2.clear()
                self.textBrowser_2.append('<div style="font: 12pt "Comic Sans MS"";><p>current humidity: '+current_humidity+'%'+'</p><p>current precipitation percentage: '+current_precipitation_percentage+'%'+'</p><p>current status: '+current_status+'</p><p>current temperature: '+current_temp+'°C'+'</p><p>current apparent feel temperature: '+current_temp_feel+'°C'+'</p><p>current wind speed: '+current_wind_speed+'Km/h'+'</p><p>at location: '+current_location+'</p>')
            if(flag):
                forecast_humidity,forecast_precipitation_percentage,forecast_status,forecast_temp_max,forecast_temp_min,forecast_feelslike= forecastfunc(day,one_call)
                self.textBrowser_2.clear()
                self.textBrowser_2.append('<div style="font: 12pt "Comic Sans MS"";><p>forecast humidity: '+forecast_humidity+'%'+'</p><p>forecast precipitation percentage: '+forecast_precipitation_percentage+'%'+'</p><p>forecast status: '+forecast_status+'</p><p>forecast maximum temperature: '+forecast_temp_max+'°C'+'</p><p>forecast minimum temperature: '+forecast_temp_min+'°C'+'</p><p>forecast average feel temperature: '+forecast_feelslike+'°C'+'</p><p>at location: '+current_location+'</p>')
        
        #code for GUI tempelate

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 685)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\weather icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 29))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setStyleSheet("border-radius: 12px;")
        self.lineEdit.setText("")
        self.lineEdit.returnPressed.connect(lambda: do_action())
        self.lineEdit.setPlaceholderText("default your location is considered")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['today: '+str(today.strftime("%Y-%m-%d")),'tomorrow: '+str((today+timedelta(days=1)).strftime("%Y-%m-%d")),str((today+timedelta(days=2)).strftime("%Y-%m-%d")),str((today+timedelta(days=3)).strftime("%Y-%m-%d"))])
        self.comboBox.activated[str].connect(forecast_display_func)
        
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(712, 120))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.pushButton_3.setStyleSheet("border-radius: 20px;background-image: url(Images\clear sky.jpg);font: 20pt \"MS Shell Dlg 2\";text-align:center;")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setAutoRepeatDelay(1)
        self.pushButton_3.setAutoRepeatInterval(1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.clicked.connect(button_Called)
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(29, 29))
        self.label_2.setMaximumSize(QtCore.QSize(100, 29))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_2.setAutoFillBackground(False)
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);background-image: url(clear sky.jpg);background-repeat: no-repeat;background-position: center;background-size: cover;display:flex;justify-content:center;align-items:center;width:70%;padding: 50px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 5, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "weather report"))
        self.label.setText(_translate("MainWindow", "Location"))
        self.pushButton_3.setText(_translate("MainWindow", "Weather Report"))
        self.label_2.setText(_translate("MainWindow", "Forecasting Day"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
