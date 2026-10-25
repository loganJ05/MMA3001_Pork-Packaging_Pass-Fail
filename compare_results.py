
"""Compare YOLO inspection predictions with reference labels."""

from pathlib import Path
import pandas as pd

GROUND_TRUTH = Path("ground_truth.csv")
PREDICTIONS = Path("results/inspection_results.csv")
OUTPUT_FOLDER = Path("results")


def compare_results():
    """Create a comparison of actual and predicted inspection decisions."""

    actual = pd.read_csv(GROUND_TRUTH)
    predicted = pd.read_csv(PREDICTIONS)

    # Merge using the image filename
    comparison = actual.merge(
        predicted,
        on="image",
        how="left",
        validate="one_to_one"
    )

    if comparison["decision"].isna().any():
        raise ValueError(
            "Some reference images do not have matching predictions"
        )

    # Exclude images needing ground-truth review
    comparison = comparison[
        comparison["actual"].isin(["PASS", "FAIL"])
    ].copy()

    # Compare annotation-derived labels with inspection decisions
    summary = pd.crosstab(
        comparison["actual"],
        comparison["decision"]
    )

    summary = summary.reindex(
        index=["FAIL", "PASS"],
        columns=["FAIL", "REVIEW", "PROVISIONAL PASS"],
        fill_value=0
    )

    print("\nInspection comparison:")
    print(summary)

    # Calculate relevant inspection metrics
    actual_fail = comparison["actual"] == "FAIL"
    fail_count = actual_fail.sum()

    missed = (
        actual_fail &
        (comparison["decision"] == "PROVISIONAL PASS")
    ).sum()

    reviews = (comparison["decision"] == "REVIEW").sum()

    false_acceptance = (
        missed / fail_count if fail_count else float("nan")
    )

    review_rate = (
        reviews / len(comparison)
        if len(comparison) else float("nan")
    )

    print(f"\nTotal evaluated: {len(comparison)}")
    print(f"False acceptance rate: {false_acceptance:.2%}")
    print(f"Manual review rate: {review_rate:.2%}")

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    comparison.to_csv(
        OUTPUT_FOLDER / "comparison.csv",
        index=False
    )

    summary.to_csv(
        OUTPUT_FOLDER / "inspection_summary.csv"
    )

    return comparison, summary


if __name__ == "__main__":
    compare_results()
