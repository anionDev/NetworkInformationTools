from time import sleep
import requests
from ScriptCollection.GeneralUtilities import GeneralUtilities

version = "0.1.0"
__version__ = version


class NetworkInformationToolsCore:

    @GeneralUtilities.check_arguments
    def show_externalnetworkinformation_wrapper(self, loop: bool, proxy:str) -> None:
        self.loop_action(loop, lambda _:  self.show_externalnetworkinformation(proxy))

    @GeneralUtilities.check_arguments
    def show_externalnetworkinformation(self, proxy:str) -> None:
        proxies = None
        if GeneralUtilities.string_has_content( proxy ):
            proxies={"http" : proxy}
        response = requests.get('ipinfo.io', proxies=proxies)
        GeneralUtilities.write_message_to_stdout (f"External network information:")
        GeneralUtilities.write_message_to_stdout (response)

    @GeneralUtilities.check_arguments
    def loop_action(self, loop: bool, function) -> None:
        if loop:
            enabled:bool=True
            while enabled:
                try:
                    function()
                except:
                    pass
                finally:
                    sleep(2)
        else:
            function()
