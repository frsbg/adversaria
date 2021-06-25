# Adversaria: An Adversarial Steganographic Method for Imperceptible Video Watermarking
Audiomask is an imperceptible watermarking tool for verifying video content ownership.

## Overview
- Use this tool in your custom service (e.g. social network, platform, forum, etc) where this applies and makes sense to implement.

## Install
`pip install adversaria`

## Usage
Import the library with a de-facto alias if you'd like.
`import adversaria as ara`

Import the function to generate the perturbation key based on the metadata of both the original video content data, the `creator_id`, and among other variables. Even if target users know that their content is imperceptibly perturbed, they can't detransform the image if they don't know the metadata and psuedorandom unsigned long value that was used to create the key that they don't have access to, making it nearly impossible to decode the video content itself.  
`from adversaria.key_generation import generate_perturbation_key`

Given that we have created a unique `perturbation_key` with `generate_perturbation_key`, we must now apply this unique and imperceptible transformation scheme to the target content linked to the target user by iterating over the frames of the video content.
`from adversaria.adversarial import apply_perturbation_key`

As far as generating the unique `perturbation_key` for your target user, you must split the video so that each frame can be imperceptibly perturbed and its unique perturbation_key extrapolated continuously. It is optional to store JSON metadata for each frame and the norm-value and grad norm-type applied to each frame as far as understanding the constant and non-constant variables applied to generate these keys.
`from adversaria.video_split import split_video`

It is important to have persistent state management regarding the metadata assigned to both the vertices and the edges that link the original and imperceptibly perturbed video content to track (psuedonymous or non-pseudonymous) users. Thus, the `store_perturbation_state` function is meant to store a JSON object for each local graph that links an original post of video content to all the copies generated for each user. It'd be important to then setup the backend to handle this on-prem real-time perturbation operation because it requires generating copies of video only visible to target users that interact with the target content that is posted.
`from adversaria.utils import store_perturbation_state`

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

## References
- https://arxiv.org/pdf/1112.2809.pdf
- https://thesai.org/Downloads/Volume7No6/Paper_51-Data_Security_Using_Cryptography_and_Steganography_Techniques.pdf
- https://digitalcommons.wcl.american.edu/cgi/viewcontent.cgi?article=1053&context=research
- https://arxiv.org/pdf/1903.09822.pdf


