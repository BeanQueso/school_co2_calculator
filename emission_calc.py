import sys
import pandas as pd
import csv
import os

#declare
co2_in_kilos = []
activities_and_emissions = []
emission = 0

def check_if_exist():
    if os.path.isfile('emission_sheet.csv') == False:
        starting_data = []
        df = pd.DataFrame(starting_data, columns = ['activity', 'emission'])
        df.to_csv("emission_sheet.csv", index = False)

#df stuff
check_if_exist()
headers = ["activity","emission"]

def select_and_calc():

    print('Select your activity: driving, flying, eating meat')

    activity = input()

    if activity.lower() == "driving":
        fuel_type = input("petrol, or diesel?: ")
        fuel_in_liters = input("Input the amount of fuel used in litres: ")

        if fuel_type.lower() == "petrol":
            emission = float(fuel_in_liters)*2.39
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+': '+str(emission)+' kilos of co2'
            activities_and_emissions.append(act_ems)
        elif fuel_type.lower() == "diesel":
            emission = float(fuel_in_liters)*2.62
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+': '+str(emission)+' kilos of co2'
            activities_and_emissions.append(act_ems)

        print(act_ems)

    if activity.lower() == "flying":
        aircraft_model = input("Aircraft model (no spaces, dashes/hyphens, etc): ")

        #boeing

        if aircraft_model.lower() == "boeing747":
            fuel_burn_l_h = 10500 
            time = input("length of flight in hours: ")
            av_passenger = 366 # average num of passenger - VERIFIED
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger # 2.4 kilos of co2 per litre of fuel burned
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+' kilos of co2'
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        if aircraft_model.lower() == "boeing737":
            fuel_burn_l_h = 2267 
            time = input("length of flight in hours: ")
            av_passenger = 150 # **ESTIMATE: 737 FITS 85 TO 215 PASSENGERS, AVERAGE = 150**
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)

        if aircraft_model.lower() == "boeing777":
            fuel_burn_l_h = 7150
            time = input("length of flight in hours: ")
            av_passenger = 350 # seats from 312 to 388 passengers, avg of those is 350
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)

        if aircraft_model.lower() == "boeing787":
            fuel_burn_l_h = 5400 # verified
            time = input("length of flight in hours: ")
            av_passenger = 292 # 787-8: 248, 787-10: 336, avg of that is 292
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        #airbus

        if aircraft_model.lower() == "a319":
            fuel_burn_l_h = 2909
            time = input("length of flight in hours: ")
            av_passenger = 124
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        if aircraft_model.lower() == "a320":
            fuel_burn_l_h = 3125
            time = input("length of flight in hours: ")
            av_passenger = 150
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)

        if aircraft_model.lower() == "a321":
            fuel_burn_l_h = 2508
            time = input("length of flight in hours: ")
            av_passenger = 185
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity +": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        if aircraft_model.lower() == "a330":
            fuel_burn_l_h = 5153 
            time = input("length of flight in hours: ")
            av_passenger = 273
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        if aircraft_model.lower() == "a350":
            fuel_burn_l_h = 5600
            time = input("length of flight in hours: ")
            av_passenger = 310 # 270 - 350 passengers, avg of those is 310
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            emission = round(emission, 3)
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)

        if aircraft_model.lower() == "a380":
            fuel_burn_l_h = 7250
            time = input("length of flight in hours: ")
            av_passenger = 555
            emission = (float(fuel_burn_l_h)*2.4*float(time))/av_passenger
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
    
    if activity.lower() == "eating meat":
        meat_type = input("what type of meat did you eat? (lamb, beef, pork, turkey, chicken): ")

        if meat_type.lower() == "lamb":
            kilos_bought = input("how many kilograms of lamb did you buy/eat?: ")
            emission = float(kilos_bought)*39.2
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)
            
            print(act_ems)
        
        if meat_type.lower() == "beef":
            kilos_bought = input("how many kilograms of beef did you buy/eat?: ")
            emission = float(kilos_bought)*27
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        if meat_type.lower() == "pork":
            kilos_bought = input("how many kilograms of pork did you buy/eat?: ")
            emission = float(kilos_bought)*27
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        if meat_type.lower() == "turkey":
            kilos_bought = input("how many kilograms of turkey did you buy/eat?: ")
            emission = float(kilos_bought)*10.9
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
        
        if meat_type.lower() == "chicken":
            kilos_bought = input("how many kilograms of chicken did you buy/eat?: ")
            emission = float(kilos_bought)*6.9
            co2_in_kilos.append(emission)
            act_ems = activity+": "+str(emission)+" kilos of co2"
            activities_and_emissions.append(act_ems)

            print(act_ems)
    
    emission_final = round(emission,2)
    new_row = [activity,emission_final]

    with open('emission_sheet.csv', 'a') as f:

        writer = csv.writer(f)

        writer.writerow(new_row)

select_and_calc()