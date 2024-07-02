class EntertainmentDevice:

    def connect_device_to_power_outlet(self, device): pass

class ConnectHDMI:

    def connect_to_device_via_hdmi_cable(self, device): pass

class ConnectEthernet:

    def connect_to_device_via_ethernet_cable(self, device): pass
class ConnectRca:

    def connect_to_device_via_rca_cable(self, device): pass

class Television(EntertainmentDevice, ConnectRca, ConnectHDMI):
    def connect_to_dvd(self, dvd_player):
        super().connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        super().connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, ConnectHDMI):
    def connect_to_tv(self, television):
        super().connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, ConnectHDMI, ConnectEthernet):
    def connect_to_tv(self, television):
        super().connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        super().connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, ConnectEthernet):
    def connect_to_tv(self, television):
        super().connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
