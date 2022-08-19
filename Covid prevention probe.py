import mysql.connector as co
import time

def create_database():
        mycon=co.connect(host="localhost",user="SCOPO",passwd="4425")
        mycursor=mycon.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS COVID")
create_database()
def reg_table():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425",database="COVID")
    mycursor=mycon.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS register(Rname varchar(50),Rphno varchar(20),Raddress varchar(50),Rmail char(40) ,Rocc varchar(30),Rtravel varchar(5),Rcovid varchar(5))")
reg_table()

def misc_tables():
        mycon=co.connect(host="localhost",user="SCOPO",passwd="4425",database="covid")
        mycursor=mycon.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS tester(Rphno varchar(20),symptoms varchar(3), existing_desease varchar(3),hold_breathe varchar(3))")
        
misc_tables()



def MAIN_MENU():
    print("\t\t...........................................................................")
    print("\t\t*****************Welcome to COVID-19 Prevention Prober*********************")
    print("\t\t...........................................................................")
    print("\n")
    print("n\t\t***********Registration PANNEL*************")
    print("1: Registration And COVID Analyser")
    print("2: Information about covid-19")
    print("3: News")
    print("4: Exit")
    print("\t\t-------------------------------------------------------")
    choi= int(input("Enter you choice: "))
        
    if choi==1:
        REGISTER()
    elif choi==2:
        INFORMATION()
    elif choi==3:
        news()
            
    elif choi==4:
        print("Thank you for using our service ")

    else:
        print("error: invalid choice try again...")
        conti=("press any key to return to main menu")



#REGISTER>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def REGISTER():
        print("\t\t...........................................................................")
        print("\t\t*****************Welcome to COVID-19 Prevention Prober*********************")
        print("\t\t...........................................................................")
        print("\n")
        print("n\t\t***********Registration PANNEL*************")
        print("1: Registration")
        print("2: Covid Analyser")
        print("3: Registration Details")
        print("4: Search")
        print("5: Deletion Of Record")
        print("6: Update Registration Record")
        print("7: Return")
        print("\t\t-------------------------------------------------------")
        choi= int(input("Enter you choice: "))
        
        if choi==1:
                register_me()
        elif choi==2:
                TESTER()
        elif choi==3:
                register_details()
        elif choi==4:
                register_search()
        elif choi==5:
                register_deletion()
        elif choi==6:
                register_update()
        elif choi==7:
                MAIN_MENU()
        else:
                print("error: invalid choice try again...")
                conti=("press any key to return to main menu")
#registration
def register_me():
    
        mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
        cursor=mycon.cursor()
        Rname=input('Enter your name: ')
        Rphno=int(input('Enter your phone number: '))
        Raddress=input('Enter your address: ')
        Rmail=input('Enter your email address: ')
        Rocc=input('Enter your Occupation: ')
        Rtravel=input('Have you travelled out the country in last 28days?(Y/N): ')
        Rcovid=input('have you ever been tested positive for covid-19?(Y/N): ')
        

        query="insert into register(Rname,Rphno,Raddress,Rmail,Rocc,Rtravel,Rcovid)values('{}','{}','{}','{}','{}','{}','{}')".format(Rname,Rphno,Raddress,Rmail,Rocc,Rtravel,Rcovid)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("\n")
        print("Record has been saved in registration table")
        print("\n")
        a=input("do you want to take the COVID-19 Analyzer?(yes/no)")
        if a=="yes":
                TESTER()
        
        else:
                print("thank you for registring")
                return


       
   
       
     

#registration_details

def register_details():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
    cursor=mycon.cursor()
    cursor.execute("select * from register")
    data = cursor.fetchall()
    for row in data:
        print(row)
    print("\n")
    time.sleep(1)
    REGISTER()
    


#search_register

def register_search():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
    cursor=mycon.cursor()
    phc=input('Enter phone no: ')
    st="select * from register where Rphno='%s'"%(phc)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)
    print("\n")
    time.sleep(1)
    REGISTER()
    

#delete_register
def register_deletion():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
    cursor=mycon.cursor()
    phc=int(input("Enter your no: "))
    st="delete from register where Rphno='%s'"%(phc)
    cursor.execute(st)
    mycon.commit()
    print("data deleted successfully")
    print("\n")
    time.sleep(1)
    REGISTER()

#update_register
def register_update():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
    cursor=mycon.cursor()
    print("1: Edit Name")
    print("2: Edit Address")
    print("3: Edit Email address")
    print("4: Return")
    print("\t\t------------------------------")
    choi=int(input("enter your choice: "))
    if choi==1:
        edit_Rname()
    elif choi==2:
        edit_Raddress()
    elif choi==3:
        edit_Rmail()
    elif choi==4:
        REGISTER()

    else:
            print("Error: Invalid Choice try again.....")
            conti="press any key to return to"

    
#edit_name
def edit_Rname():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
    cursor=mycon.cursor()
    phc=input("enter your phone no.: ")
    cn=input("enter your correct name: ")
    st="update register set Rname='%s'where Rphno='%s'"%(cn,phc)
    cursor.execute(st)
    mycon.commit()
    print("data has been changed")
    
    
#edit_address
def edit_Raddress():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
    cursor=mycon.cursor()
    phc=input('enter your phone no.: ')
    ca=input('enter your correct address: ')
    st="update register set Raddress='%s'where Rphno='%s'"%(ca,phc)
    cursor.execute(st)
    mycon.commit()
    print('data has been changed')

#edit email
def edit_Rmail():
    mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
    cursor=mycon.cursor()
    phc=input("enter your phone no.: ")
    ce=input("enter your correct Email address: ")
    st="update register set Raddress='%s'where Rphno='%s'"%(ce,phc)
    cursor.execute(st)
    mycon.commit()
    print("data has been changed")



import time

def TESTER():
                print('select you choice:')
                print('1.New user')
                print('2.Existing user')
                test=int(input('Enter your choice:'))
                if test==2:
                        print('Select your choice:')
                        print('1.Create new report')
                        print('2.Review existing report')
                        hello=int(input('Enter your choice:'))
                        if hello==1:
                                testing()
                        else:
                                mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
                                cursor=mycon.cursor()
                                cursor.execute("select * from tester")
                                data = cursor.fetchall()
                                for row in data:
                                        print(row)
                                REGISTER()
       
                else:
                         testing()
                
def testing():
                mycon=co.connect(host="localhost",user="SCOPO",passwd="4425", database="covid")
                cursor=mycon.cursor()

                Rphno=int(input('Enter your phone number: '))
                print("\1Are you experiencing any of the following symptoms?")
                print("\t1: Cough ")
                print("\t2: Fever")
                print("\t3: Difficulty in breathing")
                print("\t4: Loss of senses of smell and taste ")
                print("\t5: None of the above")
                symptoms=int(input('enter your choice:'))
                print("\n")
                if symptoms==5:
                        print("you have no covid symptoms so far")
                else:
                        print("you should take a covid-19 test and consult a doctor soon as possible")
               
                print("\n")
                print("Have you ever had any of the following:")
                print("\t1: Diabetes ")
                print("\t2: Hypertension")
                print("\t3: Lung disease")
                print("\t4: Heart disease")  
                print("\t5: Kidney disorder")
                print("\t6: None of the above")
                existing_desease=int(input('enter your choice: '))
                print("\n")
                if existing_desease==6:
                        print("you are at low risk ")
                else:
                        print("you are at high risk")
                print("\n")
                print("---------------------------")
                print("hold your breathe for 15sec")
                print("---------------------------")
                time.sleep(1)
                print("timer starts now...")
                time.sleep(1)
                sec=15
                for i in range(sec):
                        print((sec-i),end="..")
                        time.sleep(1)
                print('\n')
                hold_breathe=input('were you able to hold your breath for 15 sec??(Y/N)')
                print("\n")
                if hold_breathe=="no":
                         print("Which of the following apply to you?")
                         print("\t1: I have recently interacted or lived with someone who was")
                         print("\t   tested positive for covid-19")
                         print("\t2: Iam a healthcare worker and I examined a covid-19 confirmed")
                         print("\t   case without protective gear")
                         contact=input('enter your choice: ')
                         print("consult a doctor as analysis demonstrate that you are highly exposed to the virus. ")
                else:
                         print("stay healthy and follow social distancing")


                query="insert into tester(Rphno,symptoms,existing_desease,hold_breathe)values('{}','{}','{}','{}')".format(Rphno,symptoms,existing_desease,hold_breathe)
                cursor.execute(query)
                mycon.commit()
                mycon.close()
                cursor.close()
        
                print("Record has been saved in tester table")
                print("\n")
                print("\n")
                REGISTER()

#INFORMATION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def INFORMATION():
        print("\t\t...........................................................................")
        print("\t\t*****************Welcome to COVID-19 Prevention Prober*********************")
        print("\t\t...........................................................................")
        print("\n")
        print("n\t\t***********INFORMATION PANNEL*************")
        print("1: Orgin of COVID-19")
        print("2: How it spreads")
        print("3: Is it more dangerous than any other viruses?")
        print("4: Risk Factor ")
        print("5: return")
        print("\t\t-------------------------------------------------------")
        choi= int(input("enter you choice"))
        
        if choi==1:
            info_orgin()
        elif choi==2:
            info_spread()
        elif choi==3:
            info_dangerous()
        elif choi==4:
            info_risk()
        elif choi==5:
            MAIN_MENU()
        else:
            print("error: invalid choice try again...")
            conti=("press any key to return to main menu")



print("\t\t")

#orgin
def info_orgin():
    print("\t\t.........................................................................")
    print("\t\t**************----------ORGIN OF COVID-19----------**********************")
    print("\t\t.........................................................................")
    print("\n")
    print("\t\tThe recent outbreak began in Wuhan, a city in the Hubei province of China.")
    print("\t\tReports of the first COVID-19 cases started in December 2019.")
    print("\t\tCoronaviruses are common in certain species of animals, such as cattle and camels.")
    print("\t\tAlthough the transmission of coronaviruses from animals to humans is rare,")
    print("\t\tthis new strain likely came from bats, though one study suggests pangolins may be the origin.")
    print("\t\tSome reports trace the earliest cases back to a seafood and animal market in Wuhan.")
    print("\t\tIt may have been from here that SARS-CoV-2 started to spread to humans.")
    print("\n")
    print("\n")
    time.sleep(1)
    INFORMATION()


#How it spreads
def info_spread():
    print("\t\t.........................................................................")
    print("\t\t**************-----------HOW IT SPREADS?-----------**********************")
    print("\t\t.........................................................................")
    print("\n")
    print("\t\tSARS-CoV-2 spreads from person to person through close communities.")
    print("\n")
    print("\t\tWhen people with COVID-19 breathe out or cough, they expel tiny droplets that contain the virus.")
    print("\t\tThese droplets can enter the mouth or nose of someone without the virus, causing an infection to occur.")
    print("\n")
    print("\t\tThe most common way that this illness spreads is through close contact with someone who has the infection.")
    print("\t\t Close contact is within around 6 feet.")
    print("\n")
    print("\t\tThe disease is most contagious when a person’s symptoms are at their peak.")
    print("\t\tHowever it is possible for someone without symptoms to spread the virus. ")
    print("\t\tA new study suggests that 10% of infections are from people exhibiting no symptoms.")
    print("\t\tDroplets containing the virus can also land on nearby surfaces or objects.")
    print("\t\tOther people can pick up the virus by touching these surfaces or objects. ")
    print("\t\tInfection is likely if the person then touches their nose, eyes, or mouth.")
    print("\n")
    print("\t\tIt is important to note that COVID-19 is new, and research is still ongoing. ")
    print("\t\tThere may also be other ways that the new coronavirus can spread.")
    print("\n")
    print("\n")
    time.sleep(1)
    INFORMATION()




#Is it more dangerous than other viruses?
def info_dangerous():
    print("\t\t.........................................................................")
    print("\t\t********--------Is it more dangerous than other viruses?---------********")
    print("\t\t.........................................................................")
    print("\n")
    print("\t\tMost cases of COVID-19 are not serious. However, it can cause symptoms ")
    print("\t\tthat become severe, leading to death in some cases.become severe, ")
    print("\t\t leading to death in some cases.")
    print("\n")
    print("\t\tThe outbreak of COVID-19 has been sudden. This makes it difficult to")
    print("\t\testimate how often the disease becomes severe or the exact rate of ")
    print("\t\tmortality.")
    print("\n")
    print("\t\tOne report suggests that out of 1,099 people with confirmed cases in ")
    print("\t\tChina, around 16% became severe. Another report estimates that")
    print("\t\tabout 3.6% of the confirmed cases in China led to death.")
    print("\n")
    print("\t\tThese figures are likely to change as the situation evolves. However, they ")
    print("\t\t suggest that COVID-19 is more deadly than influenza. For example, ")
    print("\t\tseasonal influenza typically leads to death in less than 0.1% of cases.")
    print("\n")
    print("\t\tWhen testing becomes easier and more widespread, health experts will ")
    print("\t\thave a more accurate insight into the exact number of severe cases and ")
    print("\t\tdeaths.")
    print("\n")
    print("\t\tSARS is another type of coronavirus. It became a global pandemic in ")
    print("\t\t2002–2003. Around 9.6% of SARS cases led to death. However, ")
    print("\t\tCOVID-19 is more contagious, and it is already the cause of more deaths ")
    print("\t\tworldwide.")
    print("\n")
    print("\n")
    time.sleep(1)
    INFORMATION()

    
#Risk factor
def info_risk():
    print("\t\t.........................................................................")
    print("\t\t****************--------------RISK FACTOR----------------****************")
    print("\t\t.........................................................................")
    print("\n")
    print("\t\tSome factors can affect the risk of coming into contact with the virus, ")
    print("\t\twhile other factors can affect the risk of developing severe illness.")
    print("\n")
    print("\t\tThe risk of coming into contact with the virus depends on how far it has ")
    print("\t\tspread in a person’s local area.")
    print("\n")
    print("\t\tThe WHO state that the risk of developing COVID-19 is still low for most ")
    print("\t\tpeople. However, this is changing as the virus spreads — particularly in ")
    print("\t\tEurope and the United States.")
    print("\n")
    print("\t\tThe risk is higher for anyone in close contact with people who have ")
    print("\t\tCOVID-19, such as healthcare workers. Viruses can also spread more in")
    print("\t\tcertain areas, such as highly populated cities.")
    print("\n")
    print("\t\tOlder adults are most at risk of severe illness, as are people with the ")
    print("\t\tfollowing chronic health conditions:")
    print("\t\t\t1)serious heart conditions, such as heart failure, coronary artery ")
    print("\t\t\t  disease, or cardiomyopathies")
    print("\t\t\t2)kidney disease")
    print("\t\t\t3)chronic obstructive pulmonary disease (COPD)")
    print("\t\t\t4)obesity, which occurs in people with a body mass index (BMI) of 30 ")
    print("\t\t\t  or higher")
    print("\t\t\t5)sickle cell disease")
    print("\t\t\t6)a weakened immune system from a solid organ transplant")
    print("\t\t\t7)type 2 diabetes")
    print("\n")
    print("\n")
    time.sleep(1)
    INFORMATION()

#NEWS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def news():
    print("\t\t...........................................................................")
    print("\t\t*****************Welcome to COVID-19 Prevention Prober*********************")
    print("\t\t...........................................................................")
    print("\n")
    print("n\t\t***********Graphical Analysis Of Data*************")
    print("\n")
    print('Welcome to the News Section. Here you can obtain all the updates.')
    print('Please select from the following what type of information you want to extract')
    print('1: Most Affected Countries')
    print('2: Statewise COVID cases breakdown in India')
    print('3: Daily trend of COVID Cases in India')
    print('4: Vaccine Update')
    print('5: Return to main menu')
    opt=int(input('Please enter your option number:'))
    print("\n")
    if opt==1:
        import matplotlib.pyplot as plt
        cases=[12.3,9.14,6.07,2.14,2.11,1.56,1.51,1.41,1.37,1.25]
        cont=['United States','India','Brazil','France','Russia','Spain','United Kingdom','Italy','Argentina','Colombia']
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        plt.pie(cases,explode=explode,labels=cont,shadow=True)
        plt.title('Breakdown of Number of Active Cases in Most Affected Coutries in Millions')
        plt.show()
        print("\n")
        news()
    elif opt==2:
        import numpy as np
        import matplotlib.pyplot as plt
        cases=[1780,873,862,770,563,530,527,456,314,264,244,230,223,217,212,197,193,146,107,107,71,46,36,34,32,23,16,16,11,10,4,4,3,0]
        states=['Maharashtra','Karnataka','Andhra Pradesh','Tamil Nadu','Kerala','Delhi','Uttar Pradesh','West Bengal','Odisha','Telangana','Rajasthan','Bihar','Chattisgarh','Harayana','Assam','Gujarat','Madhya Pradesh','Punjab','Jharkhand','Jammu and Kashmir','Uttarakhand','Goa','Pudducherry','Himachal Pradesh','Tripura','Manipur','Chandigarh','Anurachcal Pradesh','Meghalaya','Nagaland','Sikkim','Andaman and Nicobar Islands','Mizoram','Lakshadweep']
        y_pos=np.arange(len(states))
        plt.barh(y_pos,cases,color='yellowgreen')
        plt.yticks(y_pos,states)
        plt.xlabel('Cases in Thousands')
        plt.title('Number of Active Cases in Indian States in Thousands')
        plt.show()
        print("\n")
        news()
    
    elif opt==3:
        import matplotlib.pyplot as plt
        dates=['Apr','Apr','Apr','May','May','May','Jun','Jun','Jun','Jul','Jul','Jul','Aug','Aug','Aug','Sep','Sep','Sep','Oct','Oct','Oct','Nov','Nov','Nov','Nov']
        cases=[437,896,1540,1755,3277,5611,8392,9985,14516,18653,26506,40425,57118,62064,69652,69921,95735,92605,86821,73272,46790,46963,38073,45882,41322]
        plt.plot(dates,cases,color='lightcoral')
        plt.xlabel('Dates')
        plt.ylabel('Number of Daily Cases')
        plt.title('Daily Trend of COVID Cases in India')
        plt.show()
        print("\n")
        news()

    elif opt==4:
        print('..............................................................................................')
        print('..............................................................................................')
        print('')
        print('')
        print('In a significant development, Oxford University and pharmaceutical giant AstraZeneca on Monday')
        print('(November 23) announced that the COVID-19 vaccine being developed jointly by them has shown 70')
        print('per cent efficiency. Oxford-AstraZeneca, however, added that the efficacy of vaccine could be')
        print('around 90 per cent under one dosing regimen. US-based pharma giants Pfizer and Moderna, this')
        print('week reported preliminary results from late-stage trials claiming that the efficacy of the')
        print('            coronavirus vaccine developed by them were was almost 95%.')
        print('')
        print('')
        print('..............................................................................................')
        print('..............................................................................................')
        print("\n")
        news()
    else:
        print("\n")
        MAIN_MENU()

MAIN_MENU()
