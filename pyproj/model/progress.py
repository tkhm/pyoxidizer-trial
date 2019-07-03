#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class ProgressRate(object):
    """
    サンプルダミークラス
    """

    def __init__(self, data):
        if data is not None:
            self.generated_at: str = None
            self.evaluation_date: str = data.get("evaluation_date", "")
            self.evaluation_year_month: str = data.get(
                "evaluation_year_month", 0)
