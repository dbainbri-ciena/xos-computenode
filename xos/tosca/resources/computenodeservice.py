from services.computenode.models import ComputeNodeService
from service import XOSService

class XOSComputeNodeService(XOSService):
    provides = "tosca.nodes.ComputeNodeService"
    xos_model = ComputeNodeService
    copyin_props = ["view_url", "icon_url", "enabled", "published", "public_key", "versionNumber", 'nodeId', 'hostname', 'fabricAddress', 'hardwareAddress', 'role']
