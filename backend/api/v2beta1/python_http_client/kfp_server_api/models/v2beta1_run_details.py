# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kfp_server_api.configuration import Configuration


class V2beta1RunDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pipeline_context_id': 'str',
        'pipeline_run_context_id': 'str',
        'task_details': 'list[V2beta1PipelineTaskDetail]'
    }

    attribute_map = {
        'pipeline_context_id': 'pipeline_context_id',
        'pipeline_run_context_id': 'pipeline_run_context_id',
        'task_details': 'task_details'
    }

    def __init__(self, pipeline_context_id=None, pipeline_run_context_id=None, task_details=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1RunDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pipeline_context_id = None
        self._pipeline_run_context_id = None
        self._task_details = None
        self.discriminator = None

        if pipeline_context_id is not None:
            self.pipeline_context_id = pipeline_context_id
        if pipeline_run_context_id is not None:
            self.pipeline_run_context_id = pipeline_run_context_id
        if task_details is not None:
            self.task_details = task_details

    @property
    def pipeline_context_id(self):
        """Gets the pipeline_context_id of this V2beta1RunDetails.  # noqa: E501

        Pipeline context ID of a run.  # noqa: E501

        :return: The pipeline_context_id of this V2beta1RunDetails.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_context_id

    @pipeline_context_id.setter
    def pipeline_context_id(self, pipeline_context_id):
        """Sets the pipeline_context_id of this V2beta1RunDetails.

        Pipeline context ID of a run.  # noqa: E501

        :param pipeline_context_id: The pipeline_context_id of this V2beta1RunDetails.  # noqa: E501
        :type pipeline_context_id: str
        """

        self._pipeline_context_id = pipeline_context_id

    @property
    def pipeline_run_context_id(self):
        """Gets the pipeline_run_context_id of this V2beta1RunDetails.  # noqa: E501

        Pipeline run context ID of a run.  # noqa: E501

        :return: The pipeline_run_context_id of this V2beta1RunDetails.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_run_context_id

    @pipeline_run_context_id.setter
    def pipeline_run_context_id(self, pipeline_run_context_id):
        """Sets the pipeline_run_context_id of this V2beta1RunDetails.

        Pipeline run context ID of a run.  # noqa: E501

        :param pipeline_run_context_id: The pipeline_run_context_id of this V2beta1RunDetails.  # noqa: E501
        :type pipeline_run_context_id: str
        """

        self._pipeline_run_context_id = pipeline_run_context_id

    @property
    def task_details(self):
        """Gets the task_details of this V2beta1RunDetails.  # noqa: E501

        Runtime details of the tasks that belong to the run.  # noqa: E501

        :return: The task_details of this V2beta1RunDetails.  # noqa: E501
        :rtype: list[V2beta1PipelineTaskDetail]
        """
        return self._task_details

    @task_details.setter
    def task_details(self, task_details):
        """Sets the task_details of this V2beta1RunDetails.

        Runtime details of the tasks that belong to the run.  # noqa: E501

        :param task_details: The task_details of this V2beta1RunDetails.  # noqa: E501
        :type task_details: list[V2beta1PipelineTaskDetail]
        """

        self._task_details = task_details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2beta1RunDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1RunDetails):
            return True

        return self.to_dict() != other.to_dict()