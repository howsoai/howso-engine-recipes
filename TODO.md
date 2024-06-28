```py
# If you make any UI based changes, copy `updated_params` them from cell 3 into `initial_params`
initial_params = {} # < updated_params
feature_attributes = infer_feature_attribtes(df, initial_param)
```

Use

```py
widget.value = json.dumps{
    // Calculated features from infer_feature_attributes
    initial_features: feature_attributes,
    // featuresOut: {},
    // User supplied parameters
    initial_params: { features: {} tight_bounds: [] },
    # To be introduced through the UI
    updated_params: {}
    inference_required: false # We need a very strong definition of this
}
```

Inside widget:

```js
// Create an initail operating parameter which the UI will make changes into and out of
const operaional_params = {
  ...initial_params,
  features: {
    ...initial_params.features,
  }, // Diff, anything that isn't matching the initail_features
};

// every operation needs to update
updated_params = {
  ...operational_params,
  // params as have been manipulated the UI
  features: {}, // A diff of all changes to operaional_params.features through the UI and are *not* matching initial_features
};
```

```py
# If you make any UI based changes, copy `updated_params` them from cell 3 into `initial_params`
widget_values = json.loads(width.value)
if widget_values['inference_required'] or feature_attributes.is_inference_requied_for_updated_params(**widget_values['updated_params']):
    feature_attributes = infer_feature_attributes(df, **widget_values['updated_params'])
else
    feature_attributes = SingleTableFeatureAttribute(feature_attributes, **widget_values['updated_params'])
```

# V1 goals

Related, but not direct ancestor:

- Update existing notebooks to use `feature_attributes.to_dataframe()`

Widget changes:

- WTF time checkbox...
- Update for MD markup logic above to get `bounding_mode` inference (and every other field) right
- `updated_params` to plug into `feature_attributes` doing `infer_feature_attributes(df, **widget_values['updated_params'])`.
- Create a dedicated notebook for introducing the UI

# Medium goals

- create `SingleTableFeatureAttribute(feature_attributes, **widget_values['updated_params'])` #20698
- #20699 Need method for tight and auto bounds to include into widget.value supporting `bounding_mode` field output
  - This blocks synth notebooks from using the widget
- Should / can the widget block notebook progress until the user presses some sort of 'continue' dealing with the Run All problem?

# Long goals

- Eventually, we need `feature_attributes.to_widget()`
