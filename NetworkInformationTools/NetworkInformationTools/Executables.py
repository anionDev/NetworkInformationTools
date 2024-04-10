import argparse
from .NetworkInformationToolsCore import NetworkInformationToolsCore


def ShowExternalIPAddress() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--loop', required=False, default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument('--proxy', required=False, default=None)
    args = parser.parse_args()
    NetworkInformationToolsCore().show_externalnetworkinformation_wrapper(args.loop, args.proxy)
    return 0
