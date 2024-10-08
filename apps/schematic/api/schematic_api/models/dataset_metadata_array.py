# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from schematic_api.models.base_model_ import Model
from schematic_api.models.dataset_metadata import DatasetMetadata
from schematic_api import util

from schematic_api.models.dataset_metadata import DatasetMetadata  # noqa: E501


class DatasetMetadataArray(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datasets=None):  # noqa: E501
        """DatasetMetadataArray - a model defined in OpenAPI

        :param datasets: The datasets of this DatasetMetadataArray.  # noqa: E501
        :type datasets: List[DatasetMetadata]
        """
        self.openapi_types = {"datasets": List[DatasetMetadata]}

        self.attribute_map = {"datasets": "datasets"}

        self._datasets = datasets

    @classmethod
    def from_dict(cls, dikt) -> "DatasetMetadataArray":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DatasetMetadataArray of this DatasetMetadataArray.  # noqa: E501
        :rtype: DatasetMetadataArray
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datasets(self):
        """Gets the datasets of this DatasetMetadataArray.

        An array of dataset meatdata.  # noqa: E501

        :return: The datasets of this DatasetMetadataArray.
        :rtype: List[DatasetMetadata]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this DatasetMetadataArray.

        An array of dataset meatdata.  # noqa: E501

        :param datasets: The datasets of this DatasetMetadataArray.
        :type datasets: List[DatasetMetadata]
        """

        self._datasets = datasets
