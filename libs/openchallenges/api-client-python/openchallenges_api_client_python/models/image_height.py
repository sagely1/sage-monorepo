# coding: utf-8

"""
    OpenChallenges API

    Discover, explore, and contribute to open biomedical challenges.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ImageHeight(str, Enum):
    """
    The height of the image.
    """

    """
    allowed enum values
    """
    ORIGINAL = 'original'
    ENUM_32PX = '32px'
    ENUM_100PX = '100px'
    ENUM_140PX = '140px'
    ENUM_250PX = '250px'
    ENUM_500PX = '500px'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ImageHeight from a JSON string"""
        return cls(json.loads(json_str))


