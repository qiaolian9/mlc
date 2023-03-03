from loguru import logger
from .base_layer import BaseLayer
from ..relax_utils import fetch_attr

class GetAttrFunc(BaseLayer):
    def __init__(self, bb, source_node, node_map=None, module=None, auto_gen=True):
        super(GetAttrFunc, self).__init__(bb, source_node, node_map, module, auto_gen)

    def generate_node(self):
        params = fetch_attr(self._module, self._source_node.target)
        out = self.create_params(self._name, params)
        
        logger.info("getattr_layer: " + self._name + " created")
        self.value = out