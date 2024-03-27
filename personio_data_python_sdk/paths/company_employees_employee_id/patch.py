# coding: utf-8

"""
    Personnel Data

    API for reading and writing personnel data including data about attendances, absences, documents, etc

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from personio_data_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from personio_data_python_sdk.api_response import AsyncGeneratorResponse
from personio_data_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from personio_data_python_sdk import schemas  # noqa: F401

from personio_data_python_sdk.model.employees_update_employee_fields_request import EmployeesUpdateEmployeeFieldsRequest as EmployeesUpdateEmployeeFieldsRequestSchema
from personio_data_python_sdk.model.employees_update_employee_fields_request1 import EmployeesUpdateEmployeeFieldsRequest1 as EmployeesUpdateEmployeeFieldsRequest1Schema
from personio_data_python_sdk.model.employee_update_error_response import EmployeeUpdateErrorResponse as EmployeeUpdateErrorResponseSchema
from personio_data_python_sdk.model.employee_updated_response import EmployeeUpdatedResponse as EmployeeUpdatedResponseSchema
from personio_data_python_sdk.model.employees_update_employee_fields_request_employee import EmployeesUpdateEmployeeFieldsRequestEmployee as EmployeesUpdateEmployeeFieldsRequestEmployeeSchema

from personio_data_python_sdk.type.employee_updated_response import EmployeeUpdatedResponse
from personio_data_python_sdk.type.employee_update_error_response import EmployeeUpdateErrorResponse
from personio_data_python_sdk.type.employees_update_employee_fields_request import EmployeesUpdateEmployeeFieldsRequest
from personio_data_python_sdk.type.employees_update_employee_fields_request1 import EmployeesUpdateEmployeeFieldsRequest1
from personio_data_python_sdk.type.employees_update_employee_fields_request_employee import EmployeesUpdateEmployeeFieldsRequestEmployee

from ...api_client import Dictionary
from personio_data_python_sdk.pydantic.employees_update_employee_fields_request_employee import EmployeesUpdateEmployeeFieldsRequestEmployee as EmployeesUpdateEmployeeFieldsRequestEmployeePydantic
from personio_data_python_sdk.pydantic.employee_update_error_response import EmployeeUpdateErrorResponse as EmployeeUpdateErrorResponsePydantic
from personio_data_python_sdk.pydantic.employees_update_employee_fields_request1 import EmployeesUpdateEmployeeFieldsRequest1 as EmployeesUpdateEmployeeFieldsRequest1Pydantic
from personio_data_python_sdk.pydantic.employees_update_employee_fields_request import EmployeesUpdateEmployeeFieldsRequest as EmployeesUpdateEmployeeFieldsRequestPydantic
from personio_data_python_sdk.pydantic.employee_updated_response import EmployeeUpdatedResponse as EmployeeUpdatedResponsePydantic

from . import path

# Header params
XPersonioPartnerIDSchema = schemas.StrSchema
XPersonioAppIDSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Personio-Partner-ID': typing.Union[XPersonioPartnerIDSchema, str, ],
        'X-Personio-App-ID': typing.Union[XPersonioAppIDSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_personio_partner_id = api_client.HeaderParameter(
    name="X-Personio-Partner-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XPersonioPartnerIDSchema,
)
request_header_x_personio_app_id = api_client.HeaderParameter(
    name="X-Personio-App-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XPersonioAppIDSchema,
)
# Path params
EmployeeIdSchema = schemas.Int32Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'employee_id': typing.Union[EmployeeIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_employee_id = api_client.PathParameter(
    name="employee_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EmployeeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = EmployeesUpdateEmployeeFieldsRequestSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = EmployeesUpdateEmployeeFieldsRequest1Schema


request_body_employees_update_employee_fields_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)
_auth = [
    'BearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = EmployeeUpdatedResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeeUpdatedResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeeUpdatedResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = EmployeeUpdateErrorResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: EmployeeUpdateErrorResponse


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: EmployeeUpdateErrorResponse


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_employee_fields_mapped_args(
        self,
        employee_id: int,
        employee: typing.Optional[EmployeesUpdateEmployeeFieldsRequestEmployee] = None,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if employee is not None:
            _body["employee"] = employee
        args.body = _body
        if x_personio_partner_id is not None:
            _header_params["X-Personio-Partner-ID"] = x_personio_partner_id
        if x_personio_app_id is not None:
            _header_params["X-Personio-App-ID"] = x_personio_app_id
        if employee_id is not None:
            _path_params["employee_id"] = employee_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_employee_fields_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update an employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_personio_partner_id,
            request_header_x_personio_app_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/employees/{employee_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_employees_update_employee_fields_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_employee_fields_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update an employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_personio_partner_id,
            request_header_x_personio_app_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/employees/{employee_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_employees_update_employee_fields_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateEmployeeFieldsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_employee_fields(
        self,
        employee_id: int,
        employee: typing.Optional[EmployeesUpdateEmployeeFieldsRequestEmployee] = None,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_employee_fields_mapped_args(
            employee_id=employee_id,
            employee=employee,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
        )
        return await self._aupdate_employee_fields_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_employee_fields(
        self,
        employee_id: int,
        employee: typing.Optional[EmployeesUpdateEmployeeFieldsRequestEmployee] = None,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_employee_fields_mapped_args(
            employee_id=employee_id,
            employee=employee,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
        )
        return self._update_employee_fields_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateEmployeeFields(BaseApi):

    async def aupdate_employee_fields(
        self,
        employee_id: int,
        employee: typing.Optional[EmployeesUpdateEmployeeFieldsRequestEmployee] = None,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeeUpdatedResponsePydantic:
        raw_response = await self.raw.aupdate_employee_fields(
            employee_id=employee_id,
            employee=employee,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            **kwargs,
        )
        if validate:
            return EmployeeUpdatedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeUpdatedResponsePydantic, raw_response.body)
    
    
    def update_employee_fields(
        self,
        employee_id: int,
        employee: typing.Optional[EmployeesUpdateEmployeeFieldsRequestEmployee] = None,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EmployeeUpdatedResponsePydantic:
        raw_response = self.raw.update_employee_fields(
            employee_id=employee_id,
            employee=employee,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
        )
        if validate:
            return EmployeeUpdatedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeUpdatedResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        employee_id: int,
        employee: typing.Optional[EmployeesUpdateEmployeeFieldsRequestEmployee] = None,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_employee_fields_mapped_args(
            employee_id=employee_id,
            employee=employee,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
        )
        return await self._aupdate_employee_fields_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        employee_id: int,
        employee: typing.Optional[EmployeesUpdateEmployeeFieldsRequestEmployee] = None,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_employee_fields_mapped_args(
            employee_id=employee_id,
            employee=employee,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
        )
        return self._update_employee_fields_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

