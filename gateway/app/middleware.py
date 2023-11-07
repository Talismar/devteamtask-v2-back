# from starlette.datastructures import URL
# from starlette.responses import RedirectResponse


# class RedirectsMiddleware:
#     def __init__(self, app, path_mapping: dict):
#         self.app = app
#         self.path_mapping = path_mapping

#     async def __call__(self, scope, receive, send):
#         if scope["type"] != "http":
#             await self.app(scope, receive, send)
#             return

#         # url = URL(scope=scope)

#         if True:
#             # url = url.replace(path=f"/api/project", port="8001")
#             # print(url)
#             # url = self.get_url_redirect(url.path)
#             url = "http://127.0.0.1:8001/project/"
#             response = RedirectResponse(url, status_code=301)
#             await response(scope, receive, send)
#             return

#         await self.app(scope, receive, send)

#     def get_url_redirect(self, initial_path: str):
#         service_name = initial_path.split("/")[1]
#         complement = "/".join(initial_path.split("/")[2:])

#         for base_path in self.path_mapping:
#             if service_name in base_path:
#                 return f"{self.path_mapping[base_path]}{complement}"

#         return False
