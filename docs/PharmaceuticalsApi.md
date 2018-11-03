# openapi_client.PharmaceuticalsApi

All URIs are relative to *https://api.pharmatrace.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pharmaceutical**](PharmaceuticalsApi.md#add_pharmaceutical) | **POST** /pharmaceuticals | 
[**delete_pharmaceutical**](PharmaceuticalsApi.md#delete_pharmaceutical) | **DELETE** /pharmaceuticals/{id} | 
[**find_pharmaceutical_by_id**](PharmaceuticalsApi.md#find_pharmaceutical_by_id) | **GET** /pharmaceuticals/{id} | 
[**find_pharmaceuticals**](PharmaceuticalsApi.md#find_pharmaceuticals) | **GET** /pharmaceuticals | 


# **add_pharmaceutical**
> Pharmaceutical add_pharmaceutical(pharmaceutical)



Creates a new pharmaceutical

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PharmaceuticalsApi()
pharmaceutical = openapi_client.Pharmaceutical() # Pharmaceutical | Pharmaceutical to create

try:
    api_response = api_instance.add_pharmaceutical(pharmaceutical)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PharmaceuticalsApi->add_pharmaceutical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pharmaceutical** | [**Pharmaceutical**](Pharmaceutical.md)| Pharmaceutical to create | 

### Return type

[**Pharmaceutical**](Pharmaceutical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pharmaceutical**
> delete_pharmaceutical(id)



deletes a single pharmaceutical based on the ID supplied

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PharmaceuticalsApi()
id = 56 # int | ID of pharmaceutical to delete

try:
    api_instance.delete_pharmaceutical(id)
except ApiException as e:
    print("Exception when calling PharmaceuticalsApi->delete_pharmaceutical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of pharmaceutical to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_pharmaceutical_by_id**
> Pharmaceutical find_pharmaceutical_by_id(id)



Returns a pharmaceutical based on the ID

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PharmaceuticalsApi()
id = 56 # int | ID of pharmaceutical to fetch

try:
    api_response = api_instance.find_pharmaceutical_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PharmaceuticalsApi->find_pharmaceutical_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of pharmaceutical to fetch | 

### Return type

[**Pharmaceutical**](Pharmaceutical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_pharmaceuticals**
> list[Pharmaceutical] find_pharmaceuticals(tags=tags, limit=limit)



Returns all pharmaceuticals from the system that the user has access to Nam sed condimentum est. Maecenas tempor sagittis sapien, nec rhoncus sem sagittis sit amet. Aenean at gravida augue, ac iaculis sem. Curabitur odio lorem, ornare eget elementum nec, cursus id lectus. Duis mi turpis, pulvinar ac eros ac, tincidunt varius justo. In hac habitasse platea dictumst. Integer at adipiscing ante, a sagittis ligula. Aenean pharetra tempor ante molestie imperdiet. Vivamus id aliquam diam. Cras quis velit non tortor eleifend sagittis. Praesent at enim pharetra urna volutpat venenatis eget eget mauris. In eleifend fermentum facilisis. Praesent enim enim, gravida ac sodales sed, placerat id erat. Suspendisse lacus dolor, consectetur non augue vel, vehicula interdum libero. Morbi euismod sagittis libero sed lacinia.  Sed tempus felis lobortis leo pulvinar rutrum. Nam mattis velit nisl, eu condimentum ligula luctus nec. Phasellus semper velit eget aliquet faucibus. In a mattis elit. Phasellus vel urna viverra, condimentum lorem id, rhoncus nibh. Ut pellentesque posuere elementum. Sed a varius odio. Morbi rhoncus ligula libero, vel eleifend nunc tristique vitae. Fusce et sem dui. Aenean nec scelerisque tortor. Fusce malesuada accumsan magna vel tempus. Quisque mollis felis eu dolor tristique, sit amet auctor felis gravida. Sed libero lorem, molestie sed nisl in, accumsan tempor nisi. Fusce sollicitudin massa ut lacinia mattis. Sed vel eleifend lorem. Pellentesque vitae felis pretium, pulvinar elit eu, euismod sapien. 

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.PharmaceuticalsApi()
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | maximum number of results to return (optional)

try:
    api_response = api_instance.find_pharmaceuticals(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PharmaceuticalsApi->find_pharmaceuticals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] 

### Return type

[**list[Pharmaceutical]**](Pharmaceutical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

