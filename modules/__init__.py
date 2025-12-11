# Make the 'modules' folder a real Python package
# and expose all DSA modules so ModuleInvoker can find them.

from . import dynamic_programming
from . import divide_conquer
from . import greedy
from . import graphs
from . import trees
from . import sorting
from . import arrays
from . import linked_list
from . import stacks_queues
from . import hashing

__all__ = [
    "dynamic_programming",
    "divide_conquer",
    "greedy",
    "graphs",
    "trees",
    "sorting",
    "arrays",
    "linked_list",
    "stacks_queues",
    "hashing"
]