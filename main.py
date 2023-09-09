import machine
import time
import urandom

# Global values
light_intensity = None
button_pressed = False
response_time = None

# Define the button, built-in LED pins, and ADC for the photoresistor
button = machine.Pin(2, machine.Pin.IN)
led = machine.Pin(25, machine.Pin.OUT)
adc = machine.ADC(0)

# Create or open the file for logging
with open('response_times.txt', 'w') as f:
    for i in range(10):  # Adjust the number of trials if needed
        # Reset values
        light_intensity = None
        button_pressed = False
        response_time = None
        
        # Wait for a random period of time between 1 to 5 seconds
        wait_time = urandom.randint(1, 5)
        time.sleep(wait_time)
        
        # Flash the built-in LED
        led.on()
        
        # Start the timer
        start_time = time.ticks_us()

        # Wait for the button to be pressed or for the light intensity to be above a threshold
        while not button_pressed:
            if button.value() == 1:
                button_pressed = True
                led.off()
                end_time = time.ticks_us()
                response_time = end_time - start_time

            # Read the light intensity
            light_intensity = adc.read_u16()
        
        # Write the data to the file
        f.write(f"{response_time},{light_intensity}\n")
        
        # Wait a bit before the next loop
        time.sleep(2)

print("Test completed! Data saved to response_times.txt.")
