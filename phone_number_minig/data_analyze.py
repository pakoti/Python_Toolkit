#pyhon program that check phone number log file and gives detail 


#starting point

#One of Our datas that used them is this:Two dictionaries for two carriers that we them in iran 
#(i put in a dictionary so that is so easy to create and use but i should put in a database in future)

#Irancell data
irancell={
"0930":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0931":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0932":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0932":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0933":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0934":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0935":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0936":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0937":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0938":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0939":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0901":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0902":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0903":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0904":
{
"original_province":"Only-For-Kids",
"service_type":"Cred & Prem"
}
,  
"0905":
{
"original_province":"Nation-wide",
"service_type":"Cred & Prem"
}
,  
"0941":
{
"original_province":"TD-LTE Modem Sim",
"service_type":"Cred & Prem"
}  
}

#hamrah aval data(i put in a dictionary so that is so easy to create and use but i should put in a database in future)
hamrah_aval={
"0910":
{
"original_province":"Nation-wide",
"other_provinces":"Nation-wide",
"service_type":"Cred & Prem"
}
,
"0911":
{
"original_province":"Mazandran",
"other_provinces":"Mazandran & Golestan",
"service_type":"Cred & Prem"
}
,
"0912":
{
"original_province":"Tehran",
"other_provinces":"Tehran & Semnam & qazvin & Some area of Markazi",
"service_type":"Prem"
}
,
"0913":
{
"original_province":"Isfahan",
"other_provinces":"Yazd & Chahar mahal & Kerman",
"service_type":"Cred & Prem"
}
,
"0914":
{
"original_province":"East Azerbaijan",
"other_provinces":"East Azerbaijan & aradabil & isfahan",
"service_type":"Cred & Prem"
}
,
"0915":
{
"original_province":"Razavi Khorasan",
"other_provinces":"North & south khorasan Razavi & sistan blochestan",
"service_type":"Cred & Prem"
}
,
"0916":
{
"original_province":"Khozestan",
"other_provinces":"Lorestan & Fars & isfahan",
"service_type":"Cred & Prem"
}
,
"0917":
{
"original_province":"Fars",
"other_provinces":"Boshehr & kohgiloye booyer ahmad &hormozgan",
"service_type":"Cred & Prem"
}
,
"0918":
{
"original_province":"Hamedan",
"other_provinces":"Kermanshah & ilam & Kurdestan",
"service_type":"Cred & Prem"
}
,
"0919":
{
"original_province":"Tehran",
"other_provinces":"Alborz & semnan & qom & qazvin &zanjan ",
"service_type":"Cred & Prem(if costumer wants)"
}
,
"0990":
{
"original_province":"Nation-wide",
"other_provinces":"Nation-wide",
"service_type":"Cred & Prem"
}
,
"0991":
{
"original_province":"Nation-wide",
"other_provinces":"Nation-wide",
"service_type":"Cred & Prem"
}
,
"0992":
{
"original_province":"Nation-wide",
"other_provinces":"Nation-wide",
"service_type":"Cred"
}
,
"0993":
{
"original_province":"Nation-wide",
"other_provinces":"Nation-wide",
"service_type":"Cred"
}
,
"0994":
{
"original_province":"Nation-wide",
"other_provinces":"Nation-wide",
"service_type":"Cred"
}
}

#results with different outputs


#only duration and time included
outbound_calls=[]
#duration and time and also where it originated included
detailed_outbound_calls=[]


#Functions
#orgin function is function checks where the phone number is from(province and carrier)
def detail_carrier(number):
    if number in hamrah_aval:
        a=hamrah_aval.get(number)
        return a
    else:
        b=irancell.get(number)
        return b

def origin_carrier(number):
    if number in hamrah_aval:
        return "Hamrah Aval"
    elif number in irancell:
        return "IranCell"
    else:
        return "Not in our Database"


#Global Variebls that used in making two of our results
i=0

#open and read the file after the appending:
with open("C:\\Users\\DarkMaster\\Desktop\\demo.txt", "r") as file:

    for x in file:
        i=i+1
        #dicts used only to update our lists
        phone_number_dict={}
        detailed_phone_number_dict={}

        #creating phone_number_dict={}
        phone_number_dict.update({"phone_number"+" "+str(i):x[13:25]})
        phone_number_dict.update({"duration":x[25:30]})
        phone_number_dict.update({"date":x[30:37]})


        detailed_phone_number_dict.update({"phone_number"+" "+str(i):x[13:25]})
        detailed_phone_number_dict.update({"duration":x[25:30]})
        detailed_phone_number_dict.update({"date":x[30:37]})
        detailed_phone_number_dict.update({"code":x[13:17]})
        detailed_phone_number_dict.update({"origin_carrier":origin_carrier(x[13:17])})
        detailed_phone_number_dict.update({"detail_carrier":detail_carrier(x[13:17])})



        outbound_calls.append(phone_number_dict)
        detailed_outbound_calls.append(detailed_phone_number_dict)
          
print (detailed_outbound_calls)
print (outbound_calls)