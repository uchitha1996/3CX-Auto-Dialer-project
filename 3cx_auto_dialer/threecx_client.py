import os
import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class CallResult:
    call_id: str
    status: str
    detail: str
    timestamp: datetime


class ThreeCXClient:
    def __init__(self) -> None:
        self.base_url = os.environ.get("THREECX_BASE_URL", "").rstrip("/")
        self.client_id = os.environ.get("THREECX_CLIENT_ID", "")
        self.client_secret = os.environ.get("THREECX_CLIENT_SECRET", "")
        self.caller_extension = os.environ.get("THREECX_CALLER_EXTENSION", "")
        self.mode = os.environ.get("THREECX_MODE", "mock").lower()

        if self.mode not in {"mock", "real"}:
            raise ValueError("THREECX_MODE must be 'mock' or 'real'.")

    def make_call(self, phone_number: str) -> CallResult:
        if self.mode == "mock":
            return self._mock_call(phone_number)

        # TODO: implement real 3CX call initiation endpoint.
        # Suggested place to add API call:
        # POST {THREECX_BASE_URL}/call-control/v1/calls
        # with client credentials and caller extension headers.
        return CallResult(
            call_id="TODO_REAL_CALL_ID",
            status="todo",
            detail="TODO: implement 3CX call initiation endpoint",
            timestamp=datetime.utcnow(),
        )

    def transfer_call(self, call_id: str, target_extension: str) -> CallResult:
        if self.mode == "mock":
            return self._mock_transfer(call_id, target_extension)

        # TODO: implement real 3CX transfer endpoint.
        # Suggested place to add API call:
        # POST {THREECX_BASE_URL}/call-control/v1/calls/{call_id}/transfer
        return CallResult(
            call_id=call_id,
            status="todo",
            detail="TODO: implement 3CX transfer endpoint",
            timestamp=datetime.utcnow(),
        )

    def hangup_call(self, call_id: str) -> CallResult:
        if self.mode == "mock":
            return self._mock_hangup(call_id)

        # TODO: implement real 3CX hangup endpoint.
        # Suggested place to add API call:
        # POST {THREECX_BASE_URL}/call-control/v1/calls/{call_id}/hangup
        return CallResult(
            call_id=call_id,
            status="todo",
            detail="TODO: implement 3CX hangup endpoint",
            timestamp=datetime.utcnow(),
        )

    def _mock_call(self, phone_number: str) -> CallResult:
        fake_id = f"mock-{uuid.uuid4()}"
        status = "answered" if self._simulate_success(phone_number) else "failed"
        detail = "mock call placed" if status == "answered" else "mock call failed"
        return CallResult(
            call_id=fake_id,
            status=status,
            detail=detail,
            timestamp=datetime.utcnow(),
        )

    def _mock_transfer(self, call_id: str, target_extension: str) -> CallResult:
        detail = f"mock transfer to {target_extension}"
        return CallResult(
            call_id=call_id,
            status="transferred",
            detail=detail,
            timestamp=datetime.utcnow(),
        )

    def _mock_hangup(self, call_id: str) -> CallResult:
        return CallResult(
            call_id=call_id,
            status="hungup",
            detail="mock hangup",
            timestamp=datetime.utcnow(),
        )

    @staticmethod
    def _simulate_success(phone_number: str) -> bool:
        try:
            last_digit = int(phone_number[-1])
        except (IndexError, ValueError):
            return False
        return last_digit % 2 == 0
