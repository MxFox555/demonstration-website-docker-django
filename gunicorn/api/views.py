import json
import socket
from loggedin.network_functions import send_msg, recv_msg
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from web.models import UserAPI, APICalls
from loggedin.billing_dates import BillingDates

# Create your views here.
@csrf_exempt
def api_request(request):
    json_response = {}
    if request.method == "POST":
        #The correct method
        try:
            request_dict = json.loads(request.body)
            key_user = UserAPI.objects.filter(api_key=request_dict['key'], is_active=True)
            if len(key_user) > 0:
                key_user = key_user[0]
                user_billing = BillingDates(key_user)
                day_start = user_billing.day_start()
                day_end = user_billing.day_end()
                api_calls_today = len(APICalls.objects.filter(user_called=key_user, time_called__range=[day_start, day_end], is_counted=True))
                # Append this for paid users
                if (api_calls_today < 20 or len(request_dict['open']) < 50):
                    if (all(isinstance(x, (int, float)) for x in request_dict['open']) and all(isinstance(x, (int, float)) for x in request_dict['high']) and all(isinstance(x, (int, float)) for x in request_dict['low']) and all(isinstance(x, (int, float)) for x in request_dict['close']) and all(isinstance(x, (int, float)) for x in request_dict['volume'])):
                        if len(request_dict['open']) == len(request_dict['high']) == len(request_dict['low']) == len(request_dict['close']) == len(request_dict['volume']):
                            try:
                                # All data is valid
                                # NEED TO ADD MORE STUFF
                                #print('Data is valid')
                                # Connect to the best server, Maybe try to connect to one, if unable then go to another one? like a list where you can keep adding to it
                                recv_dict = None
                                tries = 1
                                while recv_dict == None and tries < 1000:
                                    for ip in settings.CALCULATION_SERVERS:
                                        try:
                                            ipport = ip.split(":")
                                            s = socket.socket()
                                            s.connect((ipport[0], int(ipport[1])))
                                            send_msg(s, str(request_dict).encode())
                                            recv_dict = recv_msg(s).decode()
                                            recv_dict = recv_dict.replace("'", '"')
                                            recv_dict = json.loads(recv_dict)
                                            s.close()
                                        except:
                                            tries += 1
                                if tries == 1000:
                                    raise ConnectionError
                                json_response['stable'] = recv_dict['stable']
                                json_response['volatile'] = recv_dict['volatile']
                                # If all items are of equivalent length and less than 50 items (range of free calls) then make call but not counted
                                new_api_call = None
                                # Add or clauses to not count for paid members
                                if (len(request_dict['open']) < 50):
                                    new_api_call = APICalls(user_called=key_user, is_counted=False)
                                else:
                                    new_api_call = APICalls(user_called=key_user, is_counted=True)
                                new_api_call.save()
                                json_response['stable'] = recv_dict['stable']
                                json_response['volatile'] = recv_dict['volatile']
                            except ConnectionError as err:
                                print(err)
                                json_response['error'] = ['Connection could not be established, Your API calls have not been affected']
                        else:
                            # Data lists are not the same length
                            json_response['error'] = ['Data lists are not the same length']
                            pass
                    else:
                        # Data is not valid
                        json_response['error'] = ['Data is not numerical']
                else:
                    # Daily API call limit reached
                    json_response['error'] = ['Daily API call limit reached, resets at: ' + str(day_end).split('.')[0] + ' UTC']
                    pass
            else:
                # Key is not valid
                json_response['error'] = ['Key not valid']
        except json.decoder.JSONDecodeError:
            json_response['error'] = ['Request not formatted correctly']
    else:
        json_response['error'] = ['Request must be a POST request']
    return JsonResponse(json_response)