import subprocess
import time
import main1 as sig1
import main1 as sig2



def algo():
    car_count1, people_count1 = sig1.run()
    car_count2, people_count2 = sig2.run()

    print(f"The number of cars at signal 1 {car_count1}")
    print(f"The number of cars at signal 2 {car_count2}")

    print(f"The number of pedestrians at signal 1 {people_count1}")
    print(f"The number of pedestrians at signal 2 {people_count2}")


    final_count = 0
    if car_count1 and car_count2 != 0:
        ratio = car_count1/car_count2

        if ratio > 1.5 and people_count1 < 7:
            green_signal = "Signal-1 => Green Signal, Signal-2 => Red Signal"
            final_count = car_count1 * 7
        elif ratio > 1.5 and people_count1 > 7:
            green_signal = "Signal-2 => Green Signal, Signal-1 => Red Signal"
            final_count = car_count2 * 7
        elif ratio < 1.5 and people_count2 > 7:
            green_signal = "Signal-1 => Green Signal, Signal-2 => Red Signal"
            final_count = car_count2 * 7
        else:
            green_signal = "Signal-2 => Green Signal, Signal-1 => Red Signal"
            final_count = car_count2 * 7

    # Determine which subprocess gets the green signal
    else:
        if car_count1 > car_count2:
            green_signal = "Signal-1 => Green Signal, Signal-2 => Red Signal"
            final_count = car_count1 * 7
        elif car_count1 < car_count2:
            green_signal = "Signal-2 => Green Signal, Signal-1 => Red Signal"
            final_count = car_count2 * 7
        else:
            green_signal = "same number of cars"
            final_count = 30
    # Print the signals
    print(green_signal)

    return final_count

while(True):
    final_count = algo()
    start_time = time.time()
    time.sleep(final_count)
    end_time = time.time()
