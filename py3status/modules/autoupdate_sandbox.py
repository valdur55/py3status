"""
Trigger negative timeout_due.


@author valdur55 valdur@gmail.com

SAMPLE OUTPUT
{'full_text': '"Auto update off <sometime>"}
"""
import time
import datetime


class Py3status:
    """
    """

    # available configuration parameters
    _auto_update = False
    _update_interval = 0.5

    def _get_val(self):
        if self._auto_update:
            return f"Next update {self._update_interval} seconds"
        else:
            return f"Auto update off"

    def autoupdate_sandbox(self):
        return {
            "cached_until": time.perf_counter() + self._update_interval if self._auto_update else self.py3.CACHE_FOREVER,
            "full_text": f"{self._get_val()}  {datetime.datetime.now().time()}",
        }

    def _toggle_auto_update(self):
        self._auto_update = not self._auto_update

    def on_click(self, event):
        """
        Handles click events
        """
        button = event["button"]
        if button == 1:
            self._toggle_auto_update()
        elif button == 3:
            self._auto_update = False
        elif button == 2:
            self._auto_update = True



if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
