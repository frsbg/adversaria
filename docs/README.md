# Audiomask: An Adversarial Steganographic Method for Imperceptible Video Watermarking
Audiomask is an imperceptible watermarking tool for verifying video content ownership.

## Algorithm
1. Split a video into a sum of its frames 
2. Apply a norm-bounded gaussian-distribution perturbation for each frame in the total frames
3. Create a partial key string from each frame based on the random perturbation scheme applied to the frame. Iteratively repeat steps 2-3 for all frames.
4. Merge the partial keys together to create a unique `perturbed_content_id` that links to the transformed image. The key generation process depends on the perturbations which are unique to each frame in the video in question. Therefore, the key generated must be linked to the imperceptibly perturbed image frame set. 

Note: we can track the dissemination of the content because users can only access the transformed image that they can't see or de-transform, so it's guaranteed that we can track content across the internet with reverse image search and de-transformation of the image. Even if there's video compression issues, data loss, video corruptions, and so forth, any existing frame of the entire video can also be traced (e.g. the partial unique perturbed content key) to the users that spread the video.

## Use Cases
- Detecting Copyright Infringement: If private content is stored on a platform where videos are privately shared to a local network, piracy can be identified this way to the users that spread the private content (centralized but private platforms). Social networks (independent of whether they are "centralized" or "decentralized") can follow the same approach to cryptographically signing content with adversarial deep learning and automatically flag stolen content.
- Social Network Analysis: Tracking content dissemination, more specifically understanding how content/media spreads, tagging meta-analyses of content with respect to its local and global graph of influence). Social networks generally attach a unique content_id but the media can be the same, but on different accounts. Generating a cryptographic key based on the unique perturbations applied either at the image-frame level or the entire image-frame set (for a video) helps to track how content spreads.
- Semi-Formal DeepFake Detection: If one cannot retrieve the original perturbation key that can help decode the image back to its original state, then the deepfakes can also be flagged because the imperceptibly transformed content is being tampered with. We can analyze the frames and decode the frames to see the difference with the method applied to change up the content. So if one chooses to make a deepfake, they'd make a deepfake based from an imperceptibly perturbed video that can trace their edits because the platform owner (social network facilitating content platform) can decode the transformed video back to its original state.

## Supported Formats
- Video 
- Images

## References
- https://arxiv.org/pdf/1112.2809.pdf
- https://thesai.org/Downloads/Volume7No6/Paper_51-Data_Security_Using_Cryptography_and_Steganography_Techniques.pdf
- https://digitalcommons.wcl.american.edu/cgi/viewcontent.cgi?article=1053&context=research
- https://arxiv.org/pdf/1903.09822.pdf


