from subset_problem_generator import SubsetProblemGenerator


def dfs_subset_solve(target: int, numbers: list[int]) -> list[int] | None:
    # Base cases
    if target == 0:
        return []
    if len(numbers) == 0:
        return None
    if target < 0:
        return None

    # Exclude "branch" - exclude first number
    solution = dfs_subset_solve(target, numbers[1:])
    if solution is not None:
        return solution

    # Include "branch" - include first number
    solution = dfs_subset_solve(target - numbers[0], numbers[1:])
    if solution is not None:
        return [numbers[0]] + solution


if __name__ == "__main__":
    spg = SubsetProblemGenerator()
    (numbers, target_sum, subset) = spg.generate_problem()

    print(f"{numbers=}")
    print(f"{target_sum=}")
    print(f"{subset=}")
    print("--------")

    solution = dfs_subset_solve(target_sum, numbers)
    print(f"Solution: {solution}")
