from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
import zomatopy
import json
import smtplib
import itertools
import re

#List of al tier1 and tier2 cities combined
tier1tier2=['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'dindigul', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 'kanpur', 'karnal', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 'pune' 'pondicherry', 'purulia', 'prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat', 'thanjavur', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar', 'vijayawada', 'visakhapatnam', 'vellore', 'warangal']

resls=[]


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
            config = {"user_key": "700ddebbe4bb17d8d8ac9392c0ece221"}
            zomato = zomatopy.initialize_app(config)
            global resls
            loc = tracker.get_slot('location')

            cuisine = tracker.get_slot('cuisine').lower()
            p= str(tracker.get_slot('cost'))
            response = ""
            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            cuisines_dict={'chinese':5,'mexican':25,'italian':50,'american':7,'north indian':70,'south indian':85}
            results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
            d = json.loads(results)

            s=[]
            display=0
            if d['results_found'] == 0:
                response= "no results"
            else:
                if p=='one':
                    s=[restaurant for restaurant in d['restaurants'] for key,val in restaurant.items()  if val['average_cost_for_two']<300 ]
                elif p=='two':
                    s=[restaurant for restaurant in d['restaurants'] for key,val in restaurant.items()  if 300<=val['average_cost_for_two']<=700 ]
                else:
                    s=[restaurant for restaurant in d['restaurants'] for key,val in restaurant.items()  if val['average_cost_for_two']>700 ]

            resls=[restaurant for restaurant in sorted(s,key=lambda a: a['restaurant']['user_rating']['aggregate_rating'],reverse=True)]

            if len(resls) > 5:
              display = 5
            else:
              display = len(resls)

            if display==0:
                dispatcher.utter_message('No results found for the given selection criteria,start from beginning\n')
                return[Restarted()]
            #Display restaurants as per result
            for restaurant in list(itertools.islice(resls,0,display)):
                    response=response+ " "+restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"+"\n"

            dispatcher.utter_message(response)



            return [SlotSet('location', loc)]


class ActionSendemail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):

        sendmail = tracker.get_slot('wantmail')
        mailresponse=""
        mailnum =0
        global resls

        if sendmail == 'send':
            # send mail to max of top 10 restaurants
            if len(resls) > 10:
                mailnum = 10
            else:
                mailnum = len(resls)
                # Display restaurants as per result
            for restaurant in list(itertools.islice(resls, 0, mailnum)):
                mailresponse =mailresponse+ " "+ restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address']+"\n"+"average cost for two is "+str(restaurant['restaurant']['average_cost_for_two']) + "\n" + " zomato rating is " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n" + "\n"




            email = str(tracker.get_slot('email'))
            gmail_user = 'foodie.ug2020@gmail.com'
            gmail_password = 'upgrad@123'

            sent_from = gmail_user
            to=[]
            to.append(email)
            subject = str('Restaurant Search results')
            body = str(mailresponse)

            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()

                dispatcher.utter_message("Email sent with top restaurants list up to maximum of ten\n")
            except:
                dispatcher.utter_message("Some thing wrong .email not sent\n")
        dispatcher.utter_message("enjoy delicious food..Bon Apetit\n")

class ActionMailValidityCheck(Action):
    def name(self):
        return 'action_check_valid_mail'

    def run(self, dispatcher, tracker, domain):
        email = str(tracker.get_slot('email'))
        pattern=r"[\w.\-]+@[A-z0-9-]+.[A-z]{2,3}(.[A-z]{2})?"
        if re.search(pattern,email):
            return[SlotSet('validmailid', True)]
        else :
            return [SlotSet('validmailid', False)]

class ActionValidateCity(Action):
    def name(self):
        return 'action_validate_city'

    def run(self, dispatcher, tracker, domain):
        global tier1tier2
        loc = tracker.get_slot('location')
        if str(loc).lower()  in tier1tier2:
            return[SlotSet('validcity', True)]
        else:
            return [SlotSet('validcity', False)]

