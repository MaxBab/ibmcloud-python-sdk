import json

from ibmcloud_python_sdk.config import params
from ibmcloud_python_sdk.auth import get_headers as headers
from ibmcloud_python_sdk.resource import resource_instance
from ibmcloud_python_sdk.utils.common import query_wrapper as qw
from ibmcloud_python_sdk.utils.common import resource_deleted


class Policy():

    def __init__(self):
        self.cfg = params()
        self.ri = resource_instance.ResourceInstance()

    def get_policies(self, account):
        """Retrieve policy list per account

        :param account: Account ID
        :return List of policies
        :rtype dict
        """
        try:
            # Connect to api endpoint for policies
            path = ("/v1/policies?account_id={}".format(account))

            # Return data
            return qw("auth", "GET", path, headers())["data"]

        except Exception as error:
            print("Error fetching policies for account {}. {}".format(
                account, error))

    def get_policy(self, policy):
        """Retrieve specific policy

        :param account: Account ID
        :param policy: Policy ID
        :return Policy information
        :rtype dict
        """
        try:
            # Connect to api endpoint for policies
            path = ("/v1/policies/{}".format(policy))

            # Return data
            return qw("auth", "GET", path, headers())["data"]

        except Exception as error:
            print("Error fetching policy {}. {}".format(policy, error))

    def get_authorizations(self, account):
        """Retrieve authorization list per account

        :param account: Account ID
        :return List of authorizations
        :rtype dict
        """
        try:
            # Connect to api endpoint for policies
            path = ("/v1/policies?account_id={}&type=authorization".format(
                account))

            # Return data
            return qw("auth", "GET", path, headers())["data"]

        except Exception as error:
            print("Error fetching authorizations for account {}. {}".format(
                account, error))

    def get_accesses(self, account):
        """Retrieve access list per account

        :param account: Account ID
        :return List of accesses
        :rtype dict
        """
        try:
            # Connect to api endpoint for policies
            path = ("/v1/policies?account_id={}&type=access".format(
                account))

            # Return data
            return qw("auth", "GET", path, headers())["data"]

        except Exception as error:
            print("Error fetching accesses for account {}. {}".format(
                account, error))

    def create_policy(self, **kwargs):
        """Create policy

        :param type: The policy type; either 'access' or 'authorization'.
        :param subjects: The subject attribute values that must match in
            order for this policy to apply in a permission decision.
        :param roles: A set of role cloud resource names (CRNs) granted by
            the policy.
        :param resources: The attributes of the resource. Note that only one
            resource is allowed in a policy.
        :return Policy response
        :rtype dict
        """
        # Build dict of argument and assign default value when needed
        args = {
            'type': kwargs.get('type'),
            'subjects': kwargs.get('subjects'),
            'roles': kwargs.get('roles'),
            'resources': kwargs.get('resources'),
        }

        # Construct payload
        payload = {}
        for key, value in args.items():
            if value is not None:
                if key == "subjects":
                    ri_info = None
                    for subject in args['subjects']:
                        for attribute in subject["attributes"]:
                            if attribute.get("name") == "serviceInstance":
                                ri_info = self.ri.get_resource_instance(
                                    attribute.get("value"))
                                attribute["value"] = ri_info["id"]
                    payload["subjects"] = args['subjects']
                elif key == "roles":
                    ro = []
                    for role in args["roles"]:
                        tmp_r = {}
                        tmp_r["role_id"] = role
                        ro.append(tmp_r)
                    payload["roles"] = ro
                elif key == "resources":
                    ri_info = None
                    for resource in args['resources']:
                        for attribute in resource["attributes"]:
                            if attribute.get("name") == "serviceInstance":
                                ri_info = self.ri.get_resource_instance(
                                    attribute.get("value"))
                                attribute["value"] = ri_info["id"]
                    payload["resources"] = args['resources']
                else:
                    payload[key] = value

        try:
            # Connect to api endpoint for policies
            path = "/v1/policies"

            # Return data
            return qw("auth", "POST", path, headers(),
                      json.dumps(payload))["data"]

        except Exception as error:
            print("Error creating policy. {}".format(error))

    def delete_policy(self, policy):
        """Delete policy

        :param policy: Policy ID
        :return Deletion status
        :rtype dict
        """
        # Check if policy exists and get information
        policy_info = self.get_policy(policy)
        if "errors" in policy_info:
            return policy_info

        try:
            # Connect to api endpoint for policies
            path = ("/v1/policies/{}".format(policy_info["id"]))

            data = qw("auth", "DELETE", path, headers())

            # Return data
            if data["response"].status != 204:
                return data["data"]

            # Return status
            return resource_deleted()

        except Exception as error:
            print("Error deleting policy {}. {}".format(policy, error))