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

from personio_data_python_sdk.model.absences_add_absence_periods_data_response import AbsencesAddAbsencePeriodsDataResponse as AbsencesAddAbsencePeriodsDataResponseSchema
from personio_data_python_sdk.model.create_absence_period_request import CreateAbsencePeriodRequest as CreateAbsencePeriodRequestSchema
from personio_data_python_sdk.model.error_inserting_absence_response import ErrorInsertingAbsenceResponse as ErrorInsertingAbsenceResponseSchema
from personio_data_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema
from personio_data_python_sdk.model.error_create_absence_response import ErrorCreateAbsenceResponse as ErrorCreateAbsenceResponseSchema

from personio_data_python_sdk.type.absences_add_absence_periods_data_response import AbsencesAddAbsencePeriodsDataResponse
from personio_data_python_sdk.type.error_create_absence_response import ErrorCreateAbsenceResponse
from personio_data_python_sdk.type.error_response import ErrorResponse
from personio_data_python_sdk.type.create_absence_period_request import CreateAbsencePeriodRequest
from personio_data_python_sdk.type.error_inserting_absence_response import ErrorInsertingAbsenceResponse

from ...api_client import Dictionary
from personio_data_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from personio_data_python_sdk.pydantic.error_create_absence_response import ErrorCreateAbsenceResponse as ErrorCreateAbsenceResponsePydantic
from personio_data_python_sdk.pydantic.create_absence_period_request import CreateAbsencePeriodRequest as CreateAbsencePeriodRequestPydantic
from personio_data_python_sdk.pydantic.absences_add_absence_periods_data_response import AbsencesAddAbsencePeriodsDataResponse as AbsencesAddAbsencePeriodsDataResponsePydantic
from personio_data_python_sdk.pydantic.error_inserting_absence_response import ErrorInsertingAbsenceResponse as ErrorInsertingAbsenceResponsePydantic

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
# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = CreateAbsencePeriodRequestSchema


request_body_create_absence_period_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
_auth = [
    'BearerAuth',
]
SchemaFor201ResponseBodyApplicationJson = AbsencesAddAbsencePeriodsDataResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: AbsencesAddAbsencePeriodsDataResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: AbsencesAddAbsencePeriodsDataResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorInsertingAbsenceResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorInsertingAbsenceResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorInsertingAbsenceResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = ErrorCreateAbsenceResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: ErrorCreateAbsenceResponse


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: ErrorCreateAbsenceResponse


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '404': _response_for_404,
    '422': _response_for_422,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_absence_periods_data_mapped_args(
        self,
        employee_id: int,
        time_off_type_id: int,
        start_date: date,
        end_date: date,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        start_time: typing.Optional[date] = None,
        end_time: typing.Optional[date] = None,
        half_day_start: typing.Optional[bool] = None,
        half_day_end: typing.Optional[bool] = None,
        comment: typing.Optional[str] = None,
        skip_approval: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if employee_id is not None:
            _body["employee_id"] = employee_id
        if time_off_type_id is not None:
            _body["time_off_type_id"] = time_off_type_id
        if start_date is not None:
            _body["start_date"] = start_date
        if end_date is not None:
            _body["end_date"] = end_date
        if start_time is not None:
            _body["start_time"] = start_time
        if end_time is not None:
            _body["end_time"] = end_time
        if half_day_start is not None:
            _body["half_day_start"] = half_day_start
        if half_day_end is not None:
            _body["half_day_end"] = half_day_end
        if comment is not None:
            _body["comment"] = comment
        if skip_approval is not None:
            _body["skip_approval"] = skip_approval
        args.body = _body
        if x_personio_partner_id is not None:
            _header_params["X-Personio-Partner-ID"] = x_personio_partner_id
        if x_personio_app_id is not None:
            _header_params["X-Personio-App-ID"] = x_personio_app_id
        args.header = _header_params
        return args

    async def _aadd_absence_periods_data_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/absence-periods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_absence_period_request.serialize(body, content_type)
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


    def _add_absence_periods_data_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/absence-periods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_absence_period_request.serialize(body, content_type)
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


class AddAbsencePeriodsDataRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_absence_periods_data(
        self,
        employee_id: int,
        time_off_type_id: int,
        start_date: date,
        end_date: date,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        start_time: typing.Optional[date] = None,
        end_time: typing.Optional[date] = None,
        half_day_start: typing.Optional[bool] = None,
        half_day_end: typing.Optional[bool] = None,
        comment: typing.Optional[str] = None,
        skip_approval: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_absence_periods_data_mapped_args(
            employee_id=employee_id,
            time_off_type_id=time_off_type_id,
            start_date=start_date,
            end_date=end_date,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            start_time=start_time,
            end_time=end_time,
            half_day_start=half_day_start,
            half_day_end=half_day_end,
            comment=comment,
            skip_approval=skip_approval,
        )
        return await self._aadd_absence_periods_data_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def add_absence_periods_data(
        self,
        employee_id: int,
        time_off_type_id: int,
        start_date: date,
        end_date: date,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        start_time: typing.Optional[date] = None,
        end_time: typing.Optional[date] = None,
        half_day_start: typing.Optional[bool] = None,
        half_day_end: typing.Optional[bool] = None,
        comment: typing.Optional[str] = None,
        skip_approval: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_absence_periods_data_mapped_args(
            employee_id=employee_id,
            time_off_type_id=time_off_type_id,
            start_date=start_date,
            end_date=end_date,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            start_time=start_time,
            end_time=end_time,
            half_day_start=half_day_start,
            half_day_end=half_day_end,
            comment=comment,
            skip_approval=skip_approval,
        )
        return self._add_absence_periods_data_oapg(
            body=args.body,
            header_params=args.header,
        )

class AddAbsencePeriodsData(BaseApi):

    async def aadd_absence_periods_data(
        self,
        employee_id: int,
        time_off_type_id: int,
        start_date: date,
        end_date: date,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        start_time: typing.Optional[date] = None,
        end_time: typing.Optional[date] = None,
        half_day_start: typing.Optional[bool] = None,
        half_day_end: typing.Optional[bool] = None,
        comment: typing.Optional[str] = None,
        skip_approval: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> AbsencesAddAbsencePeriodsDataResponsePydantic:
        raw_response = await self.raw.aadd_absence_periods_data(
            employee_id=employee_id,
            time_off_type_id=time_off_type_id,
            start_date=start_date,
            end_date=end_date,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            start_time=start_time,
            end_time=end_time,
            half_day_start=half_day_start,
            half_day_end=half_day_end,
            comment=comment,
            skip_approval=skip_approval,
            **kwargs,
        )
        if validate:
            return AbsencesAddAbsencePeriodsDataResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AbsencesAddAbsencePeriodsDataResponsePydantic, raw_response.body)
    
    
    def add_absence_periods_data(
        self,
        employee_id: int,
        time_off_type_id: int,
        start_date: date,
        end_date: date,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        start_time: typing.Optional[date] = None,
        end_time: typing.Optional[date] = None,
        half_day_start: typing.Optional[bool] = None,
        half_day_end: typing.Optional[bool] = None,
        comment: typing.Optional[str] = None,
        skip_approval: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> AbsencesAddAbsencePeriodsDataResponsePydantic:
        raw_response = self.raw.add_absence_periods_data(
            employee_id=employee_id,
            time_off_type_id=time_off_type_id,
            start_date=start_date,
            end_date=end_date,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            start_time=start_time,
            end_time=end_time,
            half_day_start=half_day_start,
            half_day_end=half_day_end,
            comment=comment,
            skip_approval=skip_approval,
        )
        if validate:
            return AbsencesAddAbsencePeriodsDataResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AbsencesAddAbsencePeriodsDataResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        employee_id: int,
        time_off_type_id: int,
        start_date: date,
        end_date: date,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        start_time: typing.Optional[date] = None,
        end_time: typing.Optional[date] = None,
        half_day_start: typing.Optional[bool] = None,
        half_day_end: typing.Optional[bool] = None,
        comment: typing.Optional[str] = None,
        skip_approval: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_absence_periods_data_mapped_args(
            employee_id=employee_id,
            time_off_type_id=time_off_type_id,
            start_date=start_date,
            end_date=end_date,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            start_time=start_time,
            end_time=end_time,
            half_day_start=half_day_start,
            half_day_end=half_day_end,
            comment=comment,
            skip_approval=skip_approval,
        )
        return await self._aadd_absence_periods_data_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        employee_id: int,
        time_off_type_id: int,
        start_date: date,
        end_date: date,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        start_time: typing.Optional[date] = None,
        end_time: typing.Optional[date] = None,
        half_day_start: typing.Optional[bool] = None,
        half_day_end: typing.Optional[bool] = None,
        comment: typing.Optional[str] = None,
        skip_approval: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_absence_periods_data_mapped_args(
            employee_id=employee_id,
            time_off_type_id=time_off_type_id,
            start_date=start_date,
            end_date=end_date,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            start_time=start_time,
            end_time=end_time,
            half_day_start=half_day_start,
            half_day_end=half_day_end,
            comment=comment,
            skip_approval=skip_approval,
        )
        return self._add_absence_periods_data_oapg(
            body=args.body,
            header_params=args.header,
        )

