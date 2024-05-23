# input_processing.py
# Raakin Bhatti, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.).
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

# Definition of the Sensor class
class Sensor:
    # Initialization method: Initializes the sensor with default status values
    def __init__(self):
        # Setting default status values for the sensor attributes
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # Method to update the status of the sensor
    # Arguments:
    #   status_type (str): Type of status to update ('traffic_light', 'pedestrian', 'vehicle')
    #   status_value (str): New status value to set
    # Return value: None
    def update_status(self, status_type, status_value):
        # Updating the traffic_light attribute if the status type is 'traffic_light'
        if status_type == "traffic_light":
            self.traffic_light = status_value
        # Updating the pedestrian attribute if the status type is 'pedestrian'
        elif status_type == "pedestrian":
            self.pedestrian = status_value
        # Updating the vehicle attribute if the status type is 'vehicle'
        elif status_type == "vehicle":
            self.vehicle = status_value

    # Method to determine the action message based on the current sensor status
    # Arguments: None
    # Return value: str - Action message ('STOP', 'Proceed', 'Caution')
    def get_action_message(self):
        # Return "STOP" if the traffic light is red or a pedestrian or vehicle is detected
        if self.traffic_light == "red" or self.pedestrian == "yes" or self.vehicle == "yes":
            return "STOP"
        # Return "Proceed" if the traffic light is green and no pedestrian or vehicle is detected
        elif self.traffic_light == "green" and self.pedestrian == "no" and self.vehicle == "no":
            return "Proceed"
        # Return "Caution" if the traffic light is yellow and no pedestrian or vehicle is detected
        elif self.traffic_light == "yellow" and self.pedestrian == "no" and self.vehicle == "no":
            return "Caution"

    # Method to get a string representing the current status of the sensor
    # Arguments: None
    # Return value: str - Status message summarizing the sensor status
    def get_status(self):
        return f"Traffic light: {self.traffic_light}, Pedestrian: {self.pedestrian}, Vehicle: {self.vehicle}"

# Function to print the current action and status messages
# Arguments:
#   sensor (Sensor): An instance of the Sensor class
# Return value: None
def print_message(sensor):
    # Getting the action message from the sensor
    action_message = sensor.get_action_message()
    # Getting the status message from the sensor
    status_message = sensor.get_status()
    # Printing the action and status messages
    print(f"\nAction: {action_message}")
    print
