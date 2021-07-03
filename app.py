# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys
import traceback
from datetime import datetime
from http import HTTPStatus

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes
from bots import TeamsMessagingExtensionsActionBot
from config import DefaultConfig

CONFIG = DefaultConfig()

async def index(req: Request) -> Response:
    # Main bot message handler.
    
    return Response(status=HTTPStatus.OK, body="OK")

APP = web.Application(middlewares=[aiohttp_error_middleware])

APP.router.add_get("/", index)
if __name__ == "__main__":
    try:
        web.run_app(APP, port=CONFIG.PORT)
    except Exception as error:
        raise error
