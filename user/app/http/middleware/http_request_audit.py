from starlette.types import ASGIApp, Message, Receive, Scope, Send
from starlette.datastructures import MutableHeaders
from starlette.requests import Request
from datetime import datetime


class HTTPRequestAuditMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        request = Request(scope)

        start_time = datetime.now()
        method_name = request.method
        query_params = request.query_params
        path_params = request.path_params

        with open("request_log.txt", mode="a") as reqfile:
            content = f"method: {method_name}, query param: {query_params}, path params: {path_params} received at {datetime.now()}\n"
            reqfile.write(content)

        async def send_with_extra_headers(message: Message):
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                process_time = datetime.now() - start_time
                headers.append("X-Time-Elapsed", str(process_time))

            await send(message)

        await self.app(scope, receive, send_with_extra_headers)
