import rira_api
from rira_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyQuery
rira_api.configuration.api_key['apiKey'] = 'bywnEJjpRsmLgn5hbAW!UNcGLMgIUxzEPkh7dp_N_oc88jQsLwF'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rira_api.configuration.api_key_prefix['apiKey'] = 'Bearer'
# Configure API key authorization: apikeyHeader
#rira_api.configuration.api_key['apiKey'] = 'bywnEJjpRsmLgn5hbAW!UNcGLMgIUxzEPkh7dp_N_oc88jQsLwF'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rira_api.configuration.api_key_prefix['apiKey'] = 'Bearer'
# create an instance of the API class
api_instance = rira_api.NodeApi()
node_type = 'OCC' # str | node type of required connection list
detail_level = 'ipNkey' # str | The detail level of connectivity information, can be ip|ipNkey|ipNpswd
connection_type = 'ssh' # str | The type of connection, like SSH, LDAP or any user defined connection type for thos node type

try:
    api_response = api_instance.connections('OCC', 'ip', 'SSH')
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->connections: %s\n" % e