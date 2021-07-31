import Functions.GetParameters as gp
import datetime

def get_URL_params():
    final_params=''
    Error = True
    while Error:
        try:
            print('--------------------------------------------------------------------')
            other_params=list(map(int,input("Include Work From home?\nInclude Part-time?\nInternships for women?\nInternships with job offer?\n(Represent your choice with 1-True or 0-False separated by commas such as 1,0,0,1)\n\n").split(',')))
            if max(other_params) > 1 or min(other_params) < 0:
                raise ValueError

            category_list = list(map(str,input("Enter different categories separated by commas* (Required)\n").split(','))) #Example -> Web Development,Accounts,Acting
            location_list = list(map(str,input("Enter different locations separated by commas* (Required)\n").split(','))) #Example -> Mumbai,Delhi
            
            start = input('Enter start date in format (yyyy-mm-dd) or leave empty for current date\n') #Example -> 2020-9-3
            if(len(start)!=0):
                datetime.datetime.strptime(start,'%Y-%m-%d')
            
            duration = input("Enter maximum duration or leave empty for any duration\n")
            print('--------------------------------------------------------------------')
            Error = False
        except (ValueError,IndexError,TypeError):
            print("Error in input values, loading options again")
            Error = True
  
    if other_params[2] == 1:
        final_params += '/internships-for-women/'
    else:
        final_params += '/internships/'

    if other_params[0] == 1:
        final_params+= 'work-from-home-'

    start_date,max_duration = gp.select_dates(start,duration)

    final_params += gp.select_categories(category_list)
    final_params += gp.select_locations(location_list)
    final_params += max_duration
    final_params += start_date
    
    if other_params[1] == 1:
        final_params += '/part_time-true'

    if other_params[3] == 1:
        final_params += '/ppo-true'

    if other_params[0] == 1 or other_params[1] == 1: 
        final_params = final_params.replace('-internship','-jobs')
    
    return final_params

if __name__ == "__main__":
    print("Run main.py file")
     