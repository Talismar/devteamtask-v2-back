import hashlib
import hmac
from uuid import UUID

from fastapi import Depends, HTTPException, Request

from app.application.use_cases import (
    ProjectGetByIdUseCase,
    WebhookTaskUpdateStatusUseCase,
)
from app.infra.factories import make_project_get_by_id, make_webhook_task_update_status
from app.main.configuration.local import settings


async def github_webhooks(
    request: Request,
    project_use_case: ProjectGetByIdUseCase = Depends(make_project_get_by_id),
    webhook_use_case: WebhookTaskUpdateStatusUseCase = Depends(
        make_webhook_task_update_status
    ),
):
    signature = request.headers.get("x-hub-signature-256", "")
    content_type = request.headers.get("content-type")
    project_id = request.query_params.get("project_id")

    if content_type != "application/json":
        raise HTTPException(status_code=400)

    hmac_calculated = hmac.new(
        key=bytes(settings.GITHUB_WEBHOOK_SECRET, "utf-8"),
        msg=await request.body(),
        digestmod=hashlib.sha256,
    ).hexdigest()

    # if not hmac.compare_digest("sha256=" + hmac_calculated, signature):
    #     raise HTTPException(status_code=400)

    json_data = await request.json()
    # print(json_data)
    try:
        project = project_use_case.execute(UUID(project_id))
        project_id = project["project_data"]["id"]

        commits = json_data.get("commits")

        if commits is not None:
            for commit in commits:
                commit_message = commit["message"]
                webhook_use_case.execute(commit_message, project_id)  # type: ignore

    except Exception:
        raise HTTPException(status_code=400)

    return None
