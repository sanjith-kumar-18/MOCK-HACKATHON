import itertools
def held_karp(dists):
    
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))


def knapsack_held_karp(dists, cap):
    n = len(dists)
    max_val = max(dist for dist in dists)
    adjusted_dists = [dist + max_val for dist in dists]
    opt, _ = held_karp(adjusted_dists)
    remaining_cap = cap - opt

    if remaining_cap == 0:
        return opt

    knapsack_opt, _ = knapsack_held_karp(adjusted_dists, remaining_cap)
    return opt + knapsack_opt

# Example usage
dists = [[0, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1]]
cap = 4
print("Original knapsack opt:", knapsack_held_karp(dists, cap))
