import logging

logging.basicConfig(
    filename="/tmp/chargerate.log",
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='w',
    force=True)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

CHARGE_RATE_PATH = "/sys/devices/pci0000:00/0000:00:14.3/PNP0C09:00/VLV0100:00/hwmon/hwmon5/maximum_battery_charge_rate"


class Plugin:
    async def set_charge_current(self, current=250):
        logger.debug(f"Set charge current {current}")
        try:
            with open(CHARGE_RATE_PATH, "w") as f:
                f.write(str(current))
                logger.debug("Write successful")
            return True
        except Exception as e:
            logger.error(f"Write to charge rate failed: {e}")
        return False
