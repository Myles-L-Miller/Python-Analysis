# In summary, the required conversions are as follows:

  # The `Name` column should be split into separate `First Name` and `Last Name` columns.

  # The `DOB` data should be re-written into `MM/DD/YYYY` format.

  # The `SSN` data should be re-written such that the first five numbers are hidden from view.

  # The `State` data should be re-written as simple two-letter abbreviations.



import os
import csv

#Read File
employee_data_csv = os.path.join("Instructions", "PyBoss", "employee_data.csv")

#Write File
results=open("Instructions/PyBoss/Output/new_employee_data.csv", "w")
results.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")


#Imported from https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


with open(employee_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
      
        EmpID=row[0]
        Name=row[1].split(" ")
        DOB=row[2].split("-")
        SSN=row[3].split("-")
        State=row[4]

        
        #results.write("214,Sarah,Simpson,12/04/1985,***-**-8166,FL\n")
        results.write(f"{EmpID},")
        results.write(f"{Name[0]},")
        results.write(f"{Name[1]},")
        results.write(f"{DOB[1]}/{DOB[2]}/{DOB[0]},")
        results.write(f"***-**-{SSN[2]},")
        results.write(f"{us_state_abbrev[State]}\n")