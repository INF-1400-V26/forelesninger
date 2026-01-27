from itertools import combinations
from random import sample
from typing import Any, Optional, Sequence


class SubsetProblemGenerator:
    def __init__(
        self,
        n_num_subset=3,
        n_distractors=5,
        candidate_numbers: Optional[Sequence[int]] = None,
        max_iter=100,
    ) -> None:
        """Initialize the SubsetProblemGenerator.

        Parameters
        ----------
        n_num_subset : int, optional
            Number of numbers in the subset, by default 3
        n_distractors : int, optional
            Number of distractor numbers, by default 5
        candidate_numbers : list[int] | None, optional
            Candidate numbers to use, by default None
        max_iter : int, optional
            Maximum number of iterations to try generating a valid problem, by default 100

        Raises
        ------
        ValueError
            If candidate numbers are not unique or insufficient in count.
        ValueError
            If a valid problem cannot be generated within max_iter attempts.
        """
        self.n_num_subset = n_num_subset
        self.n_distractors = n_distractors
        self.max_iter = max_iter

        # Set candidate numbers
        if candidate_numbers is not None:
            # Validate user candidate numbers
            if len(candidate_numbers) < (n_num_subset + n_distractors):
                raise ValueError(
                    "Candidate numbers must be at least as many as the sum of "
                    "n_num_subset and n_distractors."
                )
            if len(set(candidate_numbers)) != len(candidate_numbers):
                raise ValueError("Candidate numbers must be unique.")
            self.candidate_numbers = candidate_numbers
        else:
            # Default candidate numbers (primes up to 200)
            self.candidate_numbers = (
                (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
                + (73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139)
                + (149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)
            )

    def _candidate_problem(self) -> tuple[list[int], int, list[int]]:
        """Generate a candidate problem instance."""
        sampled_nums = sample(
            population=self.candidate_numbers,
            k=(self.n_num_subset + self.n_distractors),
        )
        subset = sample(sampled_nums, k=self.n_num_subset)
        target_sum = sum(subset)

        return sorted(sampled_nums), target_sum, sorted(subset)

    def _validate_problem(self, problem: Any) -> bool:
        all_nums, target_sum, subset = problem
        for comb in combinations(all_nums, r=len(subset)):
            if sum(comb) == target_sum and set(comb) != set(subset):
                return False
        return True

    def generate_problem(self) -> tuple[list[int], int, list[int]]:
        """Generate an integer subset sum problem with a single solution

        Returns
        -------
        (numbers, subset_sum, subset_solution): tuple[list[int], int, list[int]]
            - numbers is the list of all available numbers
            - subset_sum is the target sum (sum of solution subset)
            - subset_solution is a list containing a solution subset

        """
        for _ in range(self.max_iter):
            problem = self._candidate_problem()
            if self._validate_problem(problem):
                return problem
            else:
                print("Generated problem invalid, retrying.")
        raise ValueError("Failed to generate a valid problem within max iterations")


if __name__ == "__main__":
    spg = SubsetProblemGenerator(
        n_num_subset=2,
        n_distractors=2,
        candidate_numbers=(19, 23, 29, 31, 37, 41, 43, 47),
    )
    for _ in range(10):
        nums, target, subset = spg.generate_problem()
        print("Numbers:", nums)
        print("Target Sum:", target)
        print("Subset that sums to target:", subset)
        print("----------------")
