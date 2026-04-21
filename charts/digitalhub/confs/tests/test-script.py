# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def main():
    if "CORE_CLIENT_ID" in os.environ:
        client_id = os.getenv("CORE_CLIENT_ID")
        client_secret = os.getenv("CORE_CLIENT_SECRET")
        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url='http://{{ include "core.fullname" .Subcharts.core }}:{{ .Subcharts.core.Values.service.port }}/auth/token',
            client_id=client_id,
            client_secret=client_secret,
            scope="openid profile credentials"
        )
        core_access = token["access_token"]
        session = token["aws_session_token"]
        aws_access_key_id = token["aws_access_key_id"]
        aws_secret_access_key = token["aws_secret_access_key"]
        print(f'export DHCORE_ACCESS_TOKEN="{core_access}"')
        print(f'export AWS_SESSION_TOKEN="{session}"')
        print(f'export AWS_ACCESS_KEY_ID="{aws_access_key_id}"')
        print(f'export AWS_SECRET_ACCESS_KEY="{aws_secret_access_key}"')
if __name__ == "__main__":
    main()
