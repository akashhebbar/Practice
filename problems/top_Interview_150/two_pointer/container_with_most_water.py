from typing import List


def container_with_most_water(height: List[int]) -> int:
    """
    Given an array of non-negative integers representing the heights of vertical lines,
    find two lines that together with the x-axis form a container that can hold the most water.

    Args:
        height: List of non-negative integers representing heights

    Returns:
        Maximum area of water that can be contained
    """
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


# Example usage
if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(container_with_most_water(height))
