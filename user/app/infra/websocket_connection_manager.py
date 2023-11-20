from fastapi import WebSocket


class AppWebSocket:
    def __init__(self, client_id: int, websocket: WebSocket):
        self.client_id = client_id
        self.websocket = websocket


class WebSocketConnectionManager:
    def __init__(self):
        self.active_connections: list[AppWebSocket] = []

    async def connect(self, client_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(AppWebSocket(client_id, websocket))

    def get_websocket_by_client_id(self, client_id: int):
        websocket: WebSocket | None = None

        for item in self.active_connections:
            if item.client_id == client_id:
                websocket = item.websocket
                break

        return websocket

    def get_app_websocket_by_websocket(self, _websocket: WebSocket):
        websocket: AppWebSocket | None = None

        for item in self.active_connections:
            if item.websocket == _websocket:
                websocket = item
                break

        return websocket

    def disconnect(self, websocket: WebSocket):
        app_websocket = self.get_app_websocket_by_websocket(websocket)
        self.active_connections.remove(app_websocket)

    async def send_data(self, data: dict | list, client_id: int):
        websocket = self.get_websocket_by_client_id(client_id)

        if websocket is not None:
            await websocket.send_json(data)

    async def broadcast(self, data: str):
        for connection in self.active_connections:
            pass
            # await connection.send_json(
            #     {"id": 1, "title": "Personal", "description": "asdasdasd"}
            # )


websocket_connection_manager = WebSocketConnectionManager()
