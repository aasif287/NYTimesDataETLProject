#imports the necessary packages
import requests,pprint,pathlib,csv
#creates varible to hold url
url='https://api.nytimes.com/svc/search/v2/articlesearch.json'
#API key stored with API endpoint of Article Search
API_KEY='CHn1bQgMCj5KgdRHA3yuQ3FBcG7yQEik'
#function that takes parameters and has request.get() method is called, using the URL and the parameters and saved in a response object
def api_refresh(parameters):
    response=requests.get(url,params=parameters)
    content=response.json()
    #prints the response, meta and hits information of data 
    print(content['response']['meta']['hits'])
#using the params parameter from the requests.get() method to pass in the API key and query
parameters={'q':'Instagram','api-key':API_KEY}
#uses function
api_refresh(parameters)
#adds the filter query for articles 
parameters['fq']='document_type:("article")'
print(parameters)
api_refresh(parameters)
#modifying the filer query to includes the Arts Section 
d_sn_filter='document_type:("article") AND section_name:("Arts")'
#update the value to the fq key in the parameters
parameters['fq']=d_sn_filter
api_refresh(parameters)
#creates and addes date ranges for parameter data
parameters['begin_date']='20180425'
parameters['end_date']='20220401'
api_refresh(parameters)
print(parameters)
#uses pprint package to print json data
response=requests.get(url,params=parameters)
content=response.json()
pprint.pprint(content)
#transformation process, declares empty list
final_data=[]
#for loop to look through content data of response and docs information 
for i in content['response']['docs']:
    pub_date=i['pub_date']
    web_url=i['web_url']
    for v in i['keywords']:
        keyword=v['value']
        #append to list for each keyword value
        final_data.append({'date':pub_date, 'web_url':web_url, 'keyword':keyword})
#prints list
print(final_data)
#uses pathlib and csv packages to write to csv file the information in list
file_path=pathlib.Path.cwd()/"final_data.csv"
file=file_path.open(mode='w',encoding='utf-8',newline="")
writer=csv.DictWriter(file,fieldnames=["date","web_url","keyword"])
#write the header row to the file
writer.writeheader()
#writing the rows to the file
writer.writerows(final_data)
