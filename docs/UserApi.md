# openapi_client.UserApi

All URIs are relative to *https://api.pharmatrace.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**me_get**](UserApi.md#me_get) | **GET** /me | User Profile


# **me_get**
> Profile me_get()

User Profile

The User Profile endpoint returns information about the PharmaTrace user that has authorized with the application.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.UserApi()

try:
    # User Profile
    api_response = api_instance.me_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

