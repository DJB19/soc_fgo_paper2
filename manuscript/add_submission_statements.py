from pathlib import Path

path = Path("manuscript/paper2_draft.md")
text = path.read_text(encoding="utf-8")

marker = "## References"

insert_text = """## 7 Limitations and Future Work

Although the proposed nonlinear FGO method showed improved robustness against current sensor bias in both simulation and NASA B0005 validation, several limitations should be acknowledged.

First, the simulation study was based on a first-order RC battery model with controlled artificial current sensor bias. Although this setting allows a clear evaluation of bias-induced SOC drift, it does not fully represent all uncertainties encountered in practical battery management systems, such as temperature variation, battery aging, capacity fading, parameter mismatch, and sensor noise coupling.

Second, the real-data validation was conducted using the first discharge cycle of the NASA B0005 lithium-ion battery aging dataset. The NASA data provide realistic voltage, current, temperature, and time-series measurements; however, the current sensor bias analyzed in this study was artificially introduced into the measured current signal. Therefore, the NASA validation should be regarded as a preliminary real-data validation rather than a complete experimental validation under naturally occurring sensor bias.

Third, only one battery cell and one discharge cycle were used in the present validation. Future work will extend the evaluation to multiple battery cells, multiple aging stages, different discharge cycles, temperature-varying conditions, and real experimental current sensor bias scenarios. In addition, comparisons with other conventional SOC estimation methods, such as EKF, UKF, and particle-filter-based approaches, will be considered in future studies.

## Data Availability Statement

The processed simulation datasets, processed NASA B0005 validation data, and result files used in this study are available in the GitHub repository associated with this work:

https://github.com/DJB19/soc_fgo_paper2

The original NASA battery aging dataset is publicly available from the NASA Ames Prognostics Center of Excellence. The raw MATLAB data files are not redistributed in this repository; only processed CSV files and result files used for the present analysis are included.

## Code Availability Statement

The source code and scripts used for the simulation, current-bias generation, nonlinear FGO estimation, NASA B0005 processing, and result visualization are available at:

https://github.com/DJB19/soc_fgo_paper2

## Funding

This research received no external funding.

## Conflicts of Interest

The authors declare no conflicts of interest.

"""

if "## 7 Limitations and Future Work" in text:
    print("Submission statements already exist. No change made.")
else:
    idx = text.index(marker)
    text = text[:idx] + insert_text + "\n" + text[idx:]
    path.write_text(text, encoding="utf-8")
    print("Submission statements inserted before References.")
