# Contributing

This Howso&trade; opensource project only accepts code contributions from individuals and organizations that have signed a contributor license agreement. For more information on contributing and for links to the individual and corporate CLAs, please visit: https://www.howso.com/cla

## Reviewing Recipes before a Release

All recipes should be visually inspected, but there are a couple of specific things that are worth looking for:

- In `time_series_forecasting.ipynb` and `time_series_overview.ipynb`, ensure that the forecasted lines are smooth
  and that the generative time series visually match the original time series.
- In `car_type_demo.ipynb` ensure that Kia and Hyundai show up in the most similar records in the output of cell 21.
- In `drift_monitoring.ipynb` ensure that there is a clear distinction between the data pre-and post the start of the
  kiwi data.
- In `auditing_and_editing.ipynb` ensure that the prediction after the edit results in the correct predicted value.
- Always consider a message informing the user of a newer version of howso-engine as a blocker. Go back and ensure the
  requirements have had their version constraints updated to be compatible with the latest release and that they have
  been re-generated with the generate requirements pipeline. if this is not possible (due to version constraints from
  other packages), create a comment and mark the PR as changes requested. Or, if you're a human, fix it yourself before
  re-running the recipes pipeline.
