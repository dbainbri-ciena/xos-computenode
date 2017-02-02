from django.db import models
from core.models import Service, PlCoreBase, Slice, Instance, Tenant, TenantWithContainer, Node, Image, User, Flavor, Subscriber, NetworkParameter, NetworkParameterType, Port, AddressPool
from core.models.plcorebase import StrippedCharField
import os
from django.db import models, transaction
from django.forms.models import model_to_dict
from django.db.models import Q
from operator import itemgetter, attrgetter, methodcaller
from core.models import Tag
from core.models.service import LeastLoadedNodeScheduler
import traceback
from xos.exceptions import *
from xos.config import Config

SERVICE_NAME = "ComputeNodeService"
SERVICE_NAME_VERBOSE = "Compute Node Service"

class ComputeNodeService(Service):
	KIND = SERVICE_NAME

	class Meta:
		app_label = "computenode"
		verbose_name = SERVICE_NAME_VERBOSE
		proxy = True

	simple_attributes = (
				("nodeId", "node-815ccfb0-e41b-11e6-be16-002590fa5f58"),
				("hostname", "niffty-default"),
				("fabricAddress", "10.1.1.2/24"),
				("hardwareAddress", "00:11:22:33:44:55"),
				("role", "compute"),
			    )

ComputeNodeService.setup_simple_attributes()
