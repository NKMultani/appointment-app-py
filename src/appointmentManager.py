import appointment

class AppointmentManager():
    def __init__(self):
        self.__appointmentList = []

    def addAppointment(self, title, date, startTime, endTime):
        newAppointmentObj = appointment.AppointmentClass(title, date, startTime, endTime)
        self.__appointmentList.append(newAppointmentObj) 

    def printAppointments(self):
        for app in self.__appointmentList:
            print(app.title)
            print(app.date)
            print(app.startTime)
            print(app.endTime)    

    def removeAppointment(self, title):
        for app in self.__appointmentList:
            if app.title.lower() == title.lower():
                self.__appointmentList.remove(app)
                break
                

    