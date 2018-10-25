# openapi_client.ContainerApi

All URIs are relative to *https://api.pharmatrace.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**location_history_get**](ContainerApi.md#location_history_get) | **GET** /locationHistory | Location History


# **location_history_get**
> Locations location_history_get(container_id=container_id, offset=offset, limit=limit)

Location History

Returns the location history of a container or a individually labeled pharmaceutical

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ContainerApi()
container_id = 'container_id_example' # str | container id of the tracked container. (optional)
offset = 56 # int | Offset the list of returned results by this amount. Default is zero. (optional)
limit = 56 # int | Number of items to retrieve. Default is 5, maximum is 100. (optional)

try:
    # Location History
    api_response = api_instance.location_history_get(container_id=container_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->location_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| container id of the tracked container. | [optional] 
 **offset** | **int**| Offset the list of returned results by this amount. Default is zero. | [optional] 
 **limit** | **int**| Number of items to retrieve. Default is 5, maximum is 100. | [optional] 

### Return type

[**Locations**](Locations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

