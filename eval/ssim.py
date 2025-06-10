import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compute_ssim_structured(base_dir="data"):
    ssim_scores = []
    # Iterate through all class folders in 'generated'
    for class_name in os.listdir(os.path.join(base_dir, "gt_natural_nobg")):
        gen_class_dir = os.path.join(base_dir, "gt", class_name)
        gt_class_dir = os.path.join(base_dir, "gt_natural_nobg", class_name)
        
        if not os.path.exists(gt_class_dir):
            print(f"Warning: No GT folder for class {class_name}. Skipping.")
            continue
            
        for img_name in os.listdir(gen_class_dir):
            # Extract base filename without extension
            img_base = os.path.splitext(img_name)[0]
            
            # Find matching GT file (handles .jpg/.png automatically)
            gt_img_path = None
            for ext in ['.png', '.jpg', '.jpeg']:
                test_path = os.path.join(gt_class_dir, f"{img_base}{ext}")
                if os.path.exists(test_path):
                    gt_img_path = test_path
                    break
            
            if not gt_img_path:
                print(f"Warning: No GT image found for {class_name}/{img_name}. Skipping.")
                continue
                
            gen_img_path = os.path.join(gen_class_dir, img_name)
            
            try:
                gen_img = cv2.imread(gen_img_path)
                gt_img = cv2.imread(gt_img_path)
                
                if gen_img is None or gt_img is None:
                    print(f"Warning: Could not read {gen_img_path} or {gt_img_path}")
                    continue
                
                if gen_img.shape != gt_img.shape:
                    gt_img = cv2.resize(gt_img, (gen_img.shape[1], gen_img.shape[0]))
                
                ssim_val = ssim(gen_img, gt_img, 
                               channel_axis=-1 if len(gen_img.shape) == 3 else None,
                               data_range=255)
                ssim_scores.append(ssim_val)
                print(f"{class_name}/{img_name}: {ssim_val:.3f} (GT: {os.path.basename(gt_img_path)})")
                
            except Exception as e:
                print(f"Error processing {class_name}/{img_name}: {str(e)}")
                continue
    
    return np.mean(ssim_scores) if ssim_scores else 0.0

mean_ssim = compute_ssim_structured()
print(f"\nMean SSIM across all classes: {mean_ssim:.3f}")