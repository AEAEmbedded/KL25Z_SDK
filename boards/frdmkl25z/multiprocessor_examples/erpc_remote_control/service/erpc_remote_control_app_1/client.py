#
# Generated by erpcgen 1.4.0 on Fri Jan 20 08:45:15 2017.
#
# AUTOGENERATED - DO NOT EDIT
#

import erpc
from . import common, interface

# Client for remote_control_app_1
class remote_control_app_1Client(interface.Iremote_control_app_1):
    def __init__(self, manager):
        super(remote_control_app_1Client, self).__init__()
        self._clientManager = manager

    def button_pressed(self, which):
        # Build remote function invocation message.
        request = self._clientManager.create_request(isOneway=True)
        codec = request.codec
        codec.start_write_message(erpc.codec.MessageInfo(
                type=erpc.codec.MessageType.kOnewayMessage,
                service=self.SERVICE_ID,
                request=self.BUTTON_PRESSED_ID,
                sequence=request.sequence))
        if which is None:
            raise ValueError("which is None")
        codec.write_uint32(which)
        codec.end_write_message()

        # Send request.
        self._clientManager.perform_request(request)



