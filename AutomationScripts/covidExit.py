# to escape from a country affected by COVID-19

#!/usr/bin/env python


from json import loads
from requests import Session
from datetime import datetime
from difflib import get_close_matches
def getStats(date,province):
    with Session() as s:
        url = f"https://cdn.jsdelivr.net/gh/CSSEGISandData/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv"
        r = s.get(url)
        csv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ")).split('\n')
        headings = ['FIPS','Admin2','Province_State','Country_Region','Last_Update','Lat','Long_','Confirmed','Deaths','Recovered','Active','Combined_Key','Incident_Rate','Case_Fatality_Ratio']
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["Province_State"].upper().replace(' ','') == province.upper().replace(' ',''):
                    return dictionary
            except:
                continue
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["Country_Region"].upper().replace(' ','') == province.upper().replace(' ',''):
                    return dictionary
            except:
                continue
    return 0
def getCountry():
    with Session() as s:
        url = 'http://ip-api.com/json'
        r = s.get(url)
        locadiction = loads(r.content)
        return locadiction["country"]
def getPopulation(country):
    with Session() as s:
        url = f"https://restcountries.eu/rest/v2/name/{country}"
        r = s.get(url)
        try:
            countries = []
            for i in loads(r.content):
                countries.append(i["name"])
            theone = get_close_matches(country,countries, n=1)[0]
            c=0
            for i in loads(r.content):
                if i["name"] == theone:
                    break
                c+=1
            for i in loads(r.content)[c].keys():
                print((i).upper()," : ",loads(r.content)[c][i])
            return (loads(r.content)[c])
        except:
            return 0
def getAirport(province):
    with Session() as s:
        url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
        r = s.get(url)
        csv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ").replace('"','')).split('\n')
        headings = ['OA code','airport name','city','country','IATA','ICAO','lat','lon','elev','X','x','continent/city','type','source']
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["city"].upper().replace(' ','') == province.upper().replace(' ',''):
                    return [dictionary]
            except:
                continue
        national = []
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["country"].upper().replace(' ','') == province.upper().replace(' ',''):
                    national.append(dictionary)
            except:
                continue
        return national
def getProvinceIATA(iata):
    with Session() as s:
        url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
        r = s.get(url)
        csv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ").replace('"','')).split('\n')
        headings = ['OA code','airport name','city','country','IATA','ICAO','lat','lon','elev','X','x','continent/city','type','source']
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["IATA"].upper().replace(' ','') == iata.upper().replace(' ',''):
                    return [dictionary]
            except:
                continue
        national = []
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["IATA"].upper().replace(' ','') == iata.upper().replace(' ',''):
                    national.append(dictionary)
            except:
                continue
        return national[0]["country"]
def getAirlines(province):
    with Session() as s:
        url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat'
        r = s.get(url)
        csv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ").replace('"','')).split('\n')
        headings = ['OA Code','Airline Name','x','IATA','ICAO','Callsign','Country','X']
        national = []
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["Country"].upper().replace(' ','') == province.upper().replace(' ',''):
                    national.append(dictionary)
            except:
                continue
        return national
def getAirlinesIATA(iata):
    with Session() as s:
        province = getProvinceIATA(iata)[0]["country"]
        url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat'
        r = s.get(url)
        csv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ").replace('"','')).split('\n')
        headings = ['OA Code','Airline Name','x','IATA','ICAO','Callsign','Country','X']
        national = []
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["Country"].upper().replace(' ','') == province.upper().replace(' ',''):
                    national.append(dictionary["IATA"])
            except:
                continue
        return national
def getAirlineName(iata):
    with Session() as s:
        url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat'
        r = s.get(url)
        csv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ").replace('"','')).split('\n')
        headings = ['OA Code','Airline Name','x','IATA','ICAO','Callsign','Country','X']
        national = []
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["IATA"].upper().replace(' ','') == iata.upper().replace(' ',''):
                    national.append(dictionary["Airline Name"])
            except:
                continue
        return national
def getRoutesFrom(iata):
    with Session() as s:
        url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/planes.dat'
        r = s.get(url)
        typecsv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ").replace('"','')).split('\n')
        url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat'
        r = s.get(url)
        csv = (str(r.content).replace('\\r','\n').replace(r'\n','\n').replace("b'",'').replace("'",'').replace(", "," - ").replace('"','')).split('\n')
        headings = ['Operator IATA','Airline OA Code','From IATA','From OA Code','To IATA','To OA Code','X','x','aircraft types (separated by space)']
        shortlist = national = []
        for i in csv:
            try:
                dictionary = dict(zip(headings,i.split(',')))
                if dictionary["From IATA"].upper().replace(' ','') == iata.upper().replace(' ',''):
                    shortlist.append(dictionary)
            except:
                continue
        iataairlines = getAirlinesIATA(iata)
        for sk in shortlist:
            try:
                i = sk
                types = i["aircraft types (separated by space)"].split(' ')
                thetypes = []
                for j in types:
                    headings = ['Full Name', 'OA Code']
                    for x in typecsv:
                        try:
                            dictionary = dict(zip(headings,x.split(',')))
                            if dictionary["OA Code"].upper().replace(' ','') == j.upper().replace(' ',''):
                                thetypes.append(dictionary["Full Name"])
                        except:
                            continue
                namee = getAirlineName(sk["Operator IATA"])
                i.update({"Airframes" : thetypes, "Airline" : namee})
                del i['aircraft types (separated by space)']
                del i['Operator IATA']
                del i['x']
                del i['X']
                del i['Airline OA Code']
                del i['From OA Code']
                del i['To OA Code']
                national.append(i)
            except:
                pass
        return national
def covidExit(province=False):
    if province==False:
        province = getCountry()
    database = []
    date = str((int(datetime.today().strftime('%d'))))
    if len(date)==1:
        date = f"0{date}"
    month = str((int(datetime.today().strftime('%m'))))
    if len(month)==1:
        month = f"0{month}"
    year = str((int(datetime.today().strftime('%Y'))))
    changed = False
    c=0
    for iterator in range(1,11):
        c+=1
        if changed == False:
            diff = iterator
        else:
            diff = c
        thedate = str(int(date)-diff)
        if len(thedate)==1:
            thedate = f"0{thedate}"
        if int(thedate)<=0:
            changed = True
            month = str((int(datetime.today().strftime('%m')))-1)
            if len(month)==1:
                month = f"0{month}"
            thedate = date = 31
            c = 0
        if int(month)==0:
            year = str((int(datetime.today().strftime('%Y')))-1)
            month = 12
        data = (getStats(f"{month}-{thedate}-{year}",province))
        database.append(data)
    country = ''
    for i in database:
        if type(i)==dict:
            country = i["Country_Region"]
            break
    countrydet = getPopulation(country)
    population = countrydet["population"]
    demonym = countrydet["demonym"]
    i = 0
    while True:
        try:
            latest = database[i]["Confirmed"]
            seclatest = database[i+1]["Confirmed"]
            break
        except:
            i+=1
    avg = 0
    i = 0
    for i in database:
        try:
            avg += float(i["Confirmed"])
        except:
            pass
    print(f'''LATEST # OF COVID-19 CASES : {latest}
SECOND-LATEST # OF COVID-19 CASES : {seclatest}
HIKE IN # OF COVID-19 CASES IN 1 DAY : {abs(float(latest)-float(seclatest))}
AVERAGE # OF COVID-19 CASES FROM PAST 10 DAYS : {avg}''')
    availairports = getAirport(province)
    if availairports == []:
        availairports = getAirport(country)
    print('\nAIRPORTS THAT OPERATE IN THE REGION')
    for i in availairports:
        print(i["airport name"])
    availairlines = getAirlines(country)
    print('\nAIRLINES THAT ARE BASED ON THE COUNTRY')
    matchairlineavail = []
    for i in availairlines:
        matchairlineavail.append(i["Airline Name"])
        print(i["Airline Name"])
    availroutes = []
    for i in availairports:
        availroutes.append(getRoutesFrom(i["IATA"]))
    print(f'\n{demonym.upper()} AIRLINES DEPARTING FROM THE REGION/COUNTRY')
    for i in availroutes[0]:
        try:
            for tryline in i['Airline']:
                if tryline in matchairlineavail:
                    break
            print(f"{tryline}  from  {i['From IATA']}  to  {i['To IATA']} in aircraft(s)  {','.join(i['Airframes'])}")
        except:
            continue
    print(f'\nAIRLINES DEPARTING FROM THE REGION/COUNTRY')
    for i in availroutes[0]:
        try:
            print(f"{i['Airline'][0]}  from  {i['From IATA']}  to  {i['To IATA']} in aircraft(s)  {','.join(i['Airframes'])}")
        except:
            continue
            

covidExit('Oman')
