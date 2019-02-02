# openapi_client.SystemInformationsApi

All URIs are relative to *https://api.pharmatrace.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_system_information**](SystemInformationsApi.md#add_system_information) | **POST** /systeminformations | 
[**delete_system_information**](SystemInformationsApi.md#delete_system_information) | **DELETE** /systeminformations/{id} | 
[**find_system_informations**](SystemInformationsApi.md#find_system_informations) | **GET** /systeminformations | 
[**find_systeminformation_by_id**](SystemInformationsApi.md#find_systeminformation_by_id) | **GET** /systeminformations/{id} | 


# **add_system_information**
> SystemInformation add_system_information(system_information)



Creates a new systeminformation

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.SystemInformationsApi()
system_information = openapi_client.SystemInformation() # SystemInformation | SystemInformation to create

try:
    api_response = api_instance.add_system_information(system_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInformationsApi->add_system_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_information** | [**SystemInformation**](SystemInformation.md)| SystemInformation to create | 

### Return type

[**SystemInformation**](SystemInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_information**
> delete_system_information(id)



deletes a single systeminformation based on the ID supplied

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.SystemInformationsApi()
id = 56 # int | ID of systeminformation to delete

try:
    api_instance.delete_system_information(id)
except ApiException as e:
    print("Exception when calling SystemInformationsApi->delete_system_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of systeminformation to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_system_informations**
> list[SystemInformation] find_system_informations(tags=tags, limit=limit)



Returns all systeminformations from the system that the user has access to Nam sed condimentum est. Maecenas tempor sagittis sapien, nec rhoncus sem sagittis sit amet. Aenean at gravida augue, ac iaculis sem. Curabitur odio lorem, ornare eget elementum nec, cursus id lectus. Duis mi turpis, pulvinar ac eros ac, tincidunt varius justo. In hac habitasse platea dictumst. Integer at adipiscing ante, a sagittis ligula. Aenean pharetra tempor ante molestie imperdiet. Vivamus id aliquam diam. Cras quis velit non tortor eleifend sagittis. Praesent at enim pharetra urna volutpat venenatis eget eget mauris. In eleifend fermentum facilisis. Praesent enim enim, gravida ac sodales sed, placerat id erat. Suspendisse lacus dolor, consectetur non augue vel, vehicula interdum libero. Morbi euismod sagittis libero sed lacinia.  Sed tempus felis lobortis leo pulvinar rutrum. Nam mattis velit nisl, eu condimentum ligula luctus nec. Phasellus semper velit eget aliquet faucibus. In a mattis elit. Phasellus vel urna viverra, condimentum lorem id, rhoncus nibh. Ut pellentesque posuere elementum. Sed a varius odio. Morbi rhoncus ligula libero, vel eleifend nunc tristique vitae. Fusce et sem dui. Aenean nec scelerisque tortor. Fusce malesuada accumsan magna vel tempus. Quisque mollis felis eu dolor tristique, sit amet auctor felis gravida. Sed libero lorem, molestie sed nisl in, accumsan tempor nisi. Fusce sollicitudin massa ut lacinia mattis. Sed vel eleifend lorem. Pellentesque vitae felis pretium, pulvinar elit eu, euismod sapien. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.SystemInformationsApi()
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | maximum number of results to return (optional)

try:
    api_response = api_instance.find_system_informations(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInformationsApi->find_system_informations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] 

### Return type

[**list[SystemInformation]**](SystemInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_systeminformation_by_id**
> SystemInformation find_systeminformation_by_id(id)



Returns a systeminformation based on the ID

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.SystemInformationsApi()
id = 56 # int | ID of systeminformation to fetch

try:
    api_response = api_instance.find_systeminformation_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInformationsApi->find_systeminformation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of systeminformation to fetch | 

### Return type

[**SystemInformation**](SystemInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

