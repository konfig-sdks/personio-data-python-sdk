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

from personio_data_python_sdk.model.public_report_response import PublicReportResponse as PublicReportResponseSchema
from personio_data_python_sdk.model.public_api_exception import PublicAPIException as PublicAPIExceptionSchema

from personio_data_python_sdk.type.public_report_response import PublicReportResponse
from personio_data_python_sdk.type.public_api_exception import PublicAPIException

from ...api_client import Dictionary
from personio_data_python_sdk.pydantic.public_api_exception import PublicAPIException as PublicAPIExceptionPydantic
from personio_data_python_sdk.pydantic.public_report_response import PublicReportResponse as PublicReportResponsePydantic

# Query params
LocaleSchema = schemas.StrSchema
PageSchema = schemas.IntSchema
LimitSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'locale': typing.Union[LocaleSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_locale = api_client.QueryParameter(
    name="locale",
    style=api_client.ParameterStyle.FORM,
    schema=LocaleSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
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
ReportIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'report_id': typing.Union[ReportIdSchema, str, ],
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


request_path_report_id = api_client.PathParameter(
    name="report_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ReportIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = PublicReportResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PublicReportResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PublicReportResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = PublicAPIExceptionSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: PublicAPIException


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: PublicAPIException


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = PublicAPIExceptionSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: PublicAPIException


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: PublicAPIException


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = PublicAPIExceptionSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: PublicAPIException


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: PublicAPIException


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_data_mapped_args(
        self,
        report_id: str,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        if locale is not None:
            _query_params["locale"] = locale
        if page is not None:
            _query_params["page"] = page
        if limit is not None:
            _query_params["limit"] = limit
        if x_personio_partner_id is not None:
            _header_params["X-Personio-Partner-ID"] = x_personio_partner_id
        if x_personio_app_id is not None:
            _header_params["X-Personio-App-ID"] = x_personio_app_id
        if report_id is not None:
            _path_params["report_id"] = report_id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aget_data_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_report_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_locale,
            request_query_page,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/custom-reports/reports/{report_id}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_data_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_report_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_locale,
            request_query_page,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/custom-reports/reports/{report_id}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetDataRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_data(
        self,
        report_id: str,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_data_mapped_args(
            report_id=report_id,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            locale=locale,
            page=page,
            limit=limit,
        )
        return await self._aget_data_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get_data(
        self,
        report_id: str,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_data_mapped_args(
            report_id=report_id,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            locale=locale,
            page=page,
            limit=limit,
        )
        return self._get_data_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class GetData(BaseApi):

    async def aget_data(
        self,
        report_id: str,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> PublicReportResponsePydantic:
        raw_response = await self.raw.aget_data(
            report_id=report_id,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            locale=locale,
            page=page,
            limit=limit,
            **kwargs,
        )
        if validate:
            return PublicReportResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PublicReportResponsePydantic, raw_response.body)
    
    
    def get_data(
        self,
        report_id: str,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> PublicReportResponsePydantic:
        raw_response = self.raw.get_data(
            report_id=report_id,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            locale=locale,
            page=page,
            limit=limit,
        )
        if validate:
            return PublicReportResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PublicReportResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        report_id: str,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_data_mapped_args(
            report_id=report_id,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            locale=locale,
            page=page,
            limit=limit,
        )
        return await self._aget_data_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        report_id: str,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_data_mapped_args(
            report_id=report_id,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            locale=locale,
            page=page,
            limit=limit,
        )
        return self._get_data_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

