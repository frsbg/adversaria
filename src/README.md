# Audiomask Core
facebook pixel meets next-generation video/image forensic watermarking

## Overview
- `video_split.py`: split video into frames 
- `key_generation.py`: get perturbation scheme to generate unique content ID for user viewing source content
- `adversarial.py`: define l2 norm-bounded perturbations to generate unique transformation scheme and use to generate a key string
- `client.py`: API client to return a JSON response with the perturbation_key generated from `key_generation.py` to generate a perturbation scheme. Pass the user's `content_id` to link the unique transformation to the user. Each transformed image can be de-transformed with a source `perturbation_key`.


## Implementation
