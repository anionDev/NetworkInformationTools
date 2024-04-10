import argparse
from .NetworkInformationToolsCore import NetworkInformationToolsCore


def ShowExternalIPAddress() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--loop', action=argparse.BooleanOptionalAction, default=False,required=False)
    parser.add_argument('--proxy', default=None,required=False)
    args = parser.parse_args()
    NetworkInformationToolsCore().show_externalnetworkinformation_wrapper(args.loop, args.proxy)
    return 0
