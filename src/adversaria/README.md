# Adversaria


## Algorithm

```
video = "./video_path/target_creator_video.mp4"
video_dataset = split_video(video)
params = HParams(num_classes=10, adv_multiplier=0.2, adv_step_size=0.05, adv_grad_norm="infinity")
adv_model = build_adv_model(params=params)
for batch in video_dataset:
    # base perturbation
    adv_model.perturb_batch(batch)

# creating aggregate PGP keys and encoding them in video --> images
target_user_perturbation_key  = ""
creator_perturbation_key = ""

# independent of login or not, the spread of video is traced back to the source / target_user_id that it matches back to
# perturbation_params : adv_step_size, adv_grad_norm, creator_id, target_user_id
# we store the psuedorandom long unsigned values in the backend along with the id metadata and perturbation metadata to re-construct the original data from

# imperceptible adversarial examples is part of what will be used to trace users that spread original content, despite noise
# best way to track directly is to apply the unique scheme of the actual transformation to then compare against the target user video
# what if someone applies perturbations given a perturbed video? How would you trace the video then? 
# if they modify perturbed content, it's harder to trace
I see. The challenge here is that if they modify a perturbed video, they can use the same tool to obfuscate their own copy, which makes this tool relatively of low utility to an extent.



```
