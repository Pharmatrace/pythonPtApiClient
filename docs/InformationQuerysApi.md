# openapi_client.InformationQuerysApi

All URIs are relative to *https://api.pharmatrace.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_information_query**](InformationQuerysApi.md#add_information_query) | **POST** /informationquerys | 
[**delete_information_query**](InformationQuerysApi.md#delete_information_query) | **DELETE** /informationquerys/{id} | 
[**find_information_querys**](InformationQuerysApi.md#find_information_querys) | **GET** /informationquerys | 
[**find_informationquery_by_id**](InformationQuerysApi.md#find_informationquery_by_id) | **GET** /informationquerys/{id} | 


# **add_information_query**
> InformationQuery add_information_query(information_query)



Creates a new informationquery

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.InformationQuerysApi()
information_query = openapi_client.InformationQuery() # InformationQuery | InformationQuery to create

try:
    api_response = api_instance.add_information_query(information_query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationQuerysApi->add_information_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **information_query** | [**InformationQuery**](InformationQuery.md)| InformationQuery to create | 

### Return type

[**InformationQuery**](InformationQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_information_query**
> delete_information_query(id)



deletes a single informationquery based on the ID supplied

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.InformationQuerysApi()
id = 56 # int | ID of informationquery to delete

try:
    api_instance.delete_information_query(id)
except ApiException as e:
    print("Exception when calling InformationQuerysApi->delete_information_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of informationquery to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_information_querys**
> list[InformationQuery] find_information_querys(tags=tags, limit=limit)



Returns all informationquerys from the system that the user has access to Nam sed condimentum est. Maecenas tempor sagittis sapien, nec rhoncus sem sagittis sit amet. Aenean at gravida augue, ac iaculis sem. Curabitur odio lorem, ornare eget elementum nec, cursus id lectus. Duis mi turpis, pulvinar ac eros ac, tincidunt varius justo. In hac habitasse platea dictumst. Integer at adipiscing ante, a sagittis ligula. Aenean pharetra tempor ante molestie imperdiet. Vivamus id aliquam diam. Cras quis velit non tortor eleifend sagittis. Praesent at enim pharetra urna volutpat venenatis eget eget mauris. In eleifend fermentum facilisis. Praesent enim enim, gravida ac sodales sed, placerat id erat. Suspendisse lacus dolor, consectetur non augue vel, vehicula interdum libero. Morbi euismod sagittis libero sed lacinia.  Sed tempus felis lobortis leo pulvinar rutrum. Nam mattis velit nisl, eu condimentum ligula luctus nec. Phasellus semper velit eget aliquet faucibus. In a mattis elit. Phasellus vel urna viverra, condimentum lorem id, rhoncus nibh. Ut pellentesque posuere elementum. Sed a varius odio. Morbi rhoncus ligula libero, vel eleifend nunc tristique vitae. Fusce et sem dui. Aenean nec scelerisque tortor. Fusce malesuada accumsan magna vel tempus. Quisque mollis felis eu dolor tristique, sit amet auctor felis gravida. Sed libero lorem, molestie sed nisl in, accumsan tempor nisi. Fusce sollicitudin massa ut lacinia mattis. Sed vel eleifend lorem. Pellentesque vitae felis pretium, pulvinar elit eu, euismod sapien. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.InformationQuerysApi()
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | maximum number of results to return (optional)

try:
    api_response = api_instance.find_information_querys(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationQuerysApi->find_information_querys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] 

### Return type

[**list[InformationQuery]**](InformationQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_informationquery_by_id**
> InformationQuery find_informationquery_by_id(id)



Returns a informationquery based on the ID

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.InformationQuerysApi()
id = 56 # int | ID of informationquery to fetch

try:
    api_response = api_instance.find_informationquery_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationQuerysApi->find_informationquery_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of informationquery to fetch | 

### Return type

[**InformationQuery**](InformationQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

