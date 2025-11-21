"""Homework 2 - Exercise 2: Bayesian Network Implementation

OBJECTIVE:
Implement a Bayesian Network with nodes representing conditional probability distributions.
The network supports computing joint, marginal, and conditional log-likelihoods through
exact inference by enumeration over all possible variable assignments.

NOTE: All computations are performed in log-space for numerical stability.

YOUR TASK:
Complete the implementation of the following methods:

1. Node.log_likelihood(states):
   - Return the log-likelihood of this node's state given its parents' states
   - Use the stored conditional log-likelihood table (self.log_params)

2. BayesianNetwork.joint_log_likelihood(states):
   - Compute the joint log-likelihood of a complete assignment to all variables

3. BayesianNetwork.marginal_log_likelihood(states):
   - Compute the log-likelihood of a partial assignment.

4. BayesianNetwork.conditional_log_likelihood(states_query, states_evidence):
   - Compute log P(query | evidence) using the definition of conditional probability
"""

import numpy as np

__author__ = "Foo Bar"
__matriculation_number__ = "012345679"
__email__ = "foo.bar@stud.tu-darmstadt.de"


class Node:
    """Node class for Bayesian Network."""

    def __init__(self, name: str, params: list[float], parents: list["Node"] | None = None):
        """Initialize a Node. Append this node to its parents' children list.

        This node represents the distribution P(X | parents(X)).

        NOTE: All computations are done in log-space for numerical stability.
        The `params` are provided as probabilities but internally converted to log-space.

        The `params` argument is a list of probabilities for the True condition of this node,
        indexed by the binary representation of the parent states in the order defined by `self.parents`.

        Example: P(A)        => params = [P(A=True)]
                 P(A | B)    => params = [P(A=True|B=True), P(A=True|B=False)]
                 P(A | B, C) => params = [
                                    P(A=True|B=True,C=True),
                                    P(A=True|B=True,C=False),
                                    P(A=True|B=False,C=True),
                                    P(A=True|B=False,C=False)
                                ]

        Args:
            name: name of the node
            parents: list of parent nodes
            params: list of probabilities for the True condition. The length of params should be 2^len(parents)
        """
        self.name = name
        if parents is None:
            parents = []
        self.parents = parents
        self.children = []  # This will be populated when a new node is created with this node as a parent

        # Append this node to its parents' children list
        for parent in parents:
            parent.children.append(self)

        # For n parent variables, there are 2**n parent assignments
        assert len(params) == 2 ** len(parents)
        # Store probabilities as-is for reference
        self.params = params
        # Convert to log-space for internal computations (numerical stability)
        self.log_params = [np.log(p) if p > 0 else -np.inf for p in params]

    def log_likelihood(self, states: dict[str, bool]) -> float:
        """Get the log-likelihood of this node's current state given the state for its parents.

        NOTE: All computations are done in log-space for numerical stability.

        Note: `self.log_params` (internally computed) encodes log P(node = True | parents) for each parent assignment in
        the order defined by `self.parents`. Therefore:
        - If the queried state is True, return that stored log-likelihood.
        - If the queried state is False, return log(1 - exp(stored log-likelihood)).

        Args:
            states: dict mapping node name to boolean value. Must include this node and all its parents.

        Returns:
            Log-likelihood of this node taking the value provided in `states` given its parents' values.
        """
        # TODO: Implement
        raise NotImplementedError

    def __repr__(self):
        """Return a string representation of the node."""
        if not self.parents:
            return f"Node({self.name})"
        return f"Node({self.name} | {', '.join([p.name for p in self.parents])})"


class BayesianNetwork:
    """Bayesian Network class."""

    def __init__(self, nodes: list[Node]):
        """Initialize a Bayesian Network with a list of nodes.

        Args:
            nodes: List of all nodes in the Bayesian Network
        """
        self.nodes = nodes

    def joint_log_likelihood(self, states: dict[str, bool]) -> float:
        """Calculate the joint log-likelihood of a complete assignment of node conditions.

        NOTE: All computations are done in log-space for numerical stability.

        Args:
            states: dict of node name to boolean value representing a complete assignment for all nodes

        Returns:
            Joint log-likelihood of the given node conditions.
        """
        # TODO: Implement
        raise NotImplementedError

    def marginal_log_likelihood(self, states: dict[str, bool]) -> float:
        """Calculate the marginal log-likelihood of a (possibly partial) assignment.

        NOTE: All computations are done in log-space for numerical stability.

        Args:
            states: dict of node name to boolean value for a subset of nodes

        Returns:
            Marginal log-likelihood log P(states) obtained by summing over all assignments of the missing nodes.
        """
        # TODO: Implement
        raise NotImplementedError

    def conditional_log_likelihood(
        self,
        states_query: dict[str, bool],
        states_evidence: dict[str, bool],
    ) -> float:
        """Calculate the conditional log-likelihood log p(params | evidence).

        NOTE: All computations are done in log-space for numerical stability.

        Args:
            states_query: dict of node name to boolean value
            states_evidence: dict of node name to boolean value

        Returns:
            Conditional log-likelihood log p(query | evidence).
        """
        # TODO: Implement
        raise NotImplementedError


if __name__ == "__main__":
    # Example construction
    # NOTE: params are probabilities, converted to log-space internally
    a = Node(name="A", params=[0.2])  # P(A=True) = 0.2
    b = Node(name="B", parents=[a], params=[0.5, 0.8])  # P(B=True | A=True) = 0.5, P(B=True | A=False) = 0.8
    bn = BayesianNetwork(nodes=[a, b])

    # Example usage

    # Joint Log-Likelihood
    log_prob = bn.joint_log_likelihood(states={"A": True, "B": False})
    print("Joint Log-Likelihood log P(A=True, B=False):", log_prob)
    print("Joint Probability P(A=True, B=False):", np.exp(log_prob))

    # Marginal Log-Likelihood
    log_prob = bn.marginal_log_likelihood(states={"B": True})
    print("Marginal Log-Likelihood log P(B=True):", log_prob)
    print("Marginal Probability P(B=True):", np.exp(log_prob))

    # Conditional Log-Likelihood
    log_prob = bn.conditional_log_likelihood(
        states_query={"A": True},
        states_evidence={"B": False},
    )
    print("Conditional Log-Likelihood log P(A=True | B=False):", log_prob)
    print("Conditional Probability P(A=True | B=False):", np.exp(log_prob))
