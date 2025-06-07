
# TactileNet: Bridging the Accessibility Gap with AI-Generated Tactile Graphics for Individuals with Vision Impairment

Official repository for project: [TactileNet](https://tactilenet.github.io/)  
Authors: Adnan Khan, Alireza Choubineh, Mai A. Shaaban, Abbas Akkasi, Majid Komeili

---

## 🔍 Abstract

Tactile graphics provide critical access to visual information for individuals with vision loss. TactileNet introduces the first large-scale dataset and fine-tuned Stable Diffusion framework for generating embossing-ready 2D tactile templates from text or image inputs. Our method combines Low-Rank Adaptation (LoRA) and DreamBooth fine-tuning techniques to generate high-fidelity tactile graphics while reducing computational overhead. Evaluations with tactile experts show strong alignment with design guidelines and structural similarity to expert-crafted templates.

---

## 🧠 Method Overview

TactileNet uses class-specific LoRA and DreamBooth adapters fine-tuned on 66 categories of tactile graphics. Each adapter is trained on a small number of high-quality, expert-sourced images and their structured prompts. The model supports both text-to-image and image-to-image generation via Stable Diffusion v1.5.

Key Features:
- High SSIM similarity (0.538 vs expert designs)
- Better silhouette preservation (0.259 vs 0.215 in binary SSIM)
- Fully compatible with embossing workflows
- Supports prompt-level editing (e.g., add/remove logo, features)

---

## ⚙️ Setup Instructions

### 1. Set Up Stable Diffusion WebUI

Follow instructions from the [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) repository.

### 2. Clone Repository

```bash
git clone https://github.com/Adnan-Khan7/TactileNet.git
cd TactileNet
```

### 3. Copy Adapters

Download LoRA adapters from [Google Dive](https://drive.google.com/drive/folders/1XFn4wlcTogWbXtm4lc0cnyEN0vH7mBVy?usp=sharing)


Copy all the .safetensors files to:

```
stable-diffusion-webui/models/Lora/
```

### 4. Download Base Models

- **SD v1.5**: Get `v1-5-pruned-emaonly.safetensors` from [Hugging Face](https://huggingface.co/runwayml/stable-diffusion-v1-5).
- **Deliberate v3** (optional): [Download](https://drive.google.com/file/d/1bQo3oElYmsCmrcT-EgGeriBGszZmzUgW/view?usp=sharing)

Place in: `/stable-diffusion-webui/models/Stable-diffusion/`

---

## 🧪 Usage & Configuration

- Use the WebUI to generate tactile graphics with prompts like:
  > "Create a tactile graphic of an airplane for visually impaired users, emphasizing raised wings, fuselage, and tail."
- For **image-to-image** translation: Use denoising strength between `0.85–0.9`
- For **text-to-image** generation: Default settings (CFG=7, steps=20) suffice
- Example configuration shown below:

![Example](imgs/airplane_config.jpg)

---

## 📈 Evaluation Protocol

- **132 tactile graphics evaluated** (66 generated + 66 benchmark)
- **66 natural images** as reference
- Evaluation Metrics:
  - Pose accuracy (Q1)
  - Guideline adherence (Q2)
  - Expert-rated quality (Q3)
  - SSIM (structural fidelity)

---

## 📦 Reproducibility

Includes:
- `ssim.py` for evaluating image similarity
- Prompt examples
- Precomputed metrics (coming soon)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

This work was supported in part by MITACS and the Digital Alliance of Canada. We thank the student volunteers at the Intelligent Machines Lab, Carleton University, for their help with dataset curation and image matching.
