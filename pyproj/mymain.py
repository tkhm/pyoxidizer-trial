#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import importlib
progress = importlib.import_module('model.progress')


def main():
    arg_psr = argparse.ArgumentParser()
    arg_psr.add_argument(
        "-m", "--mymainarg", required=True,
        help="Sample Argument")

    args = arg_psr.parse_args()

    input_evm_path = args.mymainarg
    print(input_evm_path)
    print(progress.ProgressRate(None))


if __name__ == "__main__":
    main()
