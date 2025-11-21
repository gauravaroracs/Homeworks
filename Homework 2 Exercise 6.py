"""Homework 2 - Exercise 6: Markov Blanket

OBJECTIVE:
Implement a method to compute the Markov blanket of a node in a Bayesian Network.

The Markov blanket represents the minimal set of nodes that renders X conditionally
independent of all other nodes in the network.

YOUR TASK:
Complete the implementation of the following method in the Node class:

1. markov_blanket():
   - Return the union of these sets as the Markov blanket
"""

from __future__ import annotations

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

    def markov_blanket(self):
        """Computes and returns the Markov blanket of the target variable in a network.

        Returns:
            set: A set of variables representing the Markov blanket of the target variable.
        """
        # TODO: Implement this method
        raise NotImplementedError
