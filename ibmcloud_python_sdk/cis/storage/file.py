from ibmcloud_python_sdk.utils import softlayer as sl
from SoftLayer import utils as sl_utils
from ibmcloud_python_sdk.utils.common import resource_not_found
from ibmcloud_python_sdk.utils.common import resource_error
from ibmcloud_python_sdk.utils.common import check_args


class File():

    def __init__(self):
        self.client = sl.client()
        self.file = sl.SoftLayer.FileStorageManager(self.client)

    def authorize_host_to_volume(self, **kwargs):
        """
        Authorizes hosts to File Storage Volumes

        :param volume_id: The File volume to authorize hosts to
        :param hardware_ids: A List of SoftLayer_Hardware ids
        :param virtual_guest_ids: A List of SoftLayer_Virtual_Guest ids
        :param ip_address_ids: A List of SoftLayer_Network_Subnet_IpAddress ids
        :param subnet_ids: A List of SoftLayer_Network_Subnet ids
        """

        args = ["volume_id", "hardware_ids", "virtual_guest_ids",
                "ip_address_ids", "subnet_ids"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'hardware_ids': kwargs.get('hardware_ids') or None,
            'virtual_guest_ids': kwargs.get('virtual_guest_ids') or None,
            'ip_address_ids': kwargs.get('ip_address_ids') or None,
            'subnet_ids': kwargs.get('subnet_ids') or None
        }
        try:
            self.file.authorize_host_to_volume(args['volume_id'],
                                               args['hardware_ids'],
                                               args['virtual_guest_ids'],
                                               args['ip_address_ids'],
                                               args['subnet_ids']
            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def cancel_file_volume(self, **kwargs):
        """
        Cancels the given file storage volume.

        :param volume_id (integer): The volume ID
        :param reason (string): The reason for cancellation
        :param immediate (boolean): Cancel immediately or on anniversary date
        """
        args = ["volume_id", "reason", "immediate"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'reason': kwargs.get('reason'),
            'immediate': kwargs.get('immediate')
        }

        try:
            return self.file.cancel_file_volume(args['volume_id'],
                                                reason=args['reason'],
                                                immediate=args['immediate']
            )
        except sl.SoftLayer.exceptions.SoftLayerError:
            return({"msg": "Storage Volume was already cancelled"})
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def cancel_snapshot_space(self, **kwargs):
        """
        Cancels snapshot space for a given volume.

        :param volume_id (integer): The volume ID
        :param reason (string): The reason for cancellation
        """
        args = ["volume_id", "reason"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'reason': kwargs.get('reason'),
        }

        try:
            return self.file.cancel_snapshot_space(args['volume_id'],
                                                reason=args['reason']
        )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def create_snapshot(self, **kwargs):
        """
        Creates a snapshot on the given file volume.

        :param volume_id (integer): The volume ID
        :param notes (string): The notes or "name" to assign the snapshot
        :return: Returns the id of the new snapshot
        """
        args = ["volume_id", "notes"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'notes': kwargs.get('notes'),
        }

        try:
            return self.file.create_snapshot(args['volume_id'],
                                                notes=args['notes']
        )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def deauthorize_host_to_volume(self, **kwargs):
        """
        Revokes authorization of hosts to File Storage Volumes.

        :param volume_id: The File volume to deauthorize hosts to
        :param hardware_ids: A List of SoftLayer_Hardware ids
        :param virtual_guest_ids: A List of SoftLayer_Virtual_Guest ids
        :param ip_address_ids: A List of SoftLayer_Network_Subnet_IpAddress ids
        :param subnet_ids: A List of SoftLayer_Network_Subnet ids
        :return: Returns an array of SoftLayer_Network_Storage_Allowed_Host
         objects which have access to the given File volume
        """

        args = ["volume_id", "hardware_ids", "virtual_guest_ids",
                "ip_address_ids", "subnet_ids"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'hardware_ids': kwargs.get('hardware_ids') or None,
            'virtual_guest_ids': kwargs.get('virtual_guest_ids') or None,
            'ip_address_ids': kwargs.get('ip_address_ids') or None,
            'subnet_ids': kwargs.get('subnet_ids') or None
        }

        try:
            return self.file.deauthorize_host_to_volume(args['volume_id'],
                            hardware_ids=args['hardware_ids'],
                            virtual_guest_ids=args['virtual_guest_ids'],
                            ip_address_ids=args['ip_address_ids'],
                            subnet_ids=args['subnet_ids']
        )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def delete_snapshot(self, snapshot_id):
        """
        Deletes the specified snapshot object.

        :param snapshot_id: The ID of the snapshot object to delete.
        """

        try:
            return self.file.delete_snapshot(snapshot_id)
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def disable_snapshots(self, **kwargs):
        """
        Disables snapshots for a specific file volume at a given schedule.

        :param volume_id (integer): The id of the volume
        :param schedule_type (string): 'HOURLY'|'DAILY'|'WEEKLY'
        """

        args = ["volume_id", "schedule_type"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'schedule_type': kwargs.get('schedule_type')
        }

        try:
            return self.file.disable_snapshots(args['volume_id'],
                                               args['schedule_type']
            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def enable_snapshots(self, **kwargs):
        """
        Disables snapshots for a specific file volume at a given schedule.

        :param volume_id (integer): The id of the volume
        :param schedule_type (string): 'HOURLY'|'DAILY'|'WEEKLY'
        :param retention_count (integer): The number of snapshots to attempt
         to retain in this schedule
        :param minute (integer): The minute of the hour at which HOURLY, DAILY,
         and WEEKLY snapshots should be taken
        :param hour (integer): The hour of the day at which DAILY and WEEKLY
         snapshots should be taken
        :param day_of_week (string|integer): The day of the week on which
         WEEKLY snapshots should be taken, either as a string ('SUNDAY')
         or integer ('0' is Sunday)
        """

        args = ["volume_id", "schedule_type", "retention_count", "minute"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'schedule_type': kwargs.get('schedule_type'),
            'retention_count': kwargs.get('retention_count'),
            'minute': kwargs.get('minute'),
            'hour': kwargs.get('hour'),
            'day_of_week': kwargs.get('day_of_week')
        }

        try:
            return self.file.enable_snapshots(args['volume_id'],
                                              args['schedule_type'],
                                              args['retention_count'],
                                              args['minute'],
                                              args['hour'],
                                              args['day_of_week']
            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def failback_from_replicant(self, **kwargs):
        """
        Failback from a volume replicant.

        :param volume_id (integer): The id of the volume
        :param replicant_id (integer): ID of replicant to failback from
        :return: Returns whether failback was successful or not
        """

        args = ["volume_id", "replicant_id"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'replicant_id': kwargs.get('replicant_id')
        }

        try:
            return self.file.failback_from_replicant(args['volume_id'],
                                               args['replicant_id']
            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def failover_to_replicant(self, **kwargs):
        """
        Failover to a volume replicant.

        :param volume_id (integer): The id of the volume
        :param replicant_id (integer): ID of replicant to failback from
        :param immediate (boolean): Flag indicating if failover is immediate
        :return: Returns whether failover was successful or not
        """

        args = ["volume_id", "replicant_id"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'replicant_id': kwargs.get('replicant_id'),
            'immediate': kwargs.get('immediate')
        }

        try:
            return self.file.failover_to_replicant(args['volume_id'],
                                               args['replicant_id'],
                                               immediate=args['immediate']
            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def get_file_volume_access_list(self, volume_id):
        """
        Returns a list of authorized hosts for a specified volume.

        :param volume_id (integer): The id of the volume
        :return: Returns a list of authorized hosts for a specified volume.
        """
        try:
            return self.file.get_file_volume_access_list(volume_id)
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def get_file_volume_details(self, volume_id):
        """
        Returns details about the specified volume.

        :param volume_id (integer): The id of the volume
        :return: Returns details about the specified volume.
        """
        try:
            return self.file.get_file_volume_details(volume_id)
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def get_file_volume_snapshot_list(self, volume_id):
        """
        Returns a list of snapshots for the specified volume.

        :param volume_id (integer): The id of the volume
        :return: Returns a list of snapshots for the specified volume.
        """
        try:
            return self.file.get_file_volume_snapshot_list(volume_id)
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def get_replication_locations(self, volume_id):
        """
        Acquires list of the datacenters to which a volume can be replicated.

        :param volume_id (integer): The ID of the primary volume to be replicated
        :return: Returns an array of SoftLayer_Network_Storage objects
        """
        try:
            return self.file.get_replication_locations(volume_id)
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def list_file_volumes(self, **kwargs):
        """
        Returns a list of file volumes.

        :param datacenter – Datacenter short name (e.g.: dal09)
        :param username: Name of volume.
        :param storage_type: Type of volume: Endurance or Performance
        :param order: Volume order id.
        :return: Returns a list of file volumes.
        """

        # Build dict of argument and assign default value when needed
        args = {
            'datacenter': kwargs.get('datacenter') or None,
            'username': kwargs.get('username') or None,
            'storage_type': kwargs.get('storage_type') or None,
            'order': kwargs.get('order') or None
        }

        _kwargs = {}
        _filter = sl_utils.NestedDict({})
        result = []

        _filter['nasNetworkStorage']['serviceResource']['type']['type'] = \
            (sl_utils.query_filter('!~ NAS'))

        _filter['nasNetworkStorage']['storageType']['keyName'] = (
            sl_utils.query_filter('*FILE_STORAGE*'))

        if args['username']:
            _filter['nasNetworkStorage']['username'] = \
                (sl_utils.query_filter(args['username']))

        if args['datacenter']:
            _filter['nasNetworkStorage']['serviceResource']['datacenter'][
                'name'] = (sl_utils.query_filter(args['datacenter']))

        if args['storage_type']:
            _filter['nasNetworkStorage']['storageType']['keyName'] = (
                sl_utils.query_filter('%s_FILE_STORAGE*' % args['storage_type'].upper()))

        if args['order']:
            _filter['nasNetworkStorage']['billingItem']['orderItem']['order']\
                ['id'] = (sl_utils.query_filter(args['order']))

        _kwargs['filter'] = _filter.to_dict()

        try:
            r = self.client.call('Account', 'getNasNetworkStorage', **_kwargs)
            for fs in r :
                result.append(fs)
            return result
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)


# ---

    def get_file_storages(self):
        """
        Retrieve file storage list

        :return: List of file storage
        :rtype: dict
        """
        try:
            file_storage = {}
            file_storage["file_storages"] = self.file.list_file_volumes()

            return file_storage

        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def get_file_storage(self, file_storage):
        """
        Retrieve specific file storage by ID

        :param file_storage: file_storage ID
        :return: file storage information
        :rtype: dict
        """
        try:
            return self.file.get_file_volume_details(file_storage)

        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def order_file_volume(self, **kwargs):
        """
        Places an order for a file volume.

        :param storage_type: "performance" or "endurance"
        :param location: Name of the datacenter in which to order the volume
        :param size: Size of the desired volume, in GB
        :param iops: Number of IOPs for a "Performance" order
        :param tier_level: Tier level to use for an "Endurance" order (0.25|2|4|10)
        :param snapshot_size: The size of optional snapshot space, if snapshot
         space should also be ordered (None if not ordered)
        :param service_offering: Requested offering package to use in the order
         ("storage_as_a_service", "enterprise", or "performance")
        :param hourly_billing_flag: Billing type, monthly (False) or
         hourly (True), default to monthly.
        :return: Created volume description
        :rtype: dict
        """

        args = ["storage_type", "location", "size"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'storage_type': kwargs.get('storage_type'),
            'location': kwargs.get('location'),
            'size': kwargs.get('size'),
            'iops': kwargs.get('iops') or None,
            'tier_level': kwargs.get('tier_level') or None,
            'snapshot_size': kwargs.get('snapshot_size') or None,
            'service_offering': kwargs.get('service_offering') or 'storage_as_a_service',
            'hourly_billing_flag': kwargs.get('hourly_billing_flag') or False
        }

        try:
            order = self.file.order_file_volume(args['storage_type'],
                                args['location'],
                                args['size'],
                                iops=args['iops'],
                                tier_level=args['tier_level'],
                                snapshot_size=args['snapshot_size'],
                                service_offering=args['service_offering'],
                                hourly_billing_flag=args['hourly_billing_flag']
            )
            return order
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def order_modified_volume(self, **kwargs):
        """
        Places an order for modifying an existing file volume.

        :param volume_id: The ID of the volume to be modified
        :param new_size: The new size/capacity for the volume
        :param new_iops:  The new IOPS for the volume
        :param new_tier_level: The new tier level for the volume
        :return:
        :rtype: dict
        """

        args = ["volume_id", "new_size", "new_iops", "new_tier_level"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('storage_type'),
            'new_size': kwargs.get('new_size'),
            'new_iops': kwargs.get('new_iops'),
            'new_tier_level': kwargs.get('new_tier_level')
        }

        try:
            return self.file.order_modified_volume(args['volume_id'],
                                               args['new_size'],
                                               args['new_iops'],
                                               args['new_tier_level']
                                            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def order_snapshot_space(self, **kwargs):
        """
        Orders snapshot space for the given file volume.

        :param volume_id: The ID of the volume
        :param capacity: The capacity to order, in GB
        :param tier: The tier level of the file volume, in IOPS per GB
        :param upgrade: Flag to indicate if this order is an upgrade
        :return:
        """

        args = ["volume_id", "capacity", "tier", "upgrade"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('storage_type'),
            'capacity': kwargs.get('capacity'),
            'tier': kwargs.get('tier'),
            'upgrade': kwargs.get('upgrade')
        }

        try:
            return self.file.order_snapshot_space(args['volume_id'],
                                               args['capacity'],
                                               args['tier'],
                                               args['upgrade']
                                            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def restore_from_snapshot(self, **kwargs):
        """
        Restores a specific volume from a snapshot

        :param volume_id: The ID of the volume
        :param snapshot_id: The id of the restore point
        """

        args = ["volume_id", "snapshot_id"]
        check_args(args, **kwargs)

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'snapshot_id': kwargs.get('snapshot_id')
        }

        try:
            return self.file.restore_from_snapshot(args['volume_id'],
                                               args['snapshot_id']
                                            )
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)

    def volume_set_note(self, **kwargs):
        """
        Set the notes for an existing block volume.

        :param volume_id: The ID of the volume to be modified.
        :param note: the note.
        """

        # Build dict of argument and assign default value when needed
        args = {
            'volume_id': kwargs.get('volume_id'),
            'note': kwargs.get('note')
        }
        try:
            result = self.file.volume_set_note(args['volume_id'],
                                               args['note']
                                            )
            return result
        except sl.SoftLayer.SoftLayerAPIError as error:
            return resource_error(error.faultCode, error.faultString)
