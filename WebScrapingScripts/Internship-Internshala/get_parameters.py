def select_categories(category_list):
    final_params = []
    for category in category_list:
        category = category.strip()
        if '/' in list(category):
            category = category.replace('/','%2F')
            final_params.append(category.split(' ')[0])
        else:
            category = category.replace(' ','%20')
            final_params.append(category)

    final_params = ','.join(final_params)
    final_params+='-internship'
    return final_params

def select_locations(location_list):
    final_params = []
    for location in location_list:
        location = location.strip()
        location = location.replace(' ','%20')
        final_params.append(location)
    final_params = ','.join(final_params)
    final_params ='-in-'+final_params

    return final_params

def select_dates(start,duration):
    import datetime
    
    if len(start) != 0:
        year,month,day = map(int,start.split("-")) 
        start_date = '/start_date-'+str(datetime.date(year, month, day)).replace('-','')
    else:
        start_date= ''
    
    if len(duration) != 0:
        duration = '/duration-'+duration
    else:
        duration = ''
    return(start_date,duration)

if __name__ == "__main__":
    print("Run main.py file")
