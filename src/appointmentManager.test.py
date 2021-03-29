import appointmentManager

appointmentManagerObj = appointmentManager.AppointmentManager()

appointmentManagerObj.addAppointment("app 1", "date 1", "start time 1", "end time 1")
appointmentManagerObj.addAppointment("app 2", "date 2", "start time 2", "end time 2")

appointmentManagerObj.printAppointments()

print("-----------------")

appointmentManagerObj.removeAppointment("app 2")

appointmentManagerObj.printAppointments()
