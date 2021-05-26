## New stories start from here
## Interactive Story 1

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "amrs4"}
    - slot{"email": "amrs4"}
    - action_check_valid_mail
    - slot{"validmailid": false}
    - utter_email_invalid
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## Interactive Story 2


* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "am@s48*"}
    - slot{"email": "am@s48*"}
    - action_check_valid_mail
    - slot{"validmailid": false}
    - utter_email_invalid
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart


## Interactive Story 3


* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## Interactive Story 4


* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## Interactive Story 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nandyal"}
    - slot{"location": "nandyal"}
    - action_validate_city
    - slot{"validcity": false}
    - utter_city_invalid
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"cost": "two"}
    - slot{"cost": "two"}
    - action_search_restaurants
    - slot{"location": "ajmer"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

## Interactive Story 6
* restaurant_search{"cuisine": "chinese", "location": "adoni"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "adoni"}
    - action_validate_city
    - slot{"validcity": false}
    - utter_city_invalid
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

## Interactive Story 7
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "keesara"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "keesara"}
    - action_validate_city
    - slot{"validcity": false}
    - utter_city_invalid
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

## Interactive Story 8
* restaurant_search{"location": "baasara"}
    - slot{"location": "baasara"}
    - action_validate_city
    - slot{"validcity": false}
    - utter_city_invalid
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"cost": "two"}
    - slot{"cost": "two"}
    - action_search_restaurants
    - slot{"location": "jabalpur"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

## Interactive Story 9
* restaurant_search{"cuisine": "north indian", "location": "jaipur"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "jaipur"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## Interactive Story 10
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "bhongir"}
    - slot{"location": "bhongir"}
    - action_validate_city
    - slot{"validcity": false}
    - utter_city_invalid
* restaurant_search{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "two"}
    - slot{"cost": "two"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "abc*12"}
    - slot{"email": "abc*12"}
    - action_check_valid_mail
    - slot{"validmailid": false}
    - utter_email_invalid
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## Interactive Story 11
* restaurant_search{"cuisine": "italian", "location": "palakollu"}
    - slot{"cuisine": "italian"}
    - slot{"location": "palakollu"}
    - action_validate_city
    - slot{"validcity": false}
    - utter_city_invalid
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

## Interactive Story 12
* restaurant_search{"cuisine": "south indian", "location": "mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## Interactive Story 13
* restaurant_search{"location": "jagityal"}
    - slot{"location": "jagityal"}
    - action_validate_city
    - slot{"validcity": false}
    - utter_city_invalid
* restaurant_search{"location": "pondicherry"}
    - slot{"location": "pondicherry"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"cost": "two"}
    - slot{"cost": "two"}
    - action_search_restaurants
    - slot{"location": "pondicherry"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

## Interactive Story 14
* restaurant_search{"cuisine": "chinese", "location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart


## Interactive Story 15
* restaurant_search{"cuisine": "mexican", "location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

 ## Interactive Story 16
* restaurant_search{"cuisine": "north indian", "location": "kolkata"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "kolkata"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart

  ## Interactive Story 17
* restaurant_search{"cuisine": "south indian", "location": "madurai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "madurai"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "madurai"}
    - utter_ask_mail
* affirm{"wantmail": "nope"}
    - slot{"wantmail": "nope"}
    - utter_goodbye
    - action_restart

 ## Interactive Story 18
* restaurant_search{"cuisine": "american", "location": "delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"validcity": true}
    - utter_ask_price
* restaurant_search{"cost": "three"}
    - slot{"cost": "three"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail
* affirm{"wantmail": "send"}
    - slot{"wantmail": "send"}
    - utter_email
* restaurant_search{"email": "pvnkmr@gmail.com"}
    - slot{"email": "pvnkmr@gmail.com"}
    - action_check_valid_mail
    - slot{"validmailid": true}
    - action_send_email
    - utter_goodbye
    - action_restart