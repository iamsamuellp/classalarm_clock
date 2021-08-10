


class alarm_clock:
    # ============== Constructor========
    def __init__(self , name, time,):
        self.name = name
        self.current_time = "12:30"
        self.on_button = True
        self.alarm_time = time
            #   Methods

    def alarm_set_time(self):
        self.alarm_set_time = input("set alarm time here")
        self.alarm_set_time = self.alarm_set_time
        print("Alarm time:" + str(self.alarm_set_time))

    def button_on_off(self):
            self.button_on_off = input ("Please enter 'on' or 'off'.")
            if (self.button_on_off == False):
                self.button_on_off = "off"
            print ("Alarm is off.")

            if (self.button_on_off == True):
                self.button_on_off = "on"
            print("Alarm is on")

    def alarm_info(self):
            print( "Alarm Name: " + str(self.name))
            print("Alarm Time: " + str(self.alarm_time))
            print ("The alarm is " + str(self.on_button))
            print("The current time is: "+ str(self.current_time)) 

