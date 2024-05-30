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
    print(f"Current Status: {status_message}\n")

# Main function to run the program
# Arguments: None
# Return value: None
def main():
    # Printing the program's welcome message
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    # Creating an instance of the Sensor class
    sensor = Sensor()
    while True:
        # Displaying the menu options
        print("Menu Options:")
        print("1 - Update traffic light color")
        print("2 - Update pedestrian detection")
        print("3 - Update vehicle detection")
        print("0 - End the program")
        
        try:
            # Asking the user for their choice
            choice = int(input("Enter your choice: "))
            if choice == 0:
                # Exiting the program if the user selects 0
                print("\nExiting the program.\n")
                break
            elif choice == 1:
                # Asking the user for the new traffic light color if they select 1
                status_value = input("Enter traffic light color (green, yellow, red): ").strip()
                if status_value in ["green", "yellow", "red"]:
                    # Updating the sensor status and printing the messages if the input is valid
                    sensor.update_status("traffic_light", status_value)
                    print_message(sensor)
                else:
                    # Printing an error message if the input is invalid
                    print("\nInvalid traffic light color. Please enter 'green', 'yellow', or 'red'.\n")
            elif choice == 2:
                # Asking the user for the pedestrian detection status if they select 2
                status_value = input("Is a pedestrian detected? (yes, no): ").strip()
                if status_value in ["yes", "no"]:
                    # Updating the sensor status and printing the messages if the input is valid
                    sensor.update_status("pedestrian", status_value)
                    print_message(sensor)
                else:
                    # Printing an error message if the input is invalid
                    print("\nInvalid pedestrian status. Please enter 'yes' or 'no'.\n")
            elif choice == 3:
                # Asking the user for the vehicle detection status if they select 3
                status_value = input("Is a vehicle detected? (yes, no): ").strip()
                if status_value in ["yes", "no"]:
                    # Updating the sensor status and printing the messages if the input is valid
                    sensor.update_status("vehicle", status_value)
                    print_message(sensor)
                else:
                    # Printing an error message if the input is invalid
                    print("\nInvalid vehicle status. Please enter 'yes' or 'no'.\n")
            else:
                # Printing an error message if the user selects an invalid menu option
                print("\nInvalid menu option. Please enter 0, 1, 2, or 3.\n")
        except ValueError:
            # Printing an error message if the user input is not a valid number
            print("Invalid input. Please enter a number for the menu option.")

# Ensuring the main function runs only if the script is executed directly
if __name__ == '__main__':
    main()
