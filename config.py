#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = os.environ.get("PORT")
    APP_ID = os.environ.get("MicrosoftAppId", "ac077954-0a57-47e2-afa1-788cd5e5fd29")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
