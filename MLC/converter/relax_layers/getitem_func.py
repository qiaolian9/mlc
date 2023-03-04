import re
from loguru import logger
import torch.nn as nn
from tvm import relax
from .base_layer import BaseLayer

class GetItemFunc(BaseLayer):
    def __init__(self, bb, source_node, node_map=None, module=None, auto_gen=True):
        super(GetItemFunc, self).__init__(bb, source_node, node_map, module, auto_gen)

    def generate_node(self):
        x = self.node_map[self._source_node.args[0]]
        index = self._source_node.args[1]
        from ..register_relax.getshapevalue import getshapevalue
        out = self.bb.emit(getshapevalue(x, index), name_hint=self._name)
        
        logger.info("getaitem_layer: " + self._name + " created")
        self.value = out