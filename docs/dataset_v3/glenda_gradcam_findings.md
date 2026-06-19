# GLENDA ENID Grad-CAM Findings

## Objective

Investigate which image regions influence model predictions for endometriosis detection.

## Method

Grad-CAM (Gradient-weighted Class Activation Mapping) was applied to the final convolutional layer of the ResNet50 classifier.

## Observations

- Model attention was concentrated on localized tissue regions.
- Highest activations appeared near visually abnormal structures.
- Attention maps did not focus on image borders or irrelevant background regions.
- The model relied on specific anatomical features rather than the entire image.

## Interpretation

The Grad-CAM visualizations suggest that the classifier learned meaningful visual representations associated with endometriosis.

While clinical validation by domain experts would be required, the attention maps indicate that the model is not relying solely on dataset artifacts.

## Conclusion

The explainability analysis provides evidence that the ResNet50 model bases its predictions on localized pelvic tissue characteristics, improving trust and interpretability of the imaging pipeline.