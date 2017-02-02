import os
import sys
from django.db.models import Q, F
from services.computenode.models import ComputeNodeService
from synchronizers.base.SyncInstanceUsingAnsible import SyncInstanceUsingAnsible
 
parentdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, parentdir)

class SyncComputeNodeService(SyncInstanceUsingAnsible):
 
    provides = [ComputeNodeService]
 
    observes = ComputeNodeService
 
    requested_interval = 0
 
    template_name = "compute_node_playbook.yaml"
 
    def __init__(self, *args, **kwargs):
        super(SyncComputeNodeService, self).__init__(*args, **kwargs)
 
    def fetch_pending(self, deleted):
 
        if (not deleted):
            objs = ComputeNodeService.get_tenant_objects().filter(
                Q(enacted__lt=F('updated')) | Q(enacted=None), Q(lazy_blocked=False))
        else:
            # If this is a deletion we get all of the deleted tenants..
            objs = ComputeNodeService.get_deleted_tenant_objects()
 
        return objs
 
    def get_computenodeservice(self, o):
        if not o.provider_service:
            return None
 
        computenodeservice = ComputeNodeService.get_service_objects().filter(id=o.provider_service.id)
 
        if not computenodeservice:
            return None
 
        return computenodeservice[0]
 
    # Gets the attributes that are used by the Ansible template but are not
    # part of the set of default attributes.
    def get_extra_attributes(self, o):
        fields = {}
        return fields
