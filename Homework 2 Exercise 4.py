"""Homework 2 - Exercise 4: D-Separation and Conditional Independence

OBJECTIVE:
Implement utilities for analyzing conditional independence in Bayesian Networks using
the d-separation criterion.

YOUR TASK:
Complete the implementation of the following methods in the BayesianNetwork class:

1. is_d_separated(x, y, evidence):
   - Determine if nodes x and y are d-separated given the evidence set
   - Return True if x and y are conditionally independent given evidence

2. independencies(node, evidence):
   - Find all nodes that are independent of the given node conditioned on evidence
   - Return a list of all nodes that satisfy the conditional independence criterion
"""
from __future__ import annotations

from collections.abc import Iterable

# Student metadata
__author__ = "Foo Bar"
__matriculation_number__ = "012345679"
__email__ = "foo.bar@stud.tu-darmstadt.de"


class Node:
    """Node class for Bayesian Network."""

    def __init__(self, name: str, parents: list[Node] | None = None):
        """Initialize a Node. Append this node to its parents' children list.

        This node represents the distribution P(X | parents(X)).

        Args:
            name: name of the node
            parents: list of parent nodes
        """
        self.name = name
        if parents is None:
            parents = []
        self.parents = parents
        self.children = []  # This will be populated when a new node is created with this node as a parent

        # Append this node to its parents' children list
        for parent in parents:
            parent.children.append(self)


class BayesianNetwork:
    """Structure-only utilities for d-separation."""

    def __init__(self, nodes: list[Node]):
        """Initialize a Bayesian Network with a list of nodes.

        Args:
            nodes: List of all nodes in the Bayesian Network
        """
        self.nodes = nodes

    def is_d_separated(
        self,
        x: Node,
        y: Node,
        evidence: Iterable[Node] | None = None,
    ) -> bool:
        """Return True iff X ⫫ Y | Z.

        Args:
            x: The first node
            y: The second node
            evidence: Optional set of conditioning nodes

        Returns:
            True if x and y are d-separated given evidence, False otherwise.
        """
        # TODO: Implement
        raise NotImplementedError

    def independencies(self, node: Node, evidence: Iterable[Node]) -> list[Node]:
        """Return all nodes that are independent of `node` given `evidence`.

        Args:
            node: The node to find independencies for
            evidence: The set of conditioning nodes

        Returns:
            List of all nodes that are conditionally independent of the given node.
        """
        # TODO: Implement
        raise NotImplementedError
