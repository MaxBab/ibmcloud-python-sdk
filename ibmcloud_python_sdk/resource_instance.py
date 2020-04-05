import json
from ibmcloud_python_sdk.config import params
from ibmcloud_python_sdk.auth import get_headers as headers
from ibmcloud_python_sdk.utils.common import query_wrapper as qw
from ibmcloud_python_sdk.utils.common import resource_not_found

from ibmcloud_python_sdk.utils.common import check_args

class ResourceInstance():

    def __init__(self):
        self.cfg = params()
        # self.resource_group_id = "aef66560191746fe804b9a66874f62b1"
        self.resource_plan_id = "dc1460a6-37bd-4e2b-8180-d0f86ff39baa"

    def get_resource_instances(self, resource_plan_id=None):
        """Retrieve all dns resource instances
        """
        # set resource_plan default to DNS 
        if resource_plan_id == None:
            resource_plan_id = self.resource_plan_id
        result = []
        try:
            # Connect to api endpoint for resource instances
            path = ("/v2/resource_instances")

            resource_instances = qw("rg", "GET", path, headers())

            for resource_instance in resource_instances["data"]["resources"]:
                if resource_instance["resource_plan_id"] == resource_plan_id : 
                    result.append(resource_instance)
            # Return data
            return result
        except Exception as error:
            print("Error fetching resource instances. {}").format(error)
            raise


    # Get specific resource instance by ID or by name
    # This method is generic and should be used as prefered choice
    def get_resource_instance(self, resource_instance):
        by_name = self.get_resource_instance_by_name(resource_instance)
        if "errors" in by_name:
            for key_name in by_name["errors"]:
                if key_name["code"] == "not_found":
                    by_guid = self.get_resource_instance_by_guid(resource_instance)
                    if "errors" in by_guid:
                        return by_guid
                    return by_guid
                else:
                    return by_name
        else:
            return by_name


    # Get specific resource instance by GUID
    def get_resource_instance_by_guid(self, guid):
        """
        """
        try:
            # Connect to api endpoint for resource instances
            path = ("/v2/resource_instances/{}").format(guid)
            return qw("rg", "GET", path, headers())["data"]
        except Exception as error:
            print("Error fetching resource resource instance. {}").format(error)
            raise


    # Get specific resource instance by name
    def get_resource_instance_by_name(self, name):
        resource_instances = self.get_resource_instances()
        
        if len(resource_instances) == 0:
            return ({"errors": [{"code": "not_found",
                "message": "No resource instance suitable for DNS operations found."}]})
        
        if "errors" in resource_instances:
            return resource_instances

        for resource_instance in resource_instances:
            if resource_instance["name"] == name:
                    return resource_instance
            else:
                return ({"errors": [{"code": "not_found", 
                    "message": "No resource instance suitable for DNS operations found."}]
                    })