#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import numpy as np
import math


class Network(list):
    def __init__(self, file):
        self.title = ""
        self.filename = file
        self.nodes_dict = {}
        self.internal_nodes = 0
        self.models = {}
        self.gnd = '0'

    def __str__(self):
        s = "* " + self.title + "\n"
        for elem in self:
            s += elem.get_netlist_elem_line(self.nodes_dict) + "\n"
        return s[:-1]

    def create_node(self, name):
        got_ref = 0 in self.nodes_dict
        if name not in self.nodes_dict:
            if name == '0':
                int_node = 0
            else:
                int_node = int(len(self.nodes_dict)/2) + 1*(not got_ref)
            # TODO: The dictionary is constructed for double-direction lookup
            #  Can be further optimized for higher performance
            self.nodes_dict.update({int_node: name})
            self.nodes_dict.update({name: int_node})
        else:
            raise ValueError('Unable to create new node %s: node exists'
                             % name)
        return name

    def new_internal_node(self):
        ext_node = "INT" + str(self.internal_nodes)
        self.internal_nodes = self.internal_nodes + 1
        self.create_node(ext_node)
        return ext_node

    def get_nodes_number(self):
        return int(len(self.nodes_dict)/2)

    def is_int_node_internal_only(self, int_node):
        return self.nodes_dict[int_node].find("INT") > -1

    def is_nonlinear(self):
        for elem in self:
            if elem.is_nonlinear:
                return True
        return False


class NoSuchNodeError(Exception):
    pass

class CircuitError(Exception):
    pass

class NoSuchModelError(Exception):
    pass


