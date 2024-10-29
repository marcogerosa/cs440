from enum import Enum
from datetime import datetime
from typing import List, Optional, Dict

class DeviceStatus(Enum):
    """Valid device statuses"""
    OFF = "off"
    ON = "on"
    STARTING = "starting"
    ERROR = "error"

class InvalidStateTransitionError(Exception):
    """Raised when attempting invalid state transition"""
    pass

class SmartDevice:
    # Define valid state transitions
    _VALID_TRANSITIONS = {
        DeviceStatus.OFF: [DeviceStatus.STARTING],
        DeviceStatus.STARTING: [DeviceStatus.ON, DeviceStatus.ERROR],
        DeviceStatus.ON: [DeviceStatus.OFF, DeviceStatus.ERROR],
        DeviceStatus.ERROR: [DeviceStatus.OFF]
    }

    def __init__(self, device_id: str):
        self._device_id = device_id
        self._status = DeviceStatus.OFF
        self._status_history: List[tuple[DeviceStatus, datetime]] = []
        # Record initial status
        self._add_to_history(self._status)

    @property
    def status(self) -> DeviceStatus:
        """Get current device status."""
        return self._status

    def get_status_history(self) -> List[tuple[DeviceStatus, datetime]]:
        """Get the status change history."""
        return list(self._status_history)  # Return a copy

    def can_transition_to(self, new_status: DeviceStatus) -> bool:
        """Check if transition to new status is valid."""
        return new_status in self._VALID_TRANSITIONS[self._status]

    def turn_on(self) -> None:
        """Start the device turn on sequence."""
        if self._status != DeviceStatus.OFF:
            raise InvalidStateTransitionError(
                f"Cannot turn on device from {self._status}"
            )
        self._change_status(DeviceStatus.STARTING)
        # Simulate startup completion
        self._change_status(DeviceStatus.ON)

    def turn_off(self) -> None:
        """Turn off the device."""
        if self._status not in [DeviceStatus.ON, DeviceStatus.ERROR]:
            raise InvalidStateTransitionError(
                f"Cannot turn off device from {self._status}"
            )
        self._change_status(DeviceStatus.OFF)

    def report_error(self) -> None:
        """Report device error."""
        if self._status == DeviceStatus.ERROR:
            return  # Already in error state
        self._change_status(DeviceStatus.ERROR)

    def reset_error(self) -> None:
        """Reset device from error state."""
        if self._status != DeviceStatus.ERROR:
            raise InvalidStateTransitionError("Device is not in error state")
        self._change_status(DeviceStatus.OFF)

    def _change_status(self, new_status: DeviceStatus) -> None:
        """
        Internal method to change device status.
        Validates transition and records change.
        """
        if not isinstance(new_status, DeviceStatus):
            raise ValueError(f"Invalid status type: {type(new_status)}")

        if not self.can_transition_to(new_status):
            raise InvalidStateTransitionError(
                f"Cannot transition from {self._status} to {new_status}"
            )

        self._status = new_status
        self._add_to_history(new_status)

    def _add_to_history(self, status: DeviceStatus) -> None:
        """Record status change in history."""
        self._status_history.append((status, datetime.now()))

## Usage Examples

# Example 1: Normal operation
device = SmartDevice("light_01")
print(device.status)  # DeviceStatus.OFF
device.turn_on()
print(device.status)  # DeviceStatus.ON
device.turn_off()
print(device.status)  # DeviceStatus.OFF

# Example 2: Error handling
device = SmartDevice("light_02")
device.turn_on()
device.report_error()  # Transitions to ERROR state
print(device.status)  # DeviceStatus.ERROR
device.reset_error()  # Resets to OFF state

# Example 3: View status history
device = SmartDevice("light_03")
device.turn_on()
device.report_error()
device.reset_error()

for status, timestamp in device.get_status_history():
    print(f"{timestamp}: {status}")


