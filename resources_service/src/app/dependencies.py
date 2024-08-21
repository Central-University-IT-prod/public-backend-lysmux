from typing import Annotated

from fastapi import Depends, Request

from frousquare_api import FourSquareAPI
from kupibilet_api import KupiBiletAPI
from nominatim_api.api import NominatimAPI
from openmeteo_api import OpenMeteoAPI
from route_service import RouteService
from rzd_api import RzdAPI
from workflow import WorkflowData


def get_workflow_data(request: Request) -> WorkflowData:
    return request.state.workflow_data


WorkflowDataDep = Annotated[WorkflowData, Depends(get_workflow_data)]


def get_nominatim_api(workflow_data: WorkflowDataDep) -> NominatimAPI:
    return workflow_data.nominatim_api


NominatimAPIDep = Annotated[NominatimAPI, Depends(get_nominatim_api)]


def get_open_meteo_api(workflow_data: WorkflowDataDep) -> OpenMeteoAPI:
    return workflow_data.open_meteo_api


OpenMeteoAPIDep = Annotated[OpenMeteoAPI, Depends(get_open_meteo_api)]


def get_foursquare_api(workflow_data: WorkflowDataDep) -> FourSquareAPI:
    return workflow_data.foursquare_api


FourSquareAPIDep = Annotated[FourSquareAPI, Depends(get_foursquare_api)]


def get_rzd_api(workflow_data: WorkflowDataDep) -> RzdAPI:
    return workflow_data.rzd_api


RzdAPIDep = Annotated[RzdAPI, Depends(get_rzd_api)]


def get_kupinilet_api(workflow_data: WorkflowDataDep) -> KupiBiletAPI:
    return workflow_data.kupibilet_api


KupiBiletAPIDep = Annotated[KupiBiletAPI, Depends(get_kupinilet_api)]


def get_route_service(workflow_data: WorkflowDataDep) -> RouteService:
    return workflow_data.route_service


RouteServiceDep = Annotated[RouteService, Depends(get_route_service)]
