## DESCRIPTION
*DATA MODEL SEND* = Data Model which is handed through the Frontend, Master Service to the API Category Service and then transformed in individual needed data model (Denormalization)\
*DATA MODEL GET*  = Data Model which is built in the API Category Service (Normalization) based on the returning value from any external API and sent to the Master Service

## Entertainment
### Function 1
**Category**: Entertainment\
**Function 1**: Play a spotify song (or playlist?)\
**Type**: OPERATION  \
**Data Model SEND**: {"OAuth Token", "Song Request (Playlist Request?)"}  FIXED VALUES TO API: {OAuthToken (granted by succesful auth)}  \
**Data Model GET**: {"Ok"}  \
**Public API 1**: https://developer.spotify.com/documentation/web-api/quick-start/  \
**Note**: To authenticate the api provides convenient 3rd party auth (via spotify account or facebook) without any coding effort

### Function 2
**Function 2**: Get News Sent By Mail\
**Type**: OPERATION\
**Data Model SEND**: {"Category of News" + We somehow need all the attributes from Messaging Email Data Model)\
**Data Model GET**: {"Ok"}\
**Public API 1**: https://rapidapi.com/microsoft-azure/api/bing-news-search \
**Public API 2**: https://newsapi.org/ \
**Note**: This function was introduced so that we might think of being able to pass information from one routine component to another

## Nature
### Function 1
**Category**: Nature\
**Function 1**: Get Weather for a location\
**Type**: CONDITION\
**Data Model SEND**: {"Location", "Date", "Degree", "Relation (<,>,etc)"}  FIXED VALUES TO API: {EndDate= Date, Unit = 'Metric (Degree Celsius)', Aggregated Hours = 24} \
**Data Model GET**: {"DegreeCelsius"}\
**Public API 1**: https://rapidapi.com/community/api/open-weather-map \
**Public API 2**: https://rapidapi.com/aerisweather-aerisweather/api/aerisweather1 \
**Public API 3**: https://rapidapi.com/awigmore/api/visual-crossing-weather \
**Note**: I used only APIs where no LAT or LONG is needed. (1) and (2) only need location,  (3) need start_date and aggregated_hours

## Smart Home
### Function 1
**Category**: Smart Home\
**Type**: OPERATION\
**Function 1**: Get a cup of coffee\
**Data Model SEND**: {"Unique name of action", "Number of cups"}\
**Data Model GET**: {"ok"}\
**Public API 1**: https://github.com/AdenForshaw/smarter-coffee-api/blob/master/smarter-coffee-api.py \
**Note**: We probably need to extend this public API (fake it) and add an endpoint which informs whether the brewing process is finished (because of function (4))

### Function 2
**Function 2**: Manipulate the smart light bulb / Interaction with the smart light bulb\
**Type**: OPERATION\
**Data Model SEND**: {"state = ON OR OFF"}\
**Data Model GET**: {"ok"}\
**Public API 1**: https://github.com/plasticrake/tplink-smarthome-api/blob/e0a6e8505d98f1db8fa8b33041671d6ebecf69e7/src/plug/index.js#L403 (USING TP-LINK)\
**Public API 2**: https://github.com/konsumer/kasa_control#module_send (USING KASA)\
**Note**: A TP-Link Simulator can be found here: https://github.com/plasticrake/tplink-smarthome-simulator ; Or we develop a API which works more or less like a real smart bulb

### Function 3
**Function 3**: Manipulate the plug / Interaction with the smart plug \
**Type**: OPERATION\
**Data Model SEND**: {"state = ON OR OFF"}\
**Data Model GET**: {"ok"}\
**Public API 1**: https://github.com/plasticrake/tplink-smarthome-api/blob/e0a6e8505d98f1db8fa8b33041671d6ebecf69e7/src/plug/index.js#L403  AND https://gist.github.com/agent4788/81beb25cdcdbf7e9371361ca87d3b04a \
**Note**: A TP-Link Simulator can be found here: https://github.com/plasticrake/tplink-smarthome-simulator ; Or we develop a API which works more or less like a real smart plug

### Function 4
**Function 4**: Get if the cup of coffee finished\
**Type**: CONDITION\
**Data Model SEND**: {"Unique name of action"}\
**Data Model GET**: {"Done / In Progress"}\
**Public API 1**: https://github.com/AdenForshaw/smarter-coffee-api/blob/master/smarter-coffee-api.py \
**Note**: We probably need to extend this public API (fake it) and add an endpoint which informs whether the brewing process is finsihed (because of function (4))



